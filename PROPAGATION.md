# PROPAGATION.md — protocolo de escrita

Onde salvar o que precisa sobreviver a uma sessão. Se o output de uma tarefa se encaixa em mais de uma linha, salve em todas as que se aplicam.

| Tipo de conteúdo | Onde salvar | Exemplo |
|---|---|---|
| Decisão tomada (o quê, por quê, alternativas descartadas) | `memory/decisions.md` | "Optamos por não criar NOW.md/projects/knowledge — usar memory/tasks.md e memory/ideas.md" |
| Ideia nova, ainda não validada | `memory/ideas.md` | Uma oportunidade de negócio mencionada de passagem |
| Aprendizado reutilizável (o que funcionou/não funcionou) | `memory/lessons.md` | "Esteira de validação funciona melhor quando cada skill é rodada em sessão separada" |
| Tarefa ou projeto ativo, com status | `memory/tasks.md` | Status de `AgenteBruno`, `Fractional CTO`, etc. |
| Fato ou preferência que muda como qualquer sessão futura deve se comportar | `MEMORY.md` | Uma regra de decisão validada repetidamente |
| Objetivo de longo prazo revisado | `GOALS.md` | Mudança na visão de 10 anos ou nas prioridades trimestrais |
| Skill nova recorrente | `skills/{categoria}/{nome}/SKILL.md` | Um novo processo que se repete e merece virar skill |
| Nada disso se aplica | Não salvar — informação puramente conversacional não precisa persistir | — |

## Regra de ouro

Antes de encerrar qualquer tarefa que gerou estado novo (decisão, ideia, aprendizado, mudança de prioridade), pergunte: "isso precisa sobreviver a esta sessão?" Se sim, salve na linha certa da tabela acima antes de finalizar a resposta.
