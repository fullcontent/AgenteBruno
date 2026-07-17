# BrunoOS

Agent OS pessoal do Bruno. A fonte oficial fica em `/opt/data/AgenteBruno-local` e é sincronizada para `/opt/data/` para o Hermes ler na VPS.

O fluxo de trabalho é simples: editar aqui, versionar no GitHub, e deixar o sync trazer as mudanças para o Hermes automaticamente.

## Estrutura

```
BrunoOS/
├── README.md
├── SOUL.md               # identidade do agente
├── USER.md               # perfil do Bruno
├── GOALS.md              # objetivos de curto/médio/longo prazo
├── DECISION_RULES.md     # critérios pra aceitar, priorizar ou recusar
├── THINKING.md           # como o agente pensa
├── WORKFLOW.md           # contrato operacional (bootloader)
├── WRITING_STYLE.md      # tom e voz
├── PROJECTS.md           # índice de projetos ativos
├── NOW.md                # o que está em foco agora
├── IDEAS.md              # ideias discutidas e avaliadas, ainda sem projeto
├── HERMES.md             # instruções de sincronização/uso no Hermes
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
├── memories/
│   └── USER.md            # espelho do perfil para o Hermes ler em ~/.hermes/memories/
│
├── archive/
│   ├── bruno-persona.md      # persona original, absorvida em THINKING.md/WRITING_STYLE.md
│   └── legacy-projects.md    # projetos de antes desta reestruturação
│
└── scripts/
    ├── sync.sh
    ├── update-and-sync.sh
    └── validate-brunos.py
```

Ver `WORKFLOW.md` para a ordem de leitura e o que carregar em cada situação.

## Sincronização

```bash
chmod +x scripts/update-and-sync.sh
./scripts/update-and-sync.sh
```

Copia `SOUL.md` para `/opt/data/SOUL.md`, `USER.md` para `/opt/data/USER.md` e as pastas `projects/`, `knowledge/`, `templates/`, `skills/`, `archive/`, `logs/`, `memories/` para `/opt/data/`.

## Validação

```bash
python3 scripts/validate-brunos.py
```

Confirma que a estrutura de root files, projects, knowledge, templates, skills, logs e memories está íntegra.

## Uso

Este repositório é a fonte oficial. Ele é sincronizado para `/opt/data/`, de onde o Hermes carrega o contexto. Ver `HERMES.md` para detalhes de instalação e sincronização na VPS.
