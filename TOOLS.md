# TOOLS.md — ferramentas e permissões

Lista do que o agente pode usar para executar tarefas, e sob que condições.

## Ferramentas nativas do Hermes

| Ferramenta | Uso | Restrição |
|---|---|---|
| `read_file` / leitura de workspace | Ler root files, skills, memory, docs | Livre |
| `write_file` / criar arquivo | Criar rascunhos, atualizar memory, criar skills | Livre para arquivos locais do repo; confirmar antes de sobrescrever conteúdo do Bruno já existente |
| `terminal` / shell | Rodar scripts (`sync.sh`, `validate-agent-os.py`), git, testes | Sem comandos destrutivos (`rm -rf`, `git push --force`, etc.) sem aprovação explícita |
| `web_search` | Buscar documentação pública, validar premissas de mercado | Livre |

## Integrações externas

| Integração | Uso | Status |
|---|---|---|
| MCP (Model Context Protocol) | Conectar ferramentas externas (Notion, Slack, etc.) conforme instaladas no Hermes | Depende da configuração ativa do Hermes na VPS |
| n8n | Automações de backoffice — relatórios, monitoramento de repositórios, auditorias | Em pipeline, aguardando estabilização do núcleo do agente (ver `memory/tasks.md`) |

## Política de uso

- Prefira a ferramenta mais direta para a tarefa — não rode shell para algo que leitura de arquivo resolve.
- Verifique resultado com evidência real (rodar teste, ler saída) antes de reportar como concluído.
- Ações que envolvem publicar, gastar dinheiro, deploy ou dados sensíveis seguem a política de aprovação do `AGENTS.md`, não este arquivo.
