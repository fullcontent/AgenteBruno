# Fluxo de Trabalho (VoiceLearner)

1. **Trigger**: Diário, semanal ou toda vez que for rascunhar uma resposta (`COMUNICACAO`).
2. **Análise Base**:
   - Lê as últimas mensagens/e-mails ENVIADOS pelo próprio Bruno.
   - Extrai: Saudação comum, despedida comum, tamanho médio de frases, grau de informalidade (ex: usa emojis? Usa gírias?).
3. **Aplicação**:
   - Antes de entregar o rascunho de e-mail ao Bruno no `#comunicacao`, o texto passa pela máscara do VoiceLearner para remover "Prezado", "Espero que este e-mail o encontre bem" e substituir por "Fala [Nome],", ou similar realístico do Bruno.
