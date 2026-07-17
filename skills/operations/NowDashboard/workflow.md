# Fluxo de Trabalho (NowDashboard)

1. **Trigger**: O Bruno aciona `/agora`.
2. **Coleta de Crise**:
   - Para toda a orquestração periférica.
   - Solicita ao `OPERACOES`: "Reuniões para as próximas 3h e tarefas marcadas como P1/Urgentíssimas."
   - Solicita ao `COMUNICACAO`: "Algum e-mail/mensagem que causará perda financeira ou de negócio se não respondido agora?"
3. **Filtro Implacável**:
   - O Orquestrador compila. Se a lista exceder 5 itens, o agente tem permissão/dever de cortar o que for menos crítico.
4. **Postagem**:
   - Retorna diretamente no `#comando`: "🚨 **Foco Absoluto**. Você só precisa se preocupar com isso nas próximas horas: [1 a 3 itens]."
