# Fluxo de Trabalho (EveningWrapup)

1. **Trigger**: Agendamento de cron via n8n/Hermes (ex: 19:30 PM).
2. **Coleta**:
   - Aciona `OPERACOES`: "Quais tasks ficaram abertas hoje? Qual a primeira reunião de amanhã?"
   - Aciona `COMUNICACAO`: "Há e-mails lidos que requerem resposta imediata esquecidos no inbox?"
3. **Compilação**:
   - O Orquestrador compila os retornos (House Style) com tom tranquilizador.
   - Se não houver pendências, o output é um simples: "Dia limpo. Nada exige sua atenção amanhã cedo."
4. **Postagem**:
   - Roteia para o tópico `#resumo-diario`.
