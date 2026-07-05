# Ambialles

**Status:** 🟢 Ativo
**Início:** não registrado (workspace Notion com atividade desde pelo menos 06/2026)
**Área:** Negócio / SaaS — gestão de licenciamento ambiental

## Descrição

Empresa de gestão de licenciamentos ambientais. Produto principal em desenvolvimento é uma plataforma SaaS de licenciamento ambiental (MVP em andamento). Opera com um time pequeno: Bruno, Douglas e Wilson.

Fonte da verdade operacional é o Notion ("Ambialles HQ"), não este arquivo — aqui fica só um resumo de navegação. Ver `HERMES.md`/`WORKFLOW.md` para a decisão de manter a automação de calendário/Notion no Hermes (VPS), ainda pendente de configuração de acesso.

## Objetivo

Levar a plataforma de licenciamento ambiental do MVP a cliente pagante recorrente, com o time operando com processos claros (pipeline comercial, jurídico e financeiro já estruturados no Notion).

## Status atual

- **Produto:** MVP da "Plataforma de Licenciamento Ambiental" em desenvolvimento.
- **Comercial:** pipeline ativo — proposta enviada para "Schoeler"; negociação em andamento com uma cooperativa suinícola (apresentação registrada em 03/07); lista de primeiros clientes possíveis em construção.
- **Jurídico:** já existe um modelo de Contrato de Licença de Uso de Software como Serviço.
- **Operação:** estrutura no Notion já cobre Pipeline Comercial, Ações/Projetos (com status, prioridade, responsável, prazo), Financeiro, Decisões Estratégicas, Estratégia & Produto, e uma "CIA — Central de Informações Ambialles" (portal de inteligência com registros do Claude e banco de reuniões).

## Próximos passos

- [ ] Definir se a automação de calendário/Notion da Ambialles roda via Hermes (VPS) — depende de acesso SSH à VPS e configuração de MCP lá (ver `HERMES.md`).
- [ ] Fechar primeiro cliente pagante (cooperativa suinícola / Schoeler).
- [ ] Bruno confirmar se quer que decisões/reuniões da Ambialles sejam espelhadas em `logs/decisions.md` deste repositório ou se ficam só no Notion.

## Métricas / valores

Não consolidadas neste arquivo — acompanhar diretamente nas databases do Notion (Pipeline Comercial, Financeiro).

## Riscos / pontos de atenção

Duas fontes de verdade em paralelo (Notion "Ambialles HQ" vs. `projects/Ambialles.md` neste repo) podem divergir se não houver uma regra clara de qual atualiza qual. Recomendo tratar o Notion como fonte primária de operação do dia a dia e este arquivo como resumo/contexto para o agente.
