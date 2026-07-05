# HERMES.md — instruções para o Hermes

Este repositório é o BrunoOS — Agent OS pessoal do Bruno — sincronizado para `~/.hermes/` na VPS onde o Hermes roda via Docker.

## O que o Hermes deve fazer com este repositório

1. Ler os root files na ordem descrita em `WORKFLOW.md` ao iniciar qualquer sessão.
2. Carregar `projects/*.md` e `knowledge/*.md` sob demanda, conforme a tarefa pedir.
3. Carregar skills de `skills/ideation/{Nome}/README.md` + `workflow.md` sob demanda.
4. Persistir novo estado seguindo a tabela "Onde salvar o quê" em `WORKFLOW.md`.
5. Nunca sobrescrever `GOALS.md`, `PROJECTS.md`, `projects/*.md`, `IDEAS.md` ou `logs/*.md` sem antes ler o conteúdo atual.

## Sincronização

Este repositório vive em `~/Desktop/AgenteBruno` (ou equivalente) e é sincronizado para `~/.hermes/` via `scripts/sync.sh`:

```bash
chmod +x scripts/sync.sh
./scripts/sync.sh
```

O script copia os root files e as pastas `projects/`, `knowledge/`, `templates/`, `skills/`, `archive/`, `logs/` para `~/.hermes/`, preservando a estrutura.

## Instalação na VPS

1. Clonar/atualizar este repositório na VPS onde o Hermes roda em Docker.
2. Rodar `scripts/sync.sh` para popular `~/.hermes/`.
3. Confirmar montagem do volume `~/.hermes/` no container do Hermes.
4. Testar com um prompt simples: "Leia WORKFLOW.md e me diga quem você é."

## Validação

Antes de sincronizar, rodar:

```bash
python3 scripts/validate-brunos.py
```

Isso confirma que todos os root files obrigatórios existem, que `projects/`, `knowledge/`, `templates/` e `logs/` têm os arquivos base, e que as skills seguem o formato `skills/ideation/{Nome}/{README.md,workflow.md}`.
