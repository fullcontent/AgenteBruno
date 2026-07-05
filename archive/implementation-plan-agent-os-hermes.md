# Reestruturação AgenteBruno → Formato agent-os-hermes

## Contexto

O Hermes instalado na VPS (via Docker) usa o repositório [agent-os-hermes](https://github.com/okjpg/agent-os-hermes) como base. Esse framework espera uma estrutura específica de **root files** como bootloader, **skills** em pastas com `SKILL.md`, **memory** para persistência curada e **templates** para modelos reutilizáveis.

Nosso repositório atual (`AgenteBruno`) usa uma estrutura diferente (`.hermes/context/` + skills flat). Precisamos alinhar para que o Hermes leia corretamente ao sincronizar.

---

## Diagnóstico: De → Para

### Root Files (arquivos raiz)

| agent-os-hermes espera | Nosso repo tem | Ação |
|---|---|---|
| `AGENTS.md` — contrato operacional | *(não existe)* | **Criar** com base em WORKFLOW.md + THINKING.md + DECISION_RULES.md |
| `SOUL.md` — identidade do agente | `bruno-persona.md` | **Criar** migrando conteúdo de `bruno-persona.md` |
| `USER.md` — perfil do humano | `.hermes/context/USER.md` | **Mover** para raiz (já atualizado) |
| `MAPA.md` — mapa de navegação | *(não existe)* | **Criar** descrevendo toda a estrutura |
| `MEMORY.md` — memória longa curada | *(não existe)* | **Criar** com estrutura base |
| `TOOLS.md` — ferramentas e permissões | *(não existe)* | **Criar** listando ferramentas do Hermes + MCP/n8n |
| `PROPAGATION.md` — protocolo de escrita | *(não existe)* | **Criar** com tabela de propagação personalizada |
| `HERMES.md` — instruções p/ Hermes | *(não existe)* | **Criar** com instruções de sync e uso |
| `agent-os.yaml` — manifesto | *(não existe)* | **Criar** manifesto estruturado |
| `README.md` | `README.md` *(desatualizado)* | **Reescrever** |

### Arquivos existentes que serão absorvidos

| Arquivo atual | Destino no novo formato |
|---|---|
| `.hermes/context/GOALS.md` | Absorvido dentro de `USER.md` ou `MEMORY.md` → mover para raiz como `GOALS.md` (arquivo extra do Bruno, não do framework) |
| `.hermes/context/DECISION_RULES.md` | Absorvido dentro de `AGENTS.md` (seção de rails/decisão) |
| `.hermes/context/THINKING.md` | Absorvido dentro de `SOUL.md` (seção de como pensar) |
| `.hermes/context/WORKFLOW.md` | Absorvido dentro de `AGENTS.md` (seção de procedimentos) |
| `.hermes/context/WRITING_STYLE.md` | Absorvido dentro de `SOUL.md` (seção de tom/voz) |
| `.hermes/context/PROJECTS.md` | Mover para `memory/tasks.md` como tarefas/projetos ativos |
| `bruno-persona.md` | Absorvido dentro de `SOUL.md` → mover original para `archive/` |

### Pastas

| agent-os-hermes espera | Nosso repo tem | Ação |
|---|---|---|
| `skills/{categoria}/{nome}/SKILL.md` | `skills/ideacao_e_validacao/*.md` (flat) | **Reorganizar** em pastas por skill |
| `memory/` (decisions, ideas, lessons, tasks) | *(não existe)* | **Criar** com arquivos base |
| `templates/` (SKILL-TEMPLATE, ROOT-FILES-CHECKLIST) | *(não existe)* | **Criar** com modelos |
| `scripts/` | `sync.sh` (raiz) | **Mover** sync.sh para `scripts/` + criar validador |
| `archive/` | *(não existe)* | **Criar** |
| `docs/` | *(não existe)* | **Criar** com .gitkeep |
| `examples/` | *(não existe)* | **Criar** com .gitkeep |

---

## Proposed Changes

### 1. Root Files — Novos

#### [NEW] AGENTS.md
Contrato operacional. Consolida DECISION_RULES.md + WORKFLOW.md + THINKING.md. Inclui:
- Ordem de leitura no início da sessão
- Princípio central
- Como decidir o que fazer (roteamento de skills)
- Política de aprovação
- Esteira de validação de ideias (do WORKFLOW.md)
- Checklist de decisão (do DECISION_RULES.md)

#### [NEW] SOUL.md
Identidade do agente. Consolida `bruno-persona.md` + THINKING.md + WRITING_STYLE.md. Inclui:
- Identidade base (quem o agente é)
- Tese operacional
- Como pensar (primeiros princípios, tríade da síntese, red teaming)
- Tom e voz (direto, socrático, sem bajulação)
- Termos proibidos

#### [MODIFY] USER.md
Já está na raiz e atualizado. Sem mudanças.

#### [NEW] MAPA.md
Mapa de navegação do repositório com tabela de arquivos raiz e pastas.

#### [NEW] MEMORY.md
Memória longa curada. Estrutura base com princípios e seção de memórias vazia para preenchimento.

#### [NEW] TOOLS.md
Ferramentas e permissões. Lista de ferramentas que o Hermes pode usar (terminal, read_file, write_file, web_search, etc.) + integrações MCP/n8n.

#### [NEW] PROPAGATION.md
Protocolo de escrita. Tabela de propagação personalizada para o Bruno (onde salvar decisões, tarefas, ideias, aprendizados, etc.).

#### [NEW] HERMES.md
Como usar este Agent OS no Hermes. Instruções de instalação, sincronização e uso.

#### [NEW] agent-os.yaml
Manifesto estruturado do Agent OS.

#### [NEW] GOALS.md
Mover de `.hermes/context/` para a raiz. Conteúdo preservado.

---

### 2. Root Files — Removidos / Arquivados

#### [DELETE] `.hermes/context/` (pasta inteira)
Todo o conteúdo foi migrado para root files ou absorvido em AGENTS.md / SOUL.md.

#### [MOVE] `bruno-persona.md` → `archive/bruno-persona.md`

#### [DELETE] `.hermes/` (pasta local do repo)
Não é mais necessária. A sincronização para `~/.hermes/` é feita pelo `sync.sh`.

---

### 3. Skills — Reorganização

Formato esperado: `skills/{categoria}/{nome}/SKILL.md`

| Arquivo atual | Novo caminho |
|---|---|
| `sintetizador-padroes.md` | `skills/ideation/sintetizador-padroes/SKILL.md` |
| `arquiteto-problemas.md` | `skills/ideation/arquiteto-problemas/SKILL.md` |
| `escultor-mvp.md` | `skills/ideation/escultor-mvp/SKILL.md` |
| `arquiteto-minimalista.md` | `skills/ideation/arquiteto-minimalista/SKILL.md` |
| `estrategista-riscos.md` | `skills/ideation/estrategista-riscos/SKILL.md` |
| `analista-viabilidade.md` | `skills/ideation/analista-viabilidade/SKILL.md` |
| `auditor-equacao.md` | `skills/ideation/auditor-equacao/SKILL.md` |

> [!NOTE]
> Os nomes das skills foram mantidos em português para consistência com o conteúdo existente. A categoria mudou de `ideacao_e_validacao` para `ideation` (curto, sem caracteres especiais). O conteúdo dos arquivos `.md` existentes será migrado para o formato `SKILL.md` com frontmatter `name` e `description`.

#### [DELETE] `skills/ideacao_e_validacao/` (pasta antiga)

---

### 4. Memory

#### [NEW] `memory/decisions.md` — registro de decisões
#### [NEW] `memory/ideas.md` — ideias a explorar
#### [NEW] `memory/lessons.md` — aprendizados reutilizáveis
#### [NEW] `memory/tasks.md` — tarefas e projetos ativos (absorve PROJECTS.md)

Cada arquivo será criado com estrutura base para preenchimento.

---

### 5. Templates

#### [NEW] `templates/SKILL-TEMPLATE.md` — modelo para criar skills
#### [NEW] `templates/ROOT-FILES-CHECKLIST.md` — checklist dos root files

---

### 6. Scripts

#### [MOVE + MODIFY] `sync.sh` → `scripts/sync.sh`
Reescrever para:
1. Copiar root files da raiz para `~/.hermes/context/`
2. Sincronizar `skills/` recursivamente para `~/.hermes/skills/`
3. Sincronizar `memory/` para `~/.hermes/memory/`

#### [NEW] `scripts/validate-agent-os.py` — validador básico da estrutura

---

### 7. Pastas auxiliares

#### [NEW] `docs/.gitkeep`
#### [NEW] `examples/.gitkeep`
#### [NEW] `archive/` (receberá `bruno-persona.md`)
#### [NEW] `reports/.gitkeep`

---

### 8. README.md

#### [MODIFY] README.md
Reescrever com a nova estrutura, instruções de uso e sincronização.

---

### 9. .gitignore

#### [MODIFY] .gitignore
Atualizar para excluir `.hermes/` local, `.env`, `reports/` gerados, etc.

---

## Estrutura Final

```
AgenteBruno/
├── AGENTS.md              # contrato operacional (bootloader)
├── SOUL.md                # identidade do agente
├── USER.md                # perfil do Bruno
├── GOALS.md               # objetivos de curto/médio/longo prazo
├── MAPA.md                # mapa de navegação
├── MEMORY.md              # memória longa curada
├── TOOLS.md               # ferramentas e permissões
├── PROPAGATION.md         # protocolo de escrita
├── HERMES.md              # instruções para o Hermes
├── agent-os.yaml          # manifesto estruturado
├── README.md              # documentação do repo
├── .gitignore
│
├── skills/
│   └── ideation/
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
├── reports/
└── archive/
    └── bruno-persona.md
```

---

## Open Questions

> [!IMPORTANT]
> **Arquivos extras do BrunoOS (NOW.md, projects/, knowledge/)**: Na sua proposta anterior havia `NOW.md`, `projects/`, `knowledge/`. Esses NÃO existem no framework agent-os-hermes. Sugiro duas opções:
> 1. **Não criar** — usar `memory/tasks.md` para "agora" e `memory/ideas.md` para projetos/ideias (mais alinhado ao framework).
> 2. **Criar como extensões** — adicionar como arquivos extras na raiz e pastas customizadas, mas sem garantia de que o Hermes os carregue automaticamente.
> 
> Recomendo a opção 1 por simplicidade e compatibilidade.

> [!NOTE]
> **Conteúdo dos novos root files**: Os arquivos `AGENTS.md`, `SOUL.md`, `MAPA.md`, `MEMORY.md`, `TOOLS.md`, `PROPAGATION.md`, `HERMES.md` e `agent-os.yaml` serão criados **já preenchidos** com o conteúdo do Bruno, consolidando o que já existe nos arquivos de contexto atuais. Não serão apenas esqueletos vazios.

---

## Verification Plan

### Automated
```bash
python3 scripts/validate-agent-os.py
```

### Manual
1. Verificar árvore de arquivos com `find . -type f | sort`
2. Executar `scripts/sync.sh` e confirmar que `~/.hermes/` recebe os arquivos corretos
3. Abrir o Hermes na VPS e testar: `Leia AGENTS.md e me diga quem você é`
