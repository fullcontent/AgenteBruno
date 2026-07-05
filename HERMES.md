# HERMES.md — instruções para o Hermes

Este repositório é o BrunoOS — Agent OS pessoal do Bruno — mantido em `/opt/data/AgenteBruno` e sincronizado para `~/.hermes/` na VPS onde o Hermes roda.

## O que o Hermes deve fazer com este repositório

1. Ler os root files na ordem descrita em `WORKFLOW.md` ao iniciar qualquer sessão.
2. Carregar `projects/*.md` e `knowledge/*.md` sob demanda, conforme a tarefa pedir.
3. Carregar skills de `skills/ideation/{Nome}/README.md` + `workflow.md` sob demanda.
4. Persistir novo estado seguindo a tabela "Onde salvar o quê" em `WORKFLOW.md`.
5. Nunca sobrescrever `GOALS.md`, `PROJECTS.md`, `projects/*.md`, `IDEAS.md` ou `logs/*.md` sem antes ler o conteúdo atual.

## Sincronização

A fonte oficial vive em `/opt/data/AgenteBruno` e é sincronizada diariamente para `~/.hermes/` via `scripts/update-and-sync.sh`:

```bash
chmod +x scripts/update-and-sync.sh
./scripts/update-and-sync.sh
```

O fluxo copia `SOUL.md` para `~/.hermes/SOUL.md`, `USER.md` para `~/.hermes/memories/USER.md` e as pastas `projects/`, `knowledge/`, `templates/`, `skills/`, `archive/`, `logs/` e `memories/` para `~/.hermes/`, preservando a estrutura.

## Instalação na VPS

1. Clonar/atualizar este repositório em `/opt/data/AgenteBruno`.
2. Rodar `scripts/update-and-sync.sh` para atualizar o repositório e popular `~/.hermes/`.
3. Testar com um prompt simples: "Leia WORKFLOW.md e me diga quem você é."

## Validação

Antes de sincronizar, rodar:

```bash
python3 scripts/validate-brunos.py
```

Isso confirma que todos os root files obrigatórios existem, que `projects/`, `knowledge/`, `templates/` e `logs/` têm os arquivos base, e que as skills seguem o formato `skills/ideation/{Nome}/{README.md,workflow.md}`.
