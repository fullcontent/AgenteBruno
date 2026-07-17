# Fluxo de Trabalho (FocusAndQuietHours)

## Gatilho 1: Quiet Hours (Passivo)
1. **Regra**: Todo dia, entre as 20:00 e 08:00 (ou horário definido por variável de ambiente).
2. **Ação**: O Orquestrador retém QUALQUER output gerado pelas sub-skills (exceção: alertas marcados explicitamente com a flag 🔴 URGENTE que requeiram ação imediata, como quebra de servidor SaaS).
3. **Despejo**: Às 08:00, despeja as informações acumuladas junto com o DailyBriefing.

## Gatilho 2: Comando /foco (Ativo)
1. **Regra**: O Bruno envia `/foco 2h` no `#comando`.
2. **Ação**: O Orquestrador ativa a trava de silêncio por 120 minutos. Nenhuma notificação passa (nem urgentes, a não ser que classificadas como desastre iminente).
3. **Despejo**: Ao fim das 2h, o Orquestrador coleta as mensagens barradas e faz um sumário condensado no `#comando`: "Enquanto você estava focado: 2 e-mails chegaram, 1 lembrete de task atrasou."
