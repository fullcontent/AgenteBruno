# SistemaCelic

**Status:** 🟢 Ativo — em produção, desenvolvimento contínuo
**Início:** repositório principal criado em 2019 (`sistemacelic`)
**Área:** Produto / SaaS — gestão de licenciamento/serviços para a Castro Empresarial

## Descrição
SaaS desenvolvido pelo Bruno para a Castro Empresarial. A plataforma é a **definitiva para gestão de licenciamento**: centraliza processos, monitora prazos e garante 100 % de compliance com a tecnologia que as maiores empresas do Brasil já utilizam. O contrato vigente prevê R$ 2.500/mês, com a Castro Empresarial arcando com os custos de API/Gemini e servidores.

## Objetivo
- Centralizar processos de licenciamento e serviços em um único ambiente.
- Monitorar prazos e pendências em tempo real, garantindo conformidade total.
- Fornecer indicadores de desempenho (BI) e visão geográfica da operação.
- Permitir automação de fluxos (ex.: emissão de NF‑e, boletos, atas via IA + n8n).
- Escalar a operação para atender a múltiplas UFs e milhares de clientes com baixo custo operacional.

## Status atual (a partir do GitHub, `sistemacelic`) — **Atualizado em 17/07/2026**
- **50 issues abertas**, 379 fechadas — repositório maduro, ativo desde 2019.
- **Issue criada hoje via chat:** [#468](https://github.com/fullcontent/sistemacelic/issues/468) — Incluir ID da Taxa no relatório (Melhoria, P2, Financeiro)
- **Prioridades abertas:** 11 P1, 10 P2, 10 P3, 2 P4 (14 issues sem label de prioridade, principalmente as mais antigas/recentes fora do backlog formal). Nenhuma issue com label `URGENTE!!!` aberta no momento.
- **Última sprint fechada (17/07/2026 — HOJE):** **7 issues concluídas apenas hoje**:
  - Importação de Extrato (OFX/CSV) e Conciliação Bancária (#467)
  - Relatório de Ordem de Serviço em Excel (#466)
  - Exibir apenas Administradores Ativos na lista (#465)
  - Campo para anexar contrato na OS (#464)
  - Filtros e organizadores na Dashboard de Pendências (#463)
  - Visualização completa do texto em Histórico (#462)
  - Correção: Serviços/IDs no relatório "Listagem Geral" (#461)
- **Sprint anterior (02/07/2026):** 4 issues concluídas — Edição de Interações e Histórico (#448), Clonagem de propostas (#447), Módulo de Atas Estratégicas e Automação de Workflow via IA + n8n (#438), Melhoria UX de notificação (#432).
- **Labels usadas:** Correção, Melhoria, Ajuda, Dúvida, Ajuste Visual, URGENTE!!!, Necessidade, além de prioridade (P1–P4) e área (Operacional, Comercial, Financeiro, Infraestrutura, Interface/UX, Feature, Gestão (IA), Projetos (IA), Projetos).
- **Nenhum PR aberto** no momento.

### Top P1 (11 abertas — maior prioridade)
1. #435 Relatório de Pendências: Filtrar por Status "Ativas"
2. #427 Cadastrar empresa contratada ao cliente
3. #418 Equipe responsável do serviço — vínculo simultâneo de Coordenador/Resp. Técnico/Analista
4. #403 Controle de Múltiplos Protocolos e Laudos
5. #402 Padronização de Menu de Taxas
6. #398 Checklist Empírico (Base Conhecimento) IA
7. #397 Migração de Nuvem (Nativa) — Google Drive API
8. #396 Disparo Automático de Status de Serviço por E‑mail
9. #395 Busca Global Universal (estilo Notion)
10. #394 Resumo de histórico e lançamentos de serviços
11. #393 Integração de Emissão de NF‑e e Boletos via API Banco Inter

### Tema recorrente: automação com IA
Várias issues abertas e fechadas recentemente giram em torno de IA aplicada ao operacional (labels “Gestão (IA)” e “Projetos (IA)”): extração de dados de e‑mails antigos (#439), Dossiê Inteligente com RAG (#437), timeline por frentes (#430), automação de atas via IA + n8n (já fechada, #438), auditoria de serviço via IA (fechada, #440). Vale cruzar com `IDEAS.md` e a esteira `skills/ideation/` caso algum desses vire oportunidade própria fora do sistema.

## Principais funcionalidades & métricas (extraídas do site público)
| Métrica | Valor | Observação |
|---|---|---|
| **Maturidade Digital (Docs)** | **83,6 %** | Indicador de maturidade na gestão documental |
| **Cidades atendidas** | **533** | Municípios brasileiros onde o Sistema Celic está presente |
| **Pendências controladas** | **82,3 mil** | Processos/pendências monitorados |
| **Tempo médio de conclusão** | **83 dias** | Tempo médio desde criação até finalização de processos finalizados |
| **Cobertura nacional** | **28 UFs** (inclui DF) | Presente em praticamente todos os estados brasileiros |
| **Processos geridos ao longo da trajetória** | **12.523** | Volume acumulado de processos atendidos |
| **Licenças & Protocolos ativos** | **8.344** | Licenças e protocolos atualmente vigentes no sistema |
| **Distribuição por tipo de licença** (exemplo) | AVCB: 1.660; Alvará de Funcionamento: 1.427; Licença Ambiental: 927; Alvará Sanitário: 693; Alvará de Publicidade: 553; Matrícula do Imóvel: 456 | Dados do gráfico “Distribuição por Tipo de Licença” |
| **Evolução do volume de processos** (2020‑2026) | 2020:1.422; 2021:2.623; 2022:2.218; 2023:1.663; 2024:1.396; 2025:1.977; 2026*:1.224 | *2026 em processamento, omitido em algumas análises |
| **Evolução da média de dias para conclusão** | 2021:1.395 d; 2022:1.056,5 d; 2023:757,6 d; 2024:337,55 d; 2025:63,6255 d | Queda drástica a partir de 2024 devido à digitalização total e automações Celic |
| **Principais clientes/logos** | Pague Menos (5.607 processos), Adiser BK (Burger King – 1.434), Santander (965), Espaçolaser (721) + diversas outras redes varejistas, instituições financeiras, clínicas de estética etc. | Listado na seção “Quem Confia na Nossa Tecnologia” |

## Métricas / valores (desenvolvimento)
- **Receita mensal confirmada:** R$ 2.500/mês (contrato com Castro Empresarial, que arcando com custos de API/Gemini e servidores).
- **Volume técnico:** 49 issues abertas / 379 fechadas. Desde 01/01/2026: aproximadamente 304 commits (média de ~50 commits/mês). Considerando 2‑4 h por commit, equivalente a **100‑200 h/mês** (25‑50 h/semana).

### Análise de cenários de esforço (baseado em dados do GitHub até 06/07/2026) – Ajustado para uso de Antigravity
| Cenário | Premissa | Cálculo (ajustado Antigravity) | Faixa de horas/mês | Comentário |
|---|---|---|---|---|
| 1. Commit‑only (linhas) | Esforço proporcional às linhas modificadas | 11.937 linhas/mês × (3‑12 h / 1000 linhas) | **36 – 143 h/mês** (9‑36 h/semana) | Redução de 40 % no tempo por 1000 linhas devido ao ganho de produtividade do Antigravity |
| 2. Issue‑closed | Cada issue fechada = pacote de trabalho concluído | 9,2 issues/mês × (2‑9 h / issue) | **18 – 83 h/mês** (5‑21 h/semana) | Tempo por issue reduzido em ~40 % (mais rápido com IA‑assistida) |
| 3. Issue‑aberta (pendente) | Estimativa de esforço ainda a ser gasto nas issues abertas | 49 issues abertas × (2‑9 h) = 98‑441 h total pendente. Distribuído pelos próximos 6 meses: **16 – 74 h/mês** (4‑19 h/semana) | **16 – 74 h/mês** | Mostra carga futura se o backlog for mantido, com ajuste de otimização |
| 4. Misto conservador | Commit (6 h/1000 linhas) + issue fechada (3 h) | (11.937 × 6/1000) + (9,2 × 3) = 71,6 + 27,6 = **99,2 h/mês** | **≈99 h/mês** (25 h/semana) | Ponto médio entre esforço de codificação e fechamento de tarefa, usando fatores otimizados |
| 5. Misto otimista | Commit (9 h/1000 linhas) + issue fechada (5 h) | (11.937 × 9/1000) + (9,2 × 5) = 107,4 + 46 = **153,4 h/mês** | **≈153 h/mês** (38 h/semana) | Pressupõe maior produtividade por linha e menor esforço por issue (mais funcionalidades entregues rapidamente) |
| 6. Pessimista (baixa produtividade) | Commit (4 h/1000 linhas) + issue fechada (2 h) | (11.937 × 4/1000) + (9,2 × 2) = 47,7 + 18,4 = **66,1 h/mês** | **≈66 h/mês** (17 h/semana) | Cenário de muitos retrabalhos, bloqueios ou trabalho não refletido em commits/issues (reuniões, suporte), ainda com benefício do Antigravity |
| 7. Por tipo de label (exemplo) | Distribuição de labels (ex: 30 % Ajuda, 20 % Ajuste Visual, 20 % Gestão (IA), 30 % outras) | Exemplo: 2 h para “Ajuda”, 3 h para “Ajuste Visual”, 5 h para “Gestão (IA)”, 4 h para demais → ~32 h/mês de issues fechadas + 71,6 h/mês de commits = **~104 h/mês** | **~104 h/mês** | Requer extração de distribuição de labels via API; útil para ajustar conforme tipo de trabalho predominante |

**Observações sobre a precisão das estimativas**
- Os valores são projeções; o esforço real por commit ou issue varia muito, mas o uso de Antigravity tende a reduzir o tempo gasto em tarefas repetitivas e de boilerplate.
- Trabalho não refletido em commits (reuniões, documentação, suporte ao cliente, ajustes de servidor) não é capturado.
- O volume de commits pode ser inflacionado por commits pequenos (formatação, CI) ou deflatado por grandes mudanças em poucos commits.
- Para aprimorar, seria ideal ter dados de *time tracking* ou usar a API de pull requests (adicionar linhas adicionadas/removidas) como proxy de tamanho.

**Próximos passos sugeridos para refinamento**
1. Exportar lista de commits com estatísticas (adições/deleções) via GitHub API e aplicar peso maior a commits com muitas linhas modificadas, considerando o fator de produtividade do Antigravity.
2. Classificar issues fechadas por label (ex.: “Ajuda”, “Gestão (IA)”, “Feature”) e atribuir esforço médio diferente a cada categoria, ajustado para o ganho de eficiência.
3. Comparar com o tempo gasto relatado em ferramentas de gestão (se houver) para validar os modelos.
4. Revisar mensalmente e atualizar a seção de métricas com os valores reais observados.

## Sugestões de reajuste da mensalidade (baseado no cenário misto conservador ≈ 99 h/mês)
| Opção | Descrição | Taxa hora‑valor (R$/h) | Mensalidade estimada (R$) | Comentário |
|---|---|---|---|---|
| 1 – Manter atual | Valor atual do contrato | 25,25 | 2.500 | Mantém o mesmo patamar; útil se o orçamento for rígido. |
| 2 – Valor intermediário baixo | Aproxima‑se do piso para desenvolvedor pleno | 40,00 | 3.960 (~4.000) | Reconhece parte da eficiência ganha com Antigravity. |
| 3 – Valor intermediário médio | Alinha‑se a profissional experiente (pleno/sênior) | 60,00 | 5.940 (~6.000) | Considera trabalho de operação e monitoramento além do desenvolvimento puro. |
| 4 – Valor de mercado elevado + retainer de disponibilidade | Inclui adicional por responsabilidade de servidor/backups e disponibilidade para issue travada | 80,00 + 20 % retainer | ~9.500 | Reflete valor de mercado e a responsabilidade de operação contínua. |
| 5 – Valor premium + retainer maior | Para especialista que garante disponibilidade e pode assumir melhorias estratégicas | 100,00 + 30 % retainer | ~12.900 | Indicado se quiser ser remunerado como especialista com alto nível de serviço. |
| 6 – Modelo híbrido (retainer fixo + variável) | Separa claramente pagamento por prontidão e por esforço de desenvolvimento | Retainer fixo 1.500 + 50 h × 50 h = 4.950 | ~6.450 | Transparente: paga‑se pela disponibilidade e pelas horas efetivas de trabalho. |

*Observação:* As horas base (≈ 99 h/mês) vêm do cenário “Misto Conservador” ajustado para uso de Antigravity. Caso o volume de issues mude ou a questão da NF‑e seja desbloqueada, reavalie a carga horária e ajuste a mensalidade conforme necessário.

## Riscos / pontos de atenção
- **Backlog de P1 relativamente grande** (11 itens) parado desde março/2026 sem movimento aparente até a leva fechada em 02/07/2026 – pode indicar gargalo de execução.
- **Dois repositórios paralelos** (`sistemacelicV2`, `celic-visionary-canvas`) sem atividade há meses – risco de esforço duplicado ou decisão arquitetural pendente (migrar vs. manter o `sistemacelic` atual).
- Dependência de APIs externas (Gemini, Google Drive) e custos de servidor arcados pela Castro Empresarial – monitorar custos e SLAs.
- Necessidade de documentação atualizada das novas funcionalidades de BI, mapa e ranking de clientes para facilitar onboarding e suporte.

## Próximos passos (ação imediata)
1. Atualizar este arquivo (`SistemaCelic.md`) com as informações acima (feito).
2. Solicitar ao Bruno a descrição oficial de negócio (caso ainda não tenha sido enviada) para preencher a seção “Objetivo” com maior detalhe.
3. Revisar o backlog de P1 e definir uma sprint focada nas issues de maior impacto (ex.: #435, #427, #403).
4. Avaliar o status dos repositórios `sistemacelicV2` e `celic-visionary-canvas` para decidir arquivamento, merge ou continuação.
5. Implementar atualizações de documentação interna (README, wiki) refletindo as novas métricas e funcionalidades divulgadas no site.

---
*Última atualização: 2025‑08‑27 (com base nos dados extraídos de http://sistemacelic.com/apresentacao e no estado do repositório `sistemacelic` em 06/07/2026).*