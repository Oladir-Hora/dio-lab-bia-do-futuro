# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `perfil_investidor.json` | JSON | Fonte principal: preenchido pelo usuário via formulário (dados reais coletados na interface) |
| `historico_atendimento.csv` | CSV | Simulação de interações anteriores para dar contexto |
| `produtos_financeiros.json` | JSON | Catálogo fictício de produtos financeiros para explicar conceitos |
| `transacoes.csv` | CSV | **Transações simuladas** para exemplos educativos de fluxo de caixa |

---

## Adaptações nos Dados

- O `perfil_investidor.json` agora é **dinamicamente preenchido pelo usuário** através do formulário Streamlit.  
- Os demais arquivos (`transacoes.csv`, `historico_atendimento.csv`, `produtos_financeiros.json`) permanecem **mockados** e servem apenas para fins educativos.  

---

## Estratégia de Integração

### Como os dados são carregados?

O agente carrega os dados da pasta `data/` e combina com o perfil fornecido pelo usuário:

```python
import pandas as pd
import json

# Perfil do usuário (via formulário Streamlit)
perfil = st.session_state.perfil

# CSVs mockados
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')

# JSON fictício
produtos = json.load(open('./data/produtos_financeiros.json'))

```
### Como os dados são usados no prompt?
# Como os dados são usados no prompt?
O `perfil_investidor.json` (preenchido pelo usuário) é a fonte principal para personalização.

> Os arquivos mockados (transacoes.csv, historico_atendimento.csv, produtos_financeiros.json) são usados como exemplos educativos para enriquecer o contexto.
---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

O exemplo de contexto montado abaixo, se baseia nos dados originais da base de conhecimento, mas os sintetiza deixando apenas as informações mais relevantes, otimizando assim o consumo de tokens. Entretanto, vale lembrar que mais importante do que economizar tokens, é ter todas as informações relevantes disponíveis em seu contexto.

```
DADOS DO CLIENTE (perfil_investidor.json - preenchido pelo usuário):
- Nome: Oladir da Hora
- Idade: 44
- Perfil: Moderado
- Objetivo: Reserva de emergência
- Ganhos mensais: R$ 9.000
- Despesas mensais: R$ 7.500
- Saldo mensal: R$ 1.500
- Dívidas: (informadas pelo usuário)
- Reserva de emergência: (informada pelo usuário)
- Horizonte de tempo: Médio prazo
- Prioridades de gasto: (informadas pelo usuário)

RESUMO DE GASTOS (transacoes.csv - simulado):
- Moradia: R$ 1.380
- Alimentação: R$ 570
- Transporte: R$ 295
- Saúde: R$ 188
- Lazer: R$ 55,90
- Total de saídas simuladas: R$ 2.488,90

HISTÓRICO DE ATENDIMENTO (historico_atendimento.csv - simulado):
- 15/09/2025 (chat): Pergunta sobre CDB
- 01/10/2025 (chat): Explicação sobre Tesouro Selic
- 12/10/2025 (chat): Acompanhamento de metas financeiras

PRODUTOS DISPONÍVEIS (produtos_financeiros.json - fictício):
- Tesouro Selic (risco baixo, indicado para reserva de emergência)
- CDB Liquidez Diária (risco baixo, rendimento diário)
- LCI/LCA (risco baixo, isento de IR, prazo mínimo 90 dias)
- Fundo Multimercado (risco médio, diversificação)
- Fundo de Ações (risco alto, foco no longo prazo)


```
