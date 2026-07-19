# Ambialles

**Status:** 🟢 Ativo
**Área:** Negócio / SaaS — gestão de licenciamento ambiental
**Última sincronização:** 2026-07-18 11:01 UTC
**Fontes:** Notion público (Estratégia & Produto, Desenvolvimento)

---

## ℹ️ Sobre

Empresa de gestão de licenciamentos ambientais. Produto principal: plataforma SaaS de licenciamento ambiental (MVP em andamento). Time: Bruno, Douglas e Wilson.

**Repositório GitHub:** [fullcontent/ambialles](https://github.com/fullcontent/ambialles)
**Workspace local:** `/opt/data/workspaces/ambialles`

---

## 📋 Infra & Tech Stack

- **Stack:** Laravel + Blade + Alpine.js + Tailwind + Vite + Pest
- **Branch principal:** `main`
- **Documentação:** `README.md`, `CLAUDE.md`, `docs/`

---

## 📄 Estratégia & Produto

# Estratégia & Produto — Ambialles
Documento vivo da estratégia da Ambialles. Revisitar a cada ciclo de 90 dias ou após grandes decisões.
---
## 🌟 Visão
> Ser a principal plataforma brasileira de gestão inteligente de licenciamento ambiental para empresas do agronegócio, começando pela suinocultura e evoluindo para outros setores que precisam controlar licenças, documentos, prazos, condicionantes e obrigações ambientais com mais segurança, organização e previsibilidade.

---
## 🎯 Missão
> A missão da Ambialles é simplificar e profissionalizar a gestão do licenciamento ambiental por meio de tecnologia, organização de dados e inteligência artificial, ajudando empresas do agronegócio a controlar licenças, documentos, prazos e obrigações ambientais com mais segurança jurídica, previsibilidade e otimizando os recursos humanos.

---
## 💎 Valores
* Simplicidade — Tecnologia complexa, experiência simples.
* Confiança — O cliente confia seus dados e processos a nós. Segurança é inegociável.
* Responsabilidade técnica — A IA apoia. O humano decide. Sempre.
* Velocidade com qualidade — Entregar rápido, mas sem comprometer o que é crítico.
* Parceria real — Não somos fornecedores. Somos parceiros do sucesso do cliente.
---
## 🏆 Proposta de Valor / Definir proposta de valor da Ambialles
Para produtores rurais (e consultores ambientais) que perdem prazos, documentos e controle sobre licenças ambientais, a Ambialles é uma plataforma SaaS que centraliza toda a gestão de licenciamento em um único dashboard com alertas de vencimento, controle documental (e execução assistida por IA). Diferente de planilhas e e-mails, a Ambialles garante visibilidade total e reduz o risco de autuações.
Garantir que a operação do cliente nunca pare por questões ambientais
---
## 🗺️ Posicionamento
[table_row] Consultoria TradicionalPlanilha/EmailAmbialles
[table_row] ❌❌Visão centralizada✅
[table_row] ❌❌Alertas automáticos✅
[table_row] ✅❌Execução do licenciamento✅
[table_row] ❌❌Escalável para muitas unidades✅
[table_row] ❌✅Custo acessível✅
---
## 📦 Produto — Escopo do MVP
### Funcionalidades obrigatórias (Fase 1)
- [ ] Login e controle de acesso por perfilYes
- [ ] Dashboard com visão geral das licençasYes
- [ ] Cadastro de clientes e unidades/propriedadesYes
- [ ] Cadastro e gestão de processos de licenciamentoNo
- [ ] Status do processo (Em levantamento → Protocolado → Aprovado → Renovação próxima → Vencido)No
- [ ] Armazenamento de documentosYes
- [ ] Controle de vencimentos com alertasNo
- [ ] Geração de relatórios simplesNo
- [ ] Perfis de acesso diferenciados (admin, consultor, cliente)Yes
### Funcionalidades futuras + Venda da 2º Proposta de valor (pós-piloto)
- [ ] IA para leitura e checklist de documentosNo
- [ ] Vender a proposta de licença ambiental
- [ ] Integração com órgãos ambientaisNo
- [ ] App mobileNo
- [ ] API para integração com sistemas do clienteNo
- [ ] Módulo de condicionantes e auditoriasNo
- [ ] Cadastro automatico via PDF da licença.
---
## 📊 OKRs — Ciclo 90 dias (Jun → Set 2026)
### Objetivo 1: Validar o produto com o primeiro cliente real
* KR1: Fechar contrato de piloto com Schoeler até 30/jun/2026
* KR2: MVP com as 9 funcionalidades obrigatórias funcionando até 10/jul/2026
* KR3: Schoeler usando o sistema com pelo menos 10 unidades cadastradas até 31/jul/2026
* KR4: NPS do cliente piloto ≥ 8 ao final do ciclo
### Objetivo 2: Descobrir a capacidade operacional real
* KR1: Executar 3–5 licenciamentos reais nas primeiras 6 semanas
* KR2: Escalar para 8–12 licenciamentos/mês até semana 10
* KR3: Documentar processo completo da Mireylle (passo a passo, checklists, padrões)
* KR4: Definir capacidade máxima de 1 analista em licenças/mês
### Objetivo 3: Construir base para escala comercial
* KR1: Criar case documentado da Schoeler (antes/depois) até 31/set/2026
* KR2: Ter lista de 10–20 leads qualificados prontos para abordagem
* KR3: Proposta comercial padrão criada e validada
* KR4: Modelo financeiro validado (margem, esforço, preço confirmados)
### Objetivo 4: Estruturar a empresa
* KR1: Valuation pré-investimento definido 
* KR2: CNPJ/empresa constituída até 31/ago/2026
* KR3: Todos os sócios com tarefas documentadas e acompanhadas semanalmente no Notion
---
## 🗓️ Roadmap
### Fase 1 — Fechar o Piloto (Semanas 1–3)
Objetivo: Transformar o interesse da Schoeler em contrato fechado
* Criar proposta comercial (Wilson)
* ‣ 
* Conduzir reunião de fechamento (Douglas + Wilson)
* Desenvolvimento do software (MVP) — direto ao ponto:
* Login + perfis (admin/consultor/cliente)
* Cadastros base (clientes, unidades/propriedades, processos)
* Documentos (upload/organização) + prazos/alertas
* Status do processo + dashboard
* Relatórios simples
* Publicação em produção (backup + logs básicos)
### Fase 2 — MVP Real (Operação com dados reais) (Semanas 4–6)
Objetivo: Colocar sistema + operação funcionando com dados reais (pilotando na Schoeler)
* Mapear 184 unidades da Schoeler
* Cadastrar unidades/processos prioritários no sistema
* Iniciar execução com 3–5 licenças reais (Mireylle)
* Ajustes rápidos no fluxo do software conforme uso
### Fase 3 — Teste de Capacidade (Semanas 7–10)
Objetivo: Descobrir o limite real da operação e endurecer o produto
* Escalar de 3–5 para 8–12 licenças/mês
* Medir tempo por licença e gargalos (Mireylle)
* Documentar processo completo
* Ajustar sistema com base no uso real (Bruno)
### Fase 4 — Consolidação e Escala (Semanas 11–12)
Objetivo: Transformar em modelo replicável
* Criar case real da Schoeler
* Validar margem, esforço e preço
* Preparar lista de 10–20 próximos leads
* Proposta padrão pronta para replicação
---
## 💰 Modelo de Precificação (em validação, falar sobre contratos)
> ⚠️ Decisão pendente: Definir o modelo definitivo antes da reunião com Schoeler.

---
## 🧭 Norte Estratégico
> "Não somos uma consultoria ambiental com um site. Somos uma empresa de tecnologia que executa licenciamento. O software escala. A operação valida. O case vende."



---

## 📋 Desenvolvimento — Database de Tarefas


**Total: 38 registros**


* **Aceitar tipos de renovação (RLAC/RLAS/RLO/LOR) no cadastro de Licença** · [📋 Backlog] · (🎯 High) · 👤 Bruno · 📅 2026-07-15
  └ Category: Bug Fix

* **Upload de PDF no cadastro inicial — leitura automática com parser local** · [📋 Backlog] · (🎯 High) · 👤 Bruno · 📅 2026-07-25
  └ Category: New Feature

* **Leitura de PDF por IA multi-provedor (fallback configurável)** · [📋 Backlog] · (🎯 Medium) · 👤 Bruno · 📅 2026-08-15
  └ Category: New Feature

* **Vincular conclusão do Processo de renovação à Licença (registrar/atualizar automaticamente)** · [📋 Backlog] · (🎯 High) · 👤 Bruno · 📅 2026-07-21
  └ Category: New Feature

* **Busca avançada com filtros salvos** · [📋 Backlog] · (🎯 Medium) · 📅 2026-09-15
  └ Category: Enhancement

* **Relatórios de conformidade — histórico de 4 anos** · [📋 Backlog] · (🎯 Medium) · 📅 2026-10-01
  └ Category: Enhancement

* **Definir modelo de precificação — por produtor, usuário ou licença** · [📋 Backlog] · (🎯 High) · 📅 2026-07-15
  └ Category: New Feature

* **Versionamento de documentos — histórico e auditoria** · [📋 Backlog] · (🎯 High) · 📅 2026-08-15
  └ Category: Enhancement

* **Pré-preenchimento com dados históricos em renovações** · [📋 Backlog] · (🎯 High) · 📅 2026-08-15
  └ Category: Enhancement

* **Direcionamento de tarefas entre usuários — bate-bola** · [📋 Backlog] · (🎯 High) · 📅 2026-09-01
  └ Category: Enhancement

* **Campos customizáveis para condicionantes ambientais** · [📋 Backlog] · (🎯 High) · 📅 2026-08-15
  └ Category: Enhancement

* **Opção de deploy on-premise — não apenas SaaS** · [📋 Backlog] · (🎯 High) · 📅 2026-09-01
  └ Category: New Feature

* **Integração com Sigma — rastreabilidade agrícola** · [📋 Backlog] · (🎯 High) · 📅 2026-09-01
  └ Category: New Feature

* **Alertas multicanal — WhatsApp, Telegram e notificações push** · [📋 Backlog] · (🎯 High) · 📅 2026-08-01
  └ Category: New Feature

* **Mock de consulta governamental + logs_consultas_governo** · [✅ Completed] · (🎯 Medium) · 📅 2026-06-17
  └ Category: New Feature

* **CRUD completo — Clientes, Produtores, Empreendimentos, Licenças** · [✅ Completed] · (🎯 High) · 📅 2026-06-17
  └ Category: New Feature

* **Autenticação, RBAC e aprovação de usuários** · [✅ Completed] · (🎯 High) · 📅 2026-06-17
  └ Category: New Feature

* **Sub-módulos de licença — água utilizada, condicionantes, efluentes, resíduos, checklist** · [✅ Completed] · (🎯 High) · 📅 2026-06-19
  └ Category: New Feature

* **Scraper IAT + cross-check com banco de dados** · [🔄 In progress] · (🎯 High) · 📅 2026-06-28
  └ Category: New Feature

* **Modelagem base — clientes, produtores, empreendimentos, licenças, documentos** · [✅ Completed] · (🎯 High) · 📅 2026-06-08
  └ Category: New Feature

* **Consulta CAR via InfoSimples + conversão UTM → WGS84** · [📋 Planned] · (🎯 Medium) · 📅 2026-06-28
  └ Category: New Feature

* **Dashboard com status de licenças e indicadores** · [✅ Completed] · (🎯 Medium) · 📅 2026-06-16
  └ Category: New Feature

* **Gestão de pendências de processo com alertas no dashboard** · [✅ Completed] · (🎯 High) · 📅 2026-06-17
  └ Category: New Feature

* **Sistema de processos com Kanban (etapas, drag-and-drop)** · [✅ Completed] · (🎯 High) · 📅 2026-06-17
  └ Category: New Feature

* **Cofre documental — upload, validação e rejeição de documentos** · [✅ Completed] · (🎯 High) · 📅 2026-06-17
  └ Category: New Feature

* **Persistência do CAR no Empreendimento** · [📋 Planned] · (🎯 High) · 📅 2026-07-21
  └ Category: New Feature

* **Importação em lote via PDF (Schoeler Suínos)** · [🔄 In progress] · (🎯 High) · 📅 2026-06-28
  └ Category: New Feature

* **Relatórios básicos em PDF (/relatorios)** · [📋 Backlog] · (🎯 Medium) · 📅 2026-08-15
  └ Category: New Feature

* **Painel histórico IAT (deferidas, indeferidas, requeridas)** · [🔄 In progress] · (🎯 Medium) · 📅 2026-06-28
  └ Category: New Feature

* **Monitoramento Ambiental — laudos de solo e aplicações de dejeto (IN 61/2020)** · [📋 Backlog] · (🎯 Low) · 📅 2026-11-01
  └ Category: New Feature

* **CRUD manual sub-tabelas da Licença (água, efluentes, resíduos, condicionantes, taxas)** · [📋 Planned] · (🎯 High) · 📅 2026-07-01
  └ Category: New Feature

* **Painel de Prazos (/prazos)** · [📋 Planned] · (🎯 High) · 📅 2026-06-29
  └ Category: New Feature

* **Validações cadastrais — Receita Federal, Correios, IBGE** · [📋 Backlog] · (🎯 Low) · 📅 2026-09-01
  └ Category: Enhancement

* **Expansão modelo Outorga — dados hidrológicos completos (DUIO)** · [📋 Planned] · (🎯 Low) · 📅 2026-07-07
  └ Category: New Feature

* **Notificações por email — alertas de vencimento** · [📋 Backlog] · (🎯 Medium) · 📅 2026-08-01
  └ Category: New Feature

* **Interface de listagens melhorada (licenças, empreendimentos, produtor)** · [🔄 In progress] · (🎯 Low) · 📅 2026-06-28
  └ Category: UI/UX

* **Integrações reais com IBAMA, CAR e INCRA** · [📋 Backlog] · (🎯 Medium) · 📅 2026-10-01
  └ Category: New Feature

* **Fluxo de Trabalho para gerar licencas** · [📋 Planned] · 👤 Bruno

---

## ⚙️ Automação

Este arquivo é atualizado automaticamente 1x/dia via script de coleta do Notion.
Última coleta: 2026-07-18 11:01 UTC

*Fontes: [Notion Público Ambialles](https://trapezoidal-aragon-9fc.notion.site)*
