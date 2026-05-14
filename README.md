# 🤖 Agente Financeiro Inteligente com IA Generativa

## Contexto

Os assistentes virtuais no setor financeiro estão evoluindo de simples chatbots reativos para **agentes inteligentes e proativos**. Neste desafio, você vai idealizar e prototipar um agente financeiro que utiliza IA Generativa para:

- **Antecipar necessidades** ao invés de apenas responder perguntas
- **Personalizar** sugestões com base no contexto de cada cliente
- **Cocriar soluções** financeiras de forma consultiva
- **Garantir segurança** e confiabilidade nas respostas (anti-alucinação)

> [!TIP]
> Na pasta [`examples/`](./examples/) você encontra referências de implementação para cada etapa deste desafio.

---

## O Que Você Deve Entregar

### 1. Documentação do Agente

Defina **o que** seu agente faz e **como** ele funciona:

- **Caso de Uso:** Qual problema financeiro ele resolve? (ex: consultoria de investimentos, planejamento de metas, alertas de gastos)
- **Persona e Tom de Voz:** Como o agente se comporta e se comunica?
- **Arquitetura:** Fluxo de dados e integração com a base de conhecimento
- **Segurança:** Como evitar alucinações e garantir respostas confiáveis?

📄 **Template:** [`docs/01-documentacao-agente.md`](./docs/01-documentacao-agente.md)

---

### 2. Base de Conhecimento

Utilize os **dados disponíveis** na pasta [`data/`](./data/) para alimentar seu agente:

| Arquivo | Formato | Descrição |
|---------|---------|-----------|
| `perfil_investidor.json` | JSON | Dados reais fornecidos pelo usuário (nome, idade, ganhos, despesas, dívidas, objetivos) |
| `historico_atendimento.csv` | CSV | Simulação de interações anteriores |
| `produtos_financeiros.json` | JSON | Catálogo fictício de produtos financeiros para fins educativos |
| `transacoes.csv` | CSV | **Transações simuladas** para exemplos de fluxo de caixa (não são dados reais) |

---

## 📂 Transações financeiras em CSV

O arquivo `data/transacoes.csv` contém um conjunto de **transações simuladas** que servem como exemplo de movimentações financeiras.  
Ele não representa dados reais do usuário, mas ajuda o agente a ilustrar conceitos de **fluxo de caixa**, **categorias de despesas** e **receitas**.

### Estrutura
- **data**: data da transação (AAAA-MM-DD)  
- **descricao**: descrição da transação (ex.: Salário, Aluguel, Supermercado)  
- **categoria**: categoria da transação (ex.: receita, moradia, alimentação, lazer, saúde)  
- **valor**: valor monetário  
- **tipo**: `entrada` (receita) ou `saida` (despesa)  

### Uso no agente
- Serve como **material didático** para explicar entradas e saídas.  
- Os **dados reais do usuário** são coletados via formulário e salvos em `perfil_investidor.json`.  
- Complementa o contexto para exemplos práticos de orçamento.  


📄 **Template:** [`docs/02-base-conhecimento.md`](./docs/02-base-conhecimento.md)

---

### 3. Prompts do Agente

Documente os prompts que definem o comportamento do seu agente:

- **System Prompt:** Instruções gerais de comportamento e restrições
- **Exemplos de Interação:** Cenários de uso com entrada e saída esperada
- **Tratamento de Edge Cases:** Como o agente lida com situações limite

📄 **Template:** [`docs/03-prompts.md`](./docs/03-prompts.md)

---

### 4. Aplicação Funcional

Desenvolva um **protótipo funcional** do seu agente:

- Chatbot interativo (sugestão: Streamlit, Gradio ou similar)
- Integração com LLM (via API ou modelo local)
- Conexão com a base de conhecimento

📁 **Pasta:** [`src/`](./src/)

---

### 5. Avaliação e Métricas

Descreva como você avalia a qualidade do seu agente:

**Métricas Sugeridas:**
- Precisão/assertividade das respostas
- Taxa de respostas seguras (sem alucinações)
- Coerência com o perfil do cliente

📄 **Template:** [`docs/04-metricas.md`](./docs/04-metricas.md)

---

### 6. Pitch

Grave um **pitch de 3 minutos** (estilo elevador) apresentando:

- Qual problema seu agente resolve?
- Como ele funciona na prática?
- Por que essa solução é inovadora?

📄 **Template:** [`docs/05-pitch.md`](./docs/05-pitch.md)

---

## Ferramentas Sugeridas

Todas as ferramentas abaixo possuem versões gratuitas:

| Categoria | Ferramentas |
|-----------|-------------|
| **LLMs** | [ChatGPT](https://chat.openai.com/), [Copilot](https://copilot.microsoft.com/), [Gemini](https://gemini.google.com/), [Claude](https://claude.ai/), [Ollama](https://ollama.ai/) |
| **Desenvolvimento** | [Streamlit](https://streamlit.io/), [Gradio](https://www.gradio.app/), [Google Colab](https://colab.research.google.com/) |
| **Orquestração** | [LangChain](https://www.langchain.com/), [LangFlow](https://www.langflow.org/), [CrewAI](https://www.crewai.com/) |
| **Diagramas** | [Mermaid](https://mermaid.js.org/), [Draw.io](https://app.diagrams.net/), [Excalidraw](https://excalidraw.com/) |

---

## Estrutura do Repositório

```
📁 lab-agente-financeiro/
│
├── 📄 README.md
│
├── 📁 data/                          # Dados mockados para o agente
│   ├── historico_atendimento.csv     # Histórico de atendimentos (CSV)
│   ├── perfil_investidor.json        # Perfil do cliente (JSON)
│   ├── produtos_financeiros.json     # Produtos disponíveis (JSON)
│   └── transacoes.csv                # Histórico de transações (CSV)
│
├── 📁 docs/                          # Documentação do projeto
│   ├── 01-documentacao-agente.md     # Caso de uso e arquitetura
│   ├── 02-base-conhecimento.md       # Estratégia de dados
│   ├── 03-prompts.md                 # Engenharia de prompts
│   ├── 04-metricas.md                # Avaliação e métricas
│   └── 05-pitch.md                   # Roteiro do pitch
│
├── 📁 src/                           # Código da aplicação
│   └── app.py                        # (exemplo de estrutura)
│
├── 📁 assets/                        # Imagens e diagramas
│   └── ...
│
└── 📁 examples/                      # Referências e exemplos
    └── README.md
```

---

## 📌 Dicas Finais

1. **Comece pelo prompt:** Um bom *system prompt* é a base de um agente eficaz.  
2. **Use os dados mockados com clareza:** Eles garantem consistência e evitam problemas com dados sensíveis. No seu projeto, `transacoes.csv`, `historico_atendimento.csv` e `produtos_financeiros.json` são apenas exemplos educativos.  
3. **Destaque os dados reais:** O `perfil_investidor.json` é preenchido pelo usuário via formulário e deve ser tratado como a fonte principal.  
4. **Foque na segurança:** No setor financeiro, evitar alucinações é crítico. O agente deve admitir quando não sabe algo e nunca recomendar investimentos específicos.  
5. **Teste cenários reais:** Simule perguntas que um cliente faria de verdade, usando os dados do perfil e os exemplos mockados para enriquecer a resposta.  
6. **Seja direto no pitch:** 3 minutos passam rápido, vá ao ponto e mostre claramente o problema que o agente resolve e como funciona.  
