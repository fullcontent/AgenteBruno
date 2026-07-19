#!/usr/bin/env python3
"""
Monitor de Previsão do Tempo para Escaladas
Monitora Pico Paraná (1877m) e arredores.
Dados corrigidos via mountain-forecast.com (coordenadas oficiais).
Alerta apenas se houver risco — silencioso quando tempo bom.
"""
import subprocess
import json
import sys
import re
from datetime import datetime, timezone, timedelta

# ═══════════════════════════════════════════════════════════════
# COORDENADAS OFICIAIS — Pico Paraná
# Fonte: mountain-forecast.com/peaks/Pico-Parana/forecasts/1877
# ═══════════════════════════════════════════════════════════════
# ANTES: -25.485, -48.705 (errado — ~26km de diferença)
# AGORA: -25.2523, -48.8092 (correto — do mountain-forecast)
LAT = "-25.2523"
LON = "-48.8092"
ALT = "1877"

# ── Fonte primária: Open-Meteo API ──
URL_OPENMETEO = (
    f"https://api.open-meteo.com/v1/forecast"
    f"?latitude={LAT}&longitude={LON}&altitude={ALT}"
    f"&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,weather_code,wind_speed_10m_max,wind_direction_10m_dominant"
    f"&current=temperature_2m,weather_code,wind_speed_10m,wind_direction_10m"
    f"&timezone=America%2FSao_Paulo"
)

# ── Fonte secundária: Mountain-Forecast (scraping) ──
MF_URL = "https://www.mountain-forecast.com/peaks/Pico-Parana/forecasts/1877"

# ── Mapeamento WMO → descrição ──
WMO_DESC = {
    0: "Céu limpo ☀️", 1: "Predom. limpo 🌤️", 2: "Parcial. nublado ⛅",
    3: "Nublado ☁️", 45: "Nevoeiro 🌫️", 48: "Nevoeiro c/ geada 🌫️",
    51: "Chuvisco fraco 🌦️", 53: "Chuvisco moderado 🌦️", 55: "Chuvisco intenso 🌦️",
    56: "Chuvisco congelante 🌦️❄️", 57: "Chuvisco congelante intenso 🌦️❄️",
    61: "Chuva fraca 🌧️", 63: "Chuva moderada 🌧️", 65: "Chuva forte 🌧️🌧️",
    66: "Chuva congelante fraca 🌧️❄️", 67: "Chuva congelante forte 🌧️❄️",
    71: "Neve fraca ❄️", 73: "Neve moderada ❄️", 75: "Neve intensa ❄️❄️",
    77: "Grãos de neve ❄️", 80: "Pancadas de chuva fracas 🌦️",
    81: "Pancadas de chuva moderadas 🌦️", 82: "Pancadas de chuva violentas 🌦️🌧️",
    85: "Pancadas de neve fracas ❄️", 86: "Pancadas de neve intensas ❄️❄️",
    95: "Tempestade ⛈️", 96: "Tempestade c/ granizo ⛈️🧊",
    99: "Tempestade c/ granizo intenso ⛈️🧊"
}

# ── Mapeamento weather_code → severidade ──
CHUVA_CODES = {51, 53, 55, 56, 57, 61, 63, 65, 66, 67, 80, 81, 82, 95, 96, 99}
CHUVA_FORTE_CODES = {65, 67, 82, 95, 96, 99}
NEVE_CODES = {71, 73, 75, 77, 85, 86}
TEMPESTADE_CODES = {95, 96, 99}

