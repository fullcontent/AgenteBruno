# WORKFLOW_ROUTING.md — Roteamento, Especialistas e Comandos

Este arquivo centraliza o mapeamento de como o **Superagente Orquestrador** (`#comando`) delega atividades para os especialistas operacionais e quais os comandos diretos disponíveis.

## Tópicos do Telegram e seus Especialistas

A comunicação do agente com o Bruno ocorre em um Supergrupo no Telegram. O Orquestrador central escuta o `#comando` e roteia os outputs para:

1. **`#comando` (Superagente Orquestrador)**: Canal central. Processa intenções complexas, aplica a Equação do Sentido e delega tarefas.
2. **`#operacoes` (OPERACOES)**: Canal focado em Tempo, Agenda, Tarefas (Google Tasks/Calendar) e WhatsApp Monitor.
3. **`#comunicacao` (COMUNICACAO)**: Canal focado em Inbox, Rascunhos de E-mail (Gmail) e rastreamento VIP.
4. **`#tecnologia-produto` (PRODUTO)**: Canal de discussões sobre SaaS, Código, e Validação de Ideias.
5. **`#estudio-criativo` (CRIATIVO)**: Canal de AventuFilm, documentários e roteiros.
6. **`#crescimento-financas` (FINANCAS)**: Canal de receita, extratos mensais e capital.
7. **`#saude-vitalidade` (SAUDE)**: Canal para treinos, montanhismo e planejamento de vida.
8. **`#pesquisa-radar` (PESQUISA)**: Canal para levantamento de mercado e inteligência de dados.
9. **`#resumo-diario`**: Mural puramente passivo. Recebe os resumos proativos matinais e noturnos.

---

## Regras de Roteamento por Tema

Quando o Bruno enviar uma mensagem sem comando (sem `/`), rotear assim:

| Tema | Destino |
|---|---|
| E-mails, inbox, rascunhos | → COMUNICACAO |
| Agenda, lembretes, WhatsApp diário | → OPERACOES |
| Projetos autorais, vídeo | → CRIATIVO |
| Código, SaaS, ideias novas | → PRODUTO |
| Dinheiro, extratos, planilhas | → FINANCAS |
| Exercícios, montanha, rotina | → SAUDE |
| Pesquisa web | → PESQUISA |

Se o tema for ambíguo ou tocar mais de um domínio, o Orquestrador decide ou escala para `#comando`.

---

## Comandos Diretos (Slash Commands)

Sempre que a mensagem iniciar com uma barra (`/`), pule a interpretação central e engatilhe o especialista diretamente:

- **`/operacoes`**: Vai direto para OPERACOES — agenda, tarefas, lembretes.
- **`/comunicacao`**: Vai direto para COMUNICACAO — inbox, rascunhos, Gmail.
- **`/produtos`** ou **`/tech`**: Vai direto para PRODUTO — código, SaaS, ideias.
- **`/criativo`**: Vai direto para CRIATIVO — cinema, vídeo, projetos autorais.
- **`/financas`**: Vai direto para FINANCAS — extratos, planilhas, dinheiro.
- **`/saude`**: Vai direto para SAUDE — exercícios, montanha, rotina.
- **`/pesquisa`**: Vai direto para PESQUISA — busca web, inteligência.

- **`/agora`**: Interrompe execução atual, filtra inbox/tarefas, retorna 3-5 itens mais críticos no `#comando`.
- **`/foco [Xh]`**: Silencia notificações não-urgentes pelo tempo especificado e acumula para entrega posterior.

## Integrações

As ações de rotina interagem ativamente com ferramentas via automação (ex: n8n, Make ou APIs nativas no Hermes).

- Gmail (COMUNICACAO, FINANCAS)
- Calendar & Tasks (OPERACOES, SAUDE)
- Drive (FINANCAS)
- WhatsApp (OPERACOES para monitoramento, COMUNICACAO para VIPs)
