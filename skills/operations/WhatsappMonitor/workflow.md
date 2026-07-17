# Fluxo de Trabalho (WhatsappMonitor)

1. **Trigger**: O agente recebe um stream passivo de transcrições ou contexto de conversas do WhatsApp do Bruno via API (Evolution/n8n).
2. **Avaliação Semântica**:
   - O Orquestrador analisa o contexto à procura de intenções de agendamento (ex: "Vamos marcar amanhã às 14h?", "Te envio isso depois").
3. **Geração de Proposta (`OPERACOES`)**:
   - Posta no `#operacoes`: "⚠️ Notei que você disse para [Nome] que enviaria o contrato na sexta. Quer que eu crie um lembrete no Tasks?"
4. **Interação**:
   - Se o Bruno responder "sim", usa o *QuickCapture*. Se ignorar, a proposta expira no dia seguinte.
