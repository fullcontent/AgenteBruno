# WORKFLOW.md — contrato operacional

Este arquivo é o bootloader: diz como ler o workspace, quando usar skills, como executar, e onde salvar o que precisa sobreviver à sessão.

## Ordem de leitura no início da sessão

1. `README.md` — visão geral do repositório.
2. `USER.md` — perfil do Bruno.
3. `GOALS.md` — objetivos de curto/médio/longo prazo.
4. `NOW.md` — o que está em foco agora.
5. `THINKING.md` / `WRITING_STYLE.md` — como pensar e responder.
6. `DECISION_RULES.md` — critérios de decisão.
7. `PROJECTS.md` e `projects/*.md` relevantes, conforme a tarefa.
8. `knowledge/*.md` e `skills/**/README.md`, sob demanda.

Não carregue o repositório inteiro por reflexo. Root files são roteadores; `projects/`, `knowledge/`, `skills/` entram sob demanda.

## Princípio central

> Prompt é interface.
> Skill é processo.
> Memória é continuidade.
> Ferramenta é execução.
> Verificação é confiança.

---

## Como decidir o que fazer

Ao receber uma tarefa:

1. Identifique o pedido real, não só o literal.
2. Verifique se existe skill compatível em `skills/`.
3. Se existir, carregue a skill e siga o procedimento (`README.md` + `workflow.md` da skill).
4. Se não existir e a tarefa for recorrente, proponha criar uma skill nova (ver `templates/Skill.md`).
5. Execute com ferramentas quando houver arquivo, código, Git, web, API ou validação envolvida.
6. Verifique o resultado com evidência real.
7. Salve o que precisa sobreviver à sessão (ver "Onde salvar o quê" abaixo).

---

## Esteira de validação de ideias

Sempre que o Bruno trouxer uma nova ideia ou oportunidade de negócio, acione a skill `skills/ideation/ValidateNewIdea/`, que orquestra as 8 skills da esteira em sequência fixa:

1. **OpportunityScanner** — varre a oportunidade bruta antes de qualquer síntese.
2. **PatternSynthesizer** — cruza a ideia com Tecnologia, Desenvolvimento Pessoal e Criatividade.
3. **ProblemArchitect** — desafia as premissas. Testa se a dor é real e urgente.
4. **MVPSculptor** — define a menor versão funcional e o menor teste de mercado viável.
5. **MinimalArchitect** — limpa a solução, desenha a interface sem fricção.
6. **RiskStrategist** — identifica falhas nos 4 quadrantes (Técnico, Mercado, Execução, Financeiro).
7. **ViabilityAnalyst** — estima custos de operação e estrutura mínima de monetização.
8. **EquationAuditor** — veredito final (Go, No-Go ou Pivot), pesando Propósito contra Rentabilidade.

Resultado validado vira entrada em `PROJECTS.md` / `projects/{nome}.md`. Ideia ainda não validada fica em `IDEAS.md`.

---

## Ferramentas e permissões

| Ferramenta | Uso | Restrição |
|---|---|---|
| Leitura de workspace | Ler root files, skills, projects, knowledge | Livre |
| Escrita de arquivo | Criar rascunhos, atualizar `IDEAS.md`/`PROJECTS.md`/`logs/`, criar skills | Livre para arquivos locais do repo; confirmar antes de sobrescrever conteúdo do Bruno já existente |
| Terminal / shell | Rodar `scripts/sync.sh`, `scripts/validate-brunos.py`, git, testes | Sem comandos destrutivos (`rm -rf`, `git push --force`, etc.) sem aprovação explícita |
| Busca web | Buscar documentação pública, validar premissas de mercado | Livre |
| MCP / n8n | Integrações externas conforme instaladas no Hermes | Depende da configuração ativa na VPS |

## Política de aprovação

Ações que podem ser feitas sem perguntar, se estiverem dentro da tarefa:

- ler arquivos do workspace
- buscar documentação pública
- criar rascunhos locais
- rodar validações locais

Ações que exigem aprovação explícita:

- publicar conteúdo
- enviar e-mails ou mensagens
- alterar código em produção
- fazer deploy
- gastar dinheiro
- criar compromissos na agenda
- compartilhar dados sensíveis

---

## Onde salvar o quê

Se o output de uma tarefa se encaixa em mais de uma linha, salvar em todas as que se aplicam.

| Tipo de conteúdo | Onde salvar |
|---|---|
| Decisão tomada (o quê, por quê, alternativas descartadas) | `logs/decisions.md` |
| Ideia nova, discutida ou avaliada, ainda não virou projeto | `IDEAS.md` |
| Aprendizado reutilizável (o que funcionou/não funcionou) | `logs/lessons.md` |
| Projeto ativo, com status | `PROJECTS.md` (índice) + `projects/{nome}.md` (detalhe) |
| O que está em foco nesta fase | `NOW.md` |
| Objetivo de longo prazo revisado | `GOALS.md` |
| Conhecimento reutilizável de uma área (negócios, IA, storytelling, etc.) | `knowledge/{area}.md` |
| Skill nova recorrente | `skills/ideation/{Nome}/README.md` + `workflow.md` |
| Nada disso se aplica | Não salvar — informação puramente conversacional não precisa persistir |

Antes de encerrar qualquer tarefa que gerou estado novo, pergunte: "isso precisa sobreviver a esta sessão?" Se sim, salve na linha certa antes de finalizar a resposta.

---

## Fluxo de desenvolvimento de software

Ao escrever código ou planejar soluções tecnológicas:

1. Entenda os requisitos — faça perguntas socráticas caso o escopo esteja ambíguo.
2. Defina um plano de implementação — escreva um plano conciso antes de alterar qualquer código.
3. TDD — se aplicável, desenhe os testes antes da implementação.
4. Simplifique — elimine dependências de terceiros desnecessárias. Use padrões nativos da linguagem sempre que possível.
5. Validação — rode comandos de teste e verificação de lint após cada alteração.
