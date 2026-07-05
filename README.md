# BrunoOS

Agent OS pessoal do Bruno. Este repositório é a fonte de verdade que é sincronizada para `~/.hermes/` e lida pelo Hermes rodando via Docker na VPS.

## Estrutura

```
BrunoOS/
├── README.md
├── USER.md              # perfil do Bruno
├── GOALS.md              # objetivos de curto/médio/longo prazo
├── DECISION_RULES.md      # critérios pra aceitar, priorizar ou recusar
├── THINKING.md            # como o agente pensa
├── WORKFLOW.md            # contrato operacional (bootloader)
├── WRITING_STYLE.md       # tom e voz
├── PROJECTS.md            # índice de projetos ativos
├── NOW.md                 # o que está em foco agora
├── IDEAS.md               # ideias discutidas e avaliadas, ainda sem projeto
├── HERMES.md              # instruções de sincronização/uso no Hermes
│
├── projects/
│   ├── AventuFilm.md
│   ├── Ambialles.md
│   └── ...                # demais projetos, conforme forem enviados
│
├── knowledge/
│   ├── business.md
│   ├── ai.md
│   ├── storytelling.md
│   ├── audiovisual.md
│   ├── climbing.md
│   ├── tourism.md
│   └── spirituality.md
│
├── templates/
│   ├── PRD.md
│   ├── Proposal.md
│   ├── Meeting.md
│   ├── Decision.md
│   ├── Project.md
│   └── Skill.md
│
├── skills/
│   └── ideation/           # esteira de validação de ideias (8 skills sequenciais)
│       ├── ValidateNewIdea/    # orquestrador da esteira
│       ├── OpportunityScanner/
│       ├── PatternSynthesizer/
│       ├── ProblemArchitect/
│       ├── MVPSculptor/
│       ├── MinimalArchitect/
│       ├── RiskStrategist/
│       ├── ViabilityAnalyst/
│       └── EquationAuditor/
│           (cada skill tem README.md + workflow.md)
│
├── logs/
│   ├── decisions.md
│   └── lessons.md
│
├── archive/
│   ├── bruno-persona.md      # persona original, absorvida em THINKING.md/WRITING_STYLE.md
│   └── legacy-projects.md    # projetos de antes desta reestruturação
│
└── scripts/
    ├── sync.sh
    └── validate-brunos.py
```

Ver `WORKFLOW.md` para a ordem de leitura e o que carregar em cada situação.

## Sincronização

```bash
chmod +x scripts/sync.sh
./scripts/sync.sh
```

Copia root files e as pastas `projects/`, `knowledge/`, `templates/`, `skills/`, `archive/`, `logs/` para `~/.hermes/`.

## Validação

```bash
python3 scripts/validate-brunos.py
```

Confirma que a estrutura de root files, projects, knowledge, templates, skills e logs está íntegra.

## Uso

Este repositório não é lido diretamente — ele é sincronizado para `~/.hermes/`, de onde o Hermes carrega o contexto. Ver `HERMES.md` para detalhes de instalação e sincronização na VPS.
