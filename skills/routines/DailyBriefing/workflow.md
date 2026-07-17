# Fluxo de Trabalho (DailyBriefing)

1. **Trigger**: Agendamento de cron via n8n/Hermes (ex: 07:00 AM).
2. **Coleta**:
   - Aciona `OPERACOES`: "Quais são os eventos de hoje e as tasks atrasadas/due today?"
   - Aciona `COMUNICACAO`: "Temos e-mails urgentes ou de VIPs não lidos nas últimas 12 horas?"
3. **Compilação**:
   - O Orquestrador compila os retornos aplicando ESTRITAMENTE o `HOUSE_STYLE.md`.
4. **Postagem**:
   - Roteia o output formatado diretamente para o tópico `#resumo-diario`.
