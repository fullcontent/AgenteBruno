# AgenteBruno

Agent OS pessoal do Bruno, no formato esperado pelo framework [agent-os-hermes](https://github.com/okjpg/agent-os-hermes). Este repositório é a fonte de verdade que é sincronizada para `~/.hermes/` e lida pelo Hermes rodando via Docker na VPS.

## Estrutura

```
AgenteBruno/
├── AGENTS.md              # contrato operacional (bootloader)
├── SOUL.md                # identidade do agente
├── USER.md                # perfil do Bruno
├── GOALS.md                # objetivos de curto/médio/longo prazo
├── MAPA.md                # mapa de navegação
├── MEMORY.md              # memória longa curada
├── TOOLS.md                # ferramentas e permissões
├── PROPAGATION.md          # protocolo de escrita
├── HERMES.md                # instruções para o Hermes
├── agent-os.yaml           # manifesto estruturado
├── README.md
│
├── skills/
│   └── ideation/           # esteira de validação de ideias (7 skills sequenciais)
│       ├── sintetizador-padroes/SKILL.md
│       ├── arquiteto-problemas/SKILL.md
│       ├── escultor-mvp/SKILL.md
│       ├── arquiteto-minimalista/SKILL.md
│       ├── estrategista-riscos/SKILL.md
│       ├── analista-viabilidade/SKILL.md
│       └── auditor-equacao/SKILL.md
│
├── memory/
│   ├── decisions.md
│   ├── ideas.md
│   ├── lessons.md
│   └── tasks.md
│
├── templates/
│   ├── SKILL-TEMPLATE.md
│   └── ROOT-FILES-CHECKLIST.md
│
├── scripts/
│   ├── sync.sh
│   └── validate-agent-os.py
│
├── docs/
├── examples/
├── reports/               # gerado, não versionado
└── archive/
    └── bruno-persona.md   # persona original, absorvida em SOUL.md
```

Ver [MAPA.md](MAPA.md) para o que carregar em cada situação.

## Sincronização

```bash
chmod +x scripts/sync.sh
./scripts/sync.sh
```

Copia root files, `skills/` e `memory/` para `~/.hermes/`.

## Validação

```bash
python3 scripts/validate-agent-os.py
```

Confirma que a estrutura de root files, skills, memory e templates está íntegra.

## Uso

Este repositório não é lido diretamente — ele é sincronizado para `~/.hermes/`, de onde o Hermes carrega o contexto. Ver [HERMES.md](HERMES.md) para detalhes de instalação e sincronização na VPS.
