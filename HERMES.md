# HERMES.md — instruções para o Hermes

Este repositório é o BrunoOS — Agent OS pessoal do Bruno — mantido em `/opt/data/AgenteBruno-local` e sincronizado para `/opt/data/` na VPS onde o Hermes roda.

**Regra principal:** a fonte oficial é sempre `/opt/data/AgenteBruno-local`. Tudo em `/opt/data/` é espelho operacional. Ajustes de skills, projetos, memória e identidade devem ser feitos aqui primeiro.

## O que o Hermes deve fazer com este repositório

1. Ler os root files na ordem descrita em `WORKFLOW.md` ao iniciar qualquer sessão.
2. Carregar `projects/*.md` e `knowledge/*.md` sob demanda, conforme a tarefa pedir.
3. Carregar skills de `skills/ideation/{Nome}/README.md` + `workflow.md` sob demanda.
4. Persistir novo estado seguindo a tabela "Onde salvar o quê" em `WORKFLOW.md`.
5. Nunca sobrescrever `GOALS.md`, `PROJECTS.md`, `projects/*.md`, `IDEAS.md` ou `logs/*.md` sem antes ler o conteúdo atual.

## Sincronização

A fonte oficial vive em `/opt/data/AgenteBruno-local` e é sincronizada diariamente para `/opt/data/` via `scripts/update-and-sync.sh`:

```bash
chmod +x scripts/update-and-sync.sh
./scripts/update-and-sync.sh
```

O fluxo copia `SOUL.md` para `/opt/data/SOUL.md`, `USER.md` para `/opt/data/USER.md` e as pastas `projects/`, `knowledge/`, `templates/`, `skills/`, `archive/`, `logs/` e `memories/` para `/opt/data/`, preservando a estrutura.

## Instalação na VPS

1. Clonar/atualizar este repositório em `/opt/data/AgenteBruno-local`.
2. Rodar `scripts/update-and-sync.sh` para atualizar o repositório e popular `/opt/data/`.
3. Testar com um prompt simples: "Leia WORKFLOW.md e me diga quem você é."

## Validação

Antes de sincronizar, rodar:

```bash
python3 scripts/validate-brunos.py
```

Isso confirma que todos os root files obrigatórios existem, que `projects/`, `knowledge/`, `templates/` e `logs/` têm os arquivos base, e que as skills seguem o formato `skills/ideation/{Nome}/{README.md,workflow.md}`.
