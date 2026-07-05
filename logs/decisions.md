# logs/decisions.md — registro de decisões

Registra decisões tomadas, o raciocínio por trás delas e alternativas descartadas. Ver `WORKFLOW.md` (seção "Onde salvar o quê") para quando salvar aqui. Para decisões novas, usar `templates/Decision.md`.

## Decisões

### 2026-07-04 Reestruturação do repositório para o formato agent-os-hermes
**Decisão:** Migrar `AgenteBruno` de `.hermes/context/` + skills flat para o formato esperado pelo framework agent-os-hermes (root files + `skills/{categoria}/{nome}/SKILL.md` + `memory/` + `templates/`).
**Por quê:** O Hermes na VPS lia essa estrutura específica; o formato antigo não era compatível com o bootloader esperado na época.
**Alternativas descartadas:** Criar arquivos extras (`NOW.md`, `projects/`, `knowledge/`) do BrunoOS anterior — descartado na época por não fazerem parte do framework agent-os-hermes.

### 2026-07-05 Reestruturação para o formato BrunoOS
**Decisão:** Abandonar a conformidade estrita com agent-os-hermes e migrar para a estrutura BrunoOS (root files `README/USER/GOALS/DECISION_RULES/THINKING/WORKFLOW/WRITING_STYLE/PROJECTS/NOW/IDEAS` + `projects/` + `knowledge/` + `templates/` + `skills/ideation/{Nome}/{README.md,workflow.md}` + `archive/` + `logs/`). Sincronização com a VPS via `scripts/sync.sh` foi mantida e adaptada para a nova estrutura, em vez de abandonada.
**Por quê:** Bruno definiu essa estrutura como a definitiva para o Agent OS pessoal, mais legível e navegável do que o schema genérico do agent-os-hermes.
**Alternativas descartadas:** Manter os dois formatos em paralelo — descartado por gerar duplicação e ambiguidade sobre qual é a fonte da verdade.
