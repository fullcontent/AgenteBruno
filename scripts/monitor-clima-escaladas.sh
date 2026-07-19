#!/bin/bash
# Monitor de previsão do tempo para escaladas - Pico Paraná (1877m)
# Coordenadas corrigidas via mountain-forecast.com
# Roda a cada 4 horas e só alerta se houver risco
# Delega para o Python script que tem a lógica completa

cd "$(dirname "$0")"
python3 monitor-clima-escaladas.py 2>&1
