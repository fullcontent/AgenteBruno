# HERMES.md — instruções para o Hermes

Este repositório é o Agent OS do Bruno, no formato esperado pelo framework [agent-os-hermes](https://github.com/okjpg/agent-os-hermes), rodando via Docker na VPS.

## O que o Hermes deve fazer com este repositório

1. Ler os root files na ordem descrita em `AGENTS.md` ao iniciar qualquer sessão.
2. Carregar skills de `skills/**/SKILL.md` sob demanda, conforme a tarefa pedir.
3. Persistir novo estado em `memory/` seguindo `PROPAGATION.md`.
4. Nunca sobrescrever `MEMORY.md`, `memory/*.md` ou `GOALS.md` sem antes ler o conteúdo atual.

## Sincronização

Este repositório vive em `~/Desktop/AgenteBruno` (ou equivalente) e é sincronizado para `~/.hermes/` via `scripts/sync.sh`:

```bash
chmod +x scripts/sync.sh
./scripts/sync.sh
```

O script copia:
- Root files → `~/.hermes/context/`
- `skills/` → `~/.hermes/skills/` (recursivo, preserva estrutura de pastas)
- `memory/` → `~/.hermes/memory/`

## Instalação na VPS

1. Clonar/atualizar este repositório na VPS onde o Hermes roda em Docker.
2. Rodar `scripts/sync.sh` para popular `~/.hermes/`.
3. Confirmar montagem do volume `~/.hermes/` no container do Hermes (ver docker-compose do agent-os-hermes).
4. Testar com um prompt simples: "Leia AGENTS.md e me diga quem você é."

## Validação

Antes de sincronizar, rodar:

```bash
python3 scripts/validate-agent-os.py
```

Isso confirma que todos os root files obrigatórios existem e que as skills seguem o formato `skills/{categoria}/{nome}/SKILL.md`.
