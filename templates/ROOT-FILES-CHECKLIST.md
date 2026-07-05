# templates/ROOT-FILES-CHECKLIST.md

Checklist para validar que os root files do Agent OS estão completos e coerentes. Usar ao revisar a estrutura ou antes de sincronizar com o Hermes.

## Presença

- [ ] `AGENTS.md` existe e define ordem de leitura, roteamento de skills e política de aprovação
- [ ] `SOUL.md` existe e define identidade, tom e princípios de raciocínio
- [ ] `USER.md` existe e está atualizado com o perfil atual
- [ ] `GOALS.md` existe e reflete os objetivos vigentes (revisar mensalmente)
- [ ] `MAPA.md` existe e referencia todas as pastas atuais do repositório
- [ ] `MEMORY.md` existe e não contém informação contraditória com `memory/*.md`
- [ ] `TOOLS.md` existe e lista as ferramentas realmente disponíveis
- [ ] `PROPAGATION.md` existe e cobre todos os tipos de conteúdo gerados nas sessões
- [ ] `HERMES.md` existe e as instruções de sincronização batem com `scripts/sync.sh`
- [ ] `agent-os.yaml` existe e está sincronizado com a estrutura real de pastas/arquivos
- [ ] `README.md` está atualizado e reflete a estrutura atual

## Coerência

- [ ] Nenhum root file duplica conteúdo de outro sem necessidade
- [ ] Toda skill em `skills/` segue o formato `skills/{categoria}/{nome}/SKILL.md`
- [ ] Toda skill tem frontmatter `name` e `description`
- [ ] `memory/` tem os 4 arquivos base (`decisions.md`, `ideas.md`, `lessons.md`, `tasks.md`)
- [ ] `.gitignore` exclui artefatos locais (`.hermes/` local, `reports/` gerados, `.env`)

## Sincronização

- [ ] `scripts/validate-agent-os.py` roda sem erros
- [ ] `scripts/sync.sh` copia root files, `skills/` e `memory/` para `~/.hermes/`
- [ ] Teste manual no Hermes: "Leia AGENTS.md e me diga quem você é" retorna resposta coerente com `SOUL.md`
