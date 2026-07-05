# MAPA.md — mapa de navegação

Este arquivo diz onde encontrar cada tipo de contexto no repositório. Use-o para decidir o que carregar antes de agir — não carregue tudo por reflexo.

## Root files

| Arquivo | Conteúdo | Quando carregar |
|---|---|---|
| `AGENTS.md` | Contrato operacional, roteamento de skills, política de aprovação | Sempre, no início da sessão |
| `SOUL.md` | Identidade, tom, princípios de raciocínio | Sempre, no início da sessão |
| `USER.md` | Perfil do Bruno — como pensa, decide, trabalha | Sempre, no início da sessão |
| `GOALS.md` | Objetivos de curto/médio/longo prazo | Ao avaliar prioridade ou alinhamento de uma decisão |
| `MAPA.md` | Este arquivo | Quando precisar localizar contexto |
| `MEMORY.md` | Memória longa curada (decisões e fatos que sobrevivem sessões) | Sempre, no início da sessão |
| `TOOLS.md` | Ferramentas disponíveis e permissões | Ao decidir como executar uma tarefa |
| `PROPAGATION.md` | Onde salvar o quê ao final de uma tarefa | Ao final de qualquer tarefa que gere estado novo |
| `HERMES.md` | Como este Agent OS é sincronizado e usado no Hermes | Ao lidar com sync/instalação |
| `agent-os.yaml` | Manifesto estruturado (machine-readable) | Quando uma ferramenta externa precisar ler o manifesto |
| `README.md` | Visão geral do repositório para humanos | Ao explicar o repo para alguém novo |

## Pastas

| Pasta | Conteúdo | Quando carregar |
|---|---|---|
| `skills/ideation/` | 7 skills da esteira de validação de ideias | Quando o Bruno trouxer uma ideia/oportunidade nova |
| `memory/decisions.md` | Registro de decisões tomadas e por quê | Ao revisitar ou justificar uma decisão passada |
| `memory/ideas.md` | Ideias capturadas, ainda não validadas | Ao capturar ou revisitar uma ideia |
| `memory/lessons.md` | Aprendizados reutilizáveis (o que funcionou/não funcionou) | Antes de repetir um tipo de tarefa já feito antes |
| `memory/tasks.md` | Tarefas e projetos ativos | Ao planejar o que fazer agora |
| `templates/` | Modelos reutilizáveis (skill, checklist) | Ao criar uma skill nova ou revisar root files |
| `scripts/` | `sync.sh` (sincroniza com `~/.hermes/`) e `validate-agent-os.py` (valida estrutura) | Ao sincronizar ou validar o repositório |
| `docs/` | Documentação de apoio, mais extensa que os root files | Quando um root file referenciar um doc |
| `examples/` | Exemplos de uso do Agent OS | Ao explicar como usar uma skill ou fluxo |
| `reports/` | Relatórios gerados (não versionados) | Ao gerar ou revisar output de uma execução |
| `archive/` | Material histórico, substituído por versões atuais | Só quando precisar entender a origem de algo |

## Regra de carregamento

Root files (1–7 na ordem do `AGENTS.md`) sempre entram. Tudo o resto — skills, memory, docs, examples — entra sob demanda, conforme a tarefa pedir.
