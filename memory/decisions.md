# memory/decisions.md — registro de decisões

Registra decisões tomadas, o raciocínio por trás delas e alternativas descartadas. Ver `PROPAGATION.md` para quando salvar aqui.

## Formato

```
### [Data] Título da decisão
**Decisão:** o que foi decidido.
**Por quê:** motivação, critérios do DECISION_RULES aplicados.
**Alternativas descartadas:** o que mais foi considerado.
```

## Decisões

### 2026-07-04 Reestruturação do repositório para o formato agent-os-hermes
**Decisão:** Migrar `AgenteBruno` de `.hermes/context/` + skills flat para o formato esperado pelo framework agent-os-hermes (root files + `skills/{categoria}/{nome}/SKILL.md` + `memory/` + `templates/`).
**Por quê:** O Hermes na VPS lê essa estrutura específica; o formato antigo não era compatível com o bootloader esperado.
**Alternativas descartadas:** Criar arquivos extras (`NOW.md`, `projects/`, `knowledge/`) do BrunoOS anterior — descartado por não fazerem parte do framework e não terem garantia de serem carregados pelo Hermes. Optou-se por usar `memory/tasks.md` e `memory/ideas.md` no lugar.
