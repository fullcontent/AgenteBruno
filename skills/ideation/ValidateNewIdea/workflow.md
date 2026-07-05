# Workflow: Validate New Idea

A ordem não pode ser alterada. Cada etapa consome o output da anterior.

1. **`OpportunityScanner`** — triagem: vale a pena entrar na esteira?
2. **`PatternSynthesizer`** — cruza a ideia com Tecnologia, Desenvolvimento Pessoal e Criatividade para achar o ângulo não óbvio.
3. **`ProblemArchitect`** — testa se a dor é real e urgente, ou um falso problema.
4. **`MVPSculptor`** — define a menor versão funcional e o menor teste de mercado viável.
5. **`MinimalArchitect`** — limpa a solução, desenha a interface sem fricção.
6. **`RiskStrategist`** — identifica falhas nos 4 quadrantes (Técnico, Mercado, Execução, Financeiro) e define Red Flags.
7. **`ViabilityAnalyst`** — estima custos de operação do Dia 1 e a estrutura mínima de monetização.
8. **`EquationAuditor`** — veredito final (Go, No-Go ou Pivot), pesando Propósito contra Rentabilidade.

## Interrupção antecipada

Se o `OpportunityScanner` (etapa 1) já classificar a ideia como "descartado agora", não rodar as etapas 2–8 — registrar direto em `IDEAS.md` com status "descartada" e o motivo.

## Ao final

- **Go:** criar `projects/{nome}.md` a partir de `templates/Project.md`, adicionar linha em `PROJECTS.md`, atualizar status em `IDEAS.md` para "validada (Go)".
- **No-Go:** manter em `IDEAS.md` com status "descartada (No-Go)" e o motivo do `EquationAuditor`.
- **Pivot:** manter em `IDEAS.md` com status "pivot" e a direção sugerida — pode reentrar na esteira a partir da etapa que motivou o pivot.

Registrar a decisão (etapa final e por quê) também em `logs/decisions.md`.
