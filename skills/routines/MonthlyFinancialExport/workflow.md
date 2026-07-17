# Fluxo de Trabalho (MonthlyFinancialExport)

1. **Trigger**: Todo dia 01 do mês.
2. **Coleta**:
   - Aciona `FINANCAS`: "Varra o Gmail por notas fiscais e faturas de cartão da última quinzena e faça o sumário."
3. **Compilação**:
   - Compila a notificação.
4. **Postagem**:
   - Tópico: `#crescimento-financas`.
   - Mensagem: "💰 **Fechamento Mensal**. Lembrete: acesse o seu banco e exporte o extrato em CSV/PDF para a pasta do Drive. Faturas recentes encontradas no Gmail: [Lista de Faturas]."
