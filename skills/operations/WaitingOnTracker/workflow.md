# Fluxo de Trabalho (WaitingOnTracker)

1. **Trigger**: Passivo, varre e-mails enviados rotulados ou com interrogação direcionada no Gmail.
2. **Processamento (`COMUNICACAO`)**:
   - Calcula a diferença de dias. Se `agora - envio >= 3 dias úteis` e não há reposta, a flag é levantada.
3. **Notificação**:
   - Posta no `#comunicacao`: "↩️ **Aguardando Resposta**. E-mail enviado para [Pessoa] sobre [Assunto] há 3 dias sem resposta. Quer rascunhar uma cobrança gentil?"
4. **Rascunho**:
   - Se Bruno disser "sim", rascunha usando o *VoiceLearner* e pede autorização final.