def main():
    # Buscar dados da API Open-Meteo
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={LAT}&longitude={LON}&altitude={ALT}"
        f"&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,weather_code,wind_speed_10m_max,wind_direction_10m_dominant"
        f"&current=temperature_2m,weather_code,wind_speed_10m,wind_direction_10m"
        f"&timezone=America%2FSao_Paulo"
    )

    try:
        result = subprocess.run(
            ["curl", "-s", "--max-time", "15", url],
            capture_output=True, text=True, timeout=20
        )
        data = json.loads(result.stdout)
    except Exception as e:
        print(f"ERRO: API falhou - {e}", file=sys.stderr)
        sys.exit(0)

    # ── Dados atuais ──
    current = data.get("current", {})
    temp_atual = current.get("temperature_2m")
    weather_atual = current.get("weather_code", 0)
    vento_atual = current.get("wind_speed_10m", 0)
    vento_dir_atual = current.get("wind_direction_10m")

    # ── Dados diários ──
    daily = data.get("daily", {})
    times = daily.get("time", [])
    temps_max = daily.get("temperature_2m_max", [])
    temps_min = daily.get("temperature_2m_min", [])
    chuva = daily.get("precipitation_sum", [])
    weather = daily.get("weather_code", [])
    ventos = daily.get("wind_speed_10m_max", [0]*7)
    vento_dir = daily.get("wind_direction_10m_dominant", [])

    if not times:
        print("Dados insuficientes", file=sys.stderr)
        sys.exit(0)

    # ── Determinar dia-alvo ──
    hoje = datetime.now(timezone.utc)
    dia_semana = hoje.weekday()

    if dia_semana >= 4:  # sex=4, sab=5
        TARGET_IDX = 3  # segunda
    elif dia_semana == 6:  # domingo
        TARGET_IDX = 1  # segunda
    else:
        TARGET_IDX = 1  # dia seguinte

    if len(times) <= TARGET_IDX:
        print("Dados insuficientes", file=sys.stderr)
        sys.exit(0)

    # ── Extrair dados do dia-alvo ──
    data_alvo = times[TARGET_IDX]
    chuva_alvo = chuva[TARGET_IDX]
    chuva_antes = sum(chuva[1:TARGET_IDX]) if TARGET_IDX > 1 else 0
    temp_max_alvo = temps_max[TARGET_IDX]
    temp_min_alvo = temps_min[TARGET_IDX]
    clima_alvo = weather[TARGET_IDX]
    vento_alvo = ventos[TARGET_IDX] if len(ventos) > TARGET_IDX else 0
    vento_dir_alvo = vento_dir[TARGET_IDX] if len(vento_dir) > TARGET_IDX else None

    # ── Critérios de ALERTA ──
    alertas = []

    # 1. Chuva no dia
    if chuva_alvo > 2:
        alertas.append(f"🌧️ Chuva no dia: {chuva_alvo:.1f}mm")

    # 2. Rocha molhada (chuva acumulada nos dias anteriores)
    if TARGET_IDX > 1 and chuva_antes > 5:
        alertas.append(f"⚠️ Rocha molhada: {chuva_antes:.1f}mm acumulados antes")

    # 3. Frio extremo
    if temp_max_alvo < 10:
        alertas.append(f"❄️ Frio extremo: máx {temp_max_alvo:.1f}°C")
    elif temp_min_alvo < 5:
        alertas.append(f"❄️ Mínima muito baixa: {temp_min_alvo:.1f}°C")

    # 4. Ventos fortes (Pico Paraná é exposto — ventos NW comuns)
    if vento_alvo > 50:
        alertas.append(f"💨 Ventos fortes: {vento_alvo:.0f} km/h")
    elif vento_alvo > 40:
        alertas.append(f"🌬️ Ventos moderados a fortes: {vento_alvo:.0f} km/h")

    # 5. Código WMO
    if clima_alvo in TEMPESTADE_CODES:
        alertas.append("⛈️ TEMPESTADE prevista")
    elif clima_alvo in CHUVA_FORTE_CODES:
        alertas.append("🌧️ Chuva forte prevista")
    elif clima_alvo in CHUVA_CODES:
        alertas.append("🌧️ Chuva prevista")
    elif clima_alvo in NEVE_CODES:
        alertas.append("❄️ Neve prevista")

    # ── Se houver alertas, imprimir mensagem ──
    if alertas:
        # Nome do dia-alvo
        dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
        dia_nome = dias_semana[(hoje.weekday() + TARGET_IDX) % 7]

        # Direção do vento
        dir_map = {0: "N", 45: "NE", 90: "L", 135: "SE", 180: "S", 225: "SO", 270: "O", 315: "NO", 360: "N"}
        dir_texto = ""
        if vento_dir_alvo is not None:
            dir_aprox = min(dir_map.keys(), key=lambda x: abs(x - vento_dir_alvo))
            dir_texto = dir_map[dir_aprox]

        print("=" * 50)
        print("⚠️ ALERTA DE TEMPO - ESCALADA")
        print("=" * 50)
        print()
        for a in alertas:
            print(a)
        print()
        print(f"📍 Pico Paraná, PR (1877m)")
        print(f"📅 {data_alvo} ({dia_nome})")
        print(f"🌡️  {temp_min_alvo:.0f}°C a {temp_max_alvo:.0f}°C")
        if vento_alvo > 0:
            dir_str = f" {dir_texto}" if dir_texto else ""
            print(f"💨 Vento: {vento_alvo:.0f} km/h{dir_str}")
        print()
        print("⚠️ RECOMENDAÇÃO: Avaliar plano B ou adiar a escalada")
        print("=" * 50)
    # Se sem alertas: sair silencioso (sem output = sem notificação)

if __name__ == "__main__":
    main()
