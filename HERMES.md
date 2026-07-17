# HERMES.md — instruções para o Hermes

Este repositório é o BrunoOS — Agent OS pessoal do Bruno — mantido em `/opt/data/AgenteBruno-local` e sincronizado para `/opt/data/` na VPS onde o Hermes roda.

**Regra principal:** a fonte oficial é sempre `/opt/data/AgenteBruno-local`. Tudo em `/opt/data/` é espelho operacional. Ajustes de skills, projetos, memória e identidade devem ser feitos aqui primeiro.

## Arquitetura de Tópicos no Telegram (Mapeamento Obrigatório)

Para que o orquestramento funcione no ecossistema Telegram (Supergrupo BrunoHQ), o Hermes DEVE manter um mapeamento permanente de IDs de tópicos. Quando uma skill ou rotina finalizar, o resultado deve ser roteado usando este ID:

- `#comando` -> `[ID_DO_TOPICO]`
- `#operacoes` -> `[ID_DO_TOPICO]`
- `#comunicacao` -> `[ID_DO_TOPICO]`
- `#tecnologia-produto` -> `[ID_DO_TOPICO]`
- `#estudio-criativo` -> `[ID_DO_TOPICO]`
- `#crescimento-financas` -> `[ID_DO_TOPICO]`
- `#saude-vitalidade` -> `[ID_DO_TOPICO]`
- `#pesquisa-radar` -> `[ID_DO_TOPICO]`
- `#resumo-diario` -> `[ID_DO_TOPICO]`

Consulte `WORKFLOW_ROUTING.md` para entender qual especialista é o dono de qual tópico e as regras de Slash Commands associadas a eles.

## O que o Hermes deve fazer com este repositório

1. Ler os root files na ordem descrita em `WORKFLOW.md` ao iniciar qualquer sessão, somado ao `WORKFLOW_ROUTING.md`.
2. Carregar `projects/*.md` e `knowledge/*.md` sob demanda, conforme a tarefa pedir.
3. Carregar skills operacionais e de rotina de `skills/routines/`, `skills/operations/`, `skills/comms/`, e `skills/health/` sob demanda.
4. Aplicar regras de formatação móvel de `HOUSE_STYLE.md` em toda e qualquer resposta operacional.
5. Persistir novo estado seguindo a tabela "Onde salvar o quê" em `WORKFLOW.md`.
6. Nunca sobrescrever `GOALS.md`, `PROJECTS.md`, `projects/*.md`, `IDEAS.md` ou `logs/*.md` sem antes ler o conteúdo atual.

## Sincronização

A fonte oficial vive em `/opt/data/AgenteBruno-local` e é sincronizada diariamente para `/opt/data/` via `scripts/update-and-sync.sh`:

```bash
chmod +x scripts/update-and-sync.sh
./scripts/update-and-sync.sh
```

O fluxo copia `SOUL.md` para `/opt/data/SOUL.md`, `USER.md` para `/opt/data/USER.md`, mapeamentos `WORKFLOW_ROUTING.md` e `HOUSE_STYLE.md`, e as pastas de estrutura para `/opt/data/`, preservando a estrutura.

## Instalação na VPS

1. Clonar/atualizar este repositório em `/opt/data/AgenteBruno-local`.
2. Rodar `scripts/update-and-sync.sh` para atualizar o repositório e popular `/opt/data/`.
3. Rodar a lista de prompts contida em `hermes-personal-assistant-all-prompts.md` no chat do Hermes no Telegram para efetuar o bootstrapping do ecossistema.
4. Testar com um prompt simples: "Leia WORKFLOW.md e me diga quem você é."

## Validação

Antes de sincronizar, rodar:

```bash
python3 scripts/validate-brunos.py
```

Isso confirma que todos os root files obrigatórios existem e que as novas áreas e skills foram mapeadas corretamente.
