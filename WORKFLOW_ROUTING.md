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

## Comandos Diretos (Slash Commands)

Sempre que a mensagem iniciar com uma barra (`/`), pule a interpretação central e engatilhe a funcionalidade:

- `/agora`: Interrompe a execução atual, filtra inbox/tarefas e retorna imediatamente os **3 a 5 itens mais críticos** que exigem ação do Bruno, postando no `#comando`.
- `/foco [Xh]`: Desliga notificações não-urgentes pelo tempo especificado e acumula as mensagens para um pacote de entrega ao final do período.
- `/operacoes`: Vai direto para a agenda ou tasks.
- `/comunicacao`: Vai direto para leitura ou escrita de e-mails.
- `/produtos` ou `/tech`: Aciona conversas de SaaS.
- `/criativo`: Aciona conversas de cinema/storytelling.
- `/financas`: Aciona contexto financeiro.
- `/saude`: Aciona monitor de hábitos e descanso.
- `/pesquisa`: Aciona uma busca externa não-viciada.

## Integrações
As ações de rotina interagem ativamente com ferramentas via automação (ex: n8n, Make ou APIs nativas no Hermes).
- Gmail (COMUNICACAO, FINANCAS)
- Calendar & Tasks (OPERACOES, SAUDE)
- Drive (FINANCAS)
- WhatsApp (OPERACOES para monitoramento, COMUNICACAO para VIPs)
