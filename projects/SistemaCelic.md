# SistemaCelic

**Status:** 🟢 Ativo — em produção, desenvolvimento contínuo
**Início:** repositório principal criado em 2019 (`sistemacelic`)
**Área:** Produto / SaaS — gestão de licenciamento/serviços para a Castro Empresarial

## Descrição

SaaS desenvolvido pelo Bruno para a Castro Empresarial. Ainda sem a descrição de negócio detalhada (Bruno vai enviar) — o que segue é o que dá pra observar direto do GitHub.

**Repositórios relacionados (`github.com/fullcontent`):**

| Repo | Stack | Status |
|---|---|---|
| [`sistemacelic`](https://github.com/fullcontent/sistemacelic) | Laravel (PHP + Blade) | 🟢 Principal, em produção — último push 2026-07-02 |
| [`sistemacelicV2`](https://github.com/fullcontent/sistemacelicV2) | PHP | 🟡 Parado desde 2026-03-10 — provável tentativa de reescrita/V2 |
| [`celic-visionary-canvas`](https://github.com/fullcontent/celic-visionary-canvas) | TypeScript (privado) | 🟡 Parado desde 2026-04-08 — parece protótipo de UI (nome sugere geração via Lovable/v0) |

## Objetivo

Pendente — preencher quando a descrição de negócio chegar do Bruno.

## Status atual (a partir do GitHub, `sistemacelic`)

- **49 issues abertas**, 379 fechadas — repositório maduro, ativo desde 2019.
- **Prioridades abertas:** 11 P1, 10 P2, 10 P3, 2 P4 (14 issues sem label de prioridade, principalmente as mais antigas/recentes fora do backlog formal). Nenhuma issue com label `URGENTE!!!` aberta no momento.
- **Última sprint fechada (02/07/2026):** 4 issues concluídas no mesmo dia — Edição de Interações e Histórico (#448), Clonagem de propostas (#447), Módulo de Atas Estratégicas e Automação de Workflow via IA + n8n (#438), Melhoria UX de notificação (#432).
- **Labels usadas para categorizar:** Correção, Melhoria, Ajuda, Dúvida, Ajuste Visual, URGENTE!!!, Necessidade, além de prioridade (P1–P4) e área (Operacional, Comercial, Financeiro, Infraestrutura, Interface/UX, Feature, Gestão (IA), Projetos (IA), Projetos).
- **Nenhum PR aberto** no momento.

### Top P1 (11 abertas — maior prioridade)

- #435 Relatório de Pendências: Filtrar por Status "Ativas"
- #427 Cadastrar empresa contratada ao cliente
- #418 Equipe responsável do serviço — vínculo simultâneo de Coordenador/Resp. Técnico/Analista
- #403 Controle de Múltiplos Protocolos e Laudos
- #402 Padronização de Menu de Taxas
- #398 Checklist Empírico (Base Conhecimento) IA
- #397 Migração de Nuvem (Nativa) — Google Drive API
- #396 Disparo Automático de Status de Serviço por E-mail
- #395 Busca Global Universal (estilo Notion)
- #394 Resumo de histórico e lançamentos de serviços
- #393 Integração de Emissão de NF-e e Boletos via API Banco Inter

### Um forte tema recorrente: automação com IA

Várias issues abertas e fechadas recentemente giram em torno de IA aplicada ao operacional (label "Gestão (IA)" e "Projetos (IA)"): extração de dados de emails antigos (#439), Dossiê Inteligente com RAG (#437), Timeline por frentes (#430), automação de atas via IA+n8n (já fechada, #438), auditoria de serviço via IA (fechada, #440). Vale cruzar com `IDEAS.md` e a esteira `skills/ideation/` se algum desses virar oportunidade própria fora do sistema.

## Próximos passos

- [ ] Bruno enviar a descrição de negócio do projeto (o que o sistema faz, para quem, modelo de receita com a Castro Empresarial).
- [ ] Confirmar se `sistemacelicV2` e `celic-visionary-canvas` são iniciativas ativas ou exploratórias abandonadas.
- [ ] Decidir se as 11 issues P1 abertas representam o backlog prioritário atual ou se precisa de nova triagem.

## Métricas / valores

Pendente — não há dado de receita/contrato neste repositório GitHub, só volume de trabalho técnico (49 abertas / 379 fechadas).

## Riscos / pontos de atenção

- Backlog de P1 relativamente grande (11 itens) parado desde março/2026 sem movimento aparente até a leva fechada em 02/07 — pode indicar gargalo de execução.
- Dois repositórios paralelos (`sistemacelicV2`, `celic-visionary-canvas`) sem atividade há meses — risco de esforço duplicado ou decisão arquitetural pendente (migrar vs. manter o `sistemacelic` atual).
