# Fluxo de Trabalho (QuickCapture)

1. **Trigger**: O Bruno posta uma mensagem curta e injuntiva no Telegram (qualquer tópico ou no DM do Hermes) como: "Lembrar de comprar equipamento" ou "Preciso ligar pro contador sexta".
2. **Avaliação**: O Orquestrador reconhece que NÃO é uma pergunta e NÃO exige uma resposta elaborada.
3. **Ação (`OPERACOES`)**:
   - Extrai o verbo, o contexto e a data (se houver).
   - Usa a API do Google Tasks para criar a tarefa imediatamente.
4. **Confirmação**:
   - Responde ultra-curto no `#operacoes`: "✅ 'Ligar pro contador' salvo no Tasks para sexta-feira."
