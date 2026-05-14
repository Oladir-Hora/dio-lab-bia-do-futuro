# 🤖 Gui — Seu Guia Financeiro Inteligente

> Agente de IA educativo para finanças pessoais, desenvolvido como solução para o laboratório **Bia do Futuro** da [Digital Innovation One](https://www.dio.me/).

---

## 💡 O Problema

Muitas pessoas têm dificuldade em entender conceitos básicos de finanças pessoais. A falta de informação acessível leva a decisões financeiras desinformadas — não por descuido, mas por ausência de um guia confiável e descomplicado.

## ✅ A Solução: Gui

**Gui** (Guia Financeiro) é um agente conversacional baseado em IA que ensina finanças pessoais de forma simples, personalizada e segura. Ele não recomenda investimentos específicos — ele **educa**, usando os próprios dados do usuário como exemplos práticos.

---

## 🧠 Persona do Agente

| Atributo | Descrição |
|---|---|
| **Nome** | Gui (Guia Financeiro) |
| **Personalidade** | Calmo, paciente, encorajador |
| **Tom de voz** | Amigável, acessível, didático — como um professor de confiança |
| **Público-alvo** | Qualquer pessoa, especialmente iniciantes em finanças |

**Exemplos de linguagem:**
- Saudação: *"Olá! Como posso te ajudar com suas finanças hoje?"*
- Confirmação: *"Entendi! Deixa eu verificar isso para você."*
- Limitação: *"Não tenho essa informação no momento, mas posso ajudar com..."*

---

## 🏗️ Arquitetura

```
flowchart TD
    A[Usuário] --> B[Streamlit - Interface Visual]
    B --> C[LLM via Ollama - local]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação Anti-Alucinação]
    E --> F[Resposta Personalizada]
```

| Componente | Tecnologia |
|---|---|
| Interface | Streamlit |
| LLM | Ollama (local) — modelo `gpt-oss:20b` |
| Base de Conhecimento | JSON e CSV mockados |
| Validação | Regras no system prompt |

---

## 📁 Estrutura do Repositório

```
📁 dio-lab-bia-do-futuro/
│
├── 📄 README.md
│
├── 📁 data/
│   ├── perfil_investidor.json        ← Fonte principal: preenchido pelo usuário
│   ├── historico_atendimento.csv     ← Simulação de interações anteriores
│   ├── produtos_financeiros.json     ← Catálogo fictício de produtos
│   └── transacoes.csv                ← Transações simuladas para exemplos
│
├── 📁 docs/
│   ├── 01-documentacao-agente.md     ← Caso de uso e arquitetura
│   ├── 02-base-conhecimento.md       ← Estratégia de dados
│   ├── 03-prompts.md                 ← Engenharia de prompts
│   ├── 04-metricas.md                ← Avaliação e resultados
│   └── 05-pitch.md                   ← (em breve)
│
├── 📁 src/
│   └── app.py                        ← Aplicação principal (Streamlit)
│
├── 📁 assets/
└── 📁 examples/
```

---

## 🗃️ Base de Conhecimento

O Gui combina dados reais do usuário com dados educativos mockados:

| Arquivo | Tipo | Uso |
|---|---|---|
| `perfil_investidor.json` | **Dado real** (via formulário) | Personalização das respostas |
| `transacoes.csv` | Simulado | Exemplos de fluxo de caixa |
| `historico_atendimento.csv` | Simulado | Contexto de atendimentos anteriores |
| `produtos_financeiros.json` | Fictício | Explicação de produtos financeiros |

**Exemplo de contexto montado para o LLM:**
```
CLIENTE: Oladir da Hora, 44 anos, perfil Moderado
OBJETIVO: Reserva de emergência
GANHOS MENSAIS: R$ 9.000 | DESPESAS: R$ 7.500 | SALDO: R$ 1.500

RESUMO DE GASTOS (simulado):
- Moradia: R$ 1.380 | Alimentação: R$ 570 | Transporte: R$ 295

PRODUTOS DISPONÍVEIS: Tesouro Selic, CDB, LCI/LCA, Fundo Multimercado...
```

---

## 🧩 System Prompt

```
Você é o Gui, um guia financeiro amigável e didático.

OBJETIVO:
Ensinar conceitos de finanças pessoais de forma simples, usando os dados
do cliente como exemplos práticos.

REGRAS:
- NUNCA recomende investimentos específicos — apenas explique como funcionam
- JAMAIS responda perguntas fora do tema finanças pessoais
- Use os dados fornecidos para dar exemplos personalizados
- Linguagem simples, como se explicasse para um amigo
- Sempre pergunte se o cliente entendeu
- Responda de forma sucinta, com no máximo 3 parágrafos
```

### Exemplos de Interação

**Conceito financeiro:**
> 👤 "O que é CDI?"
> 🤖 "CDI é uma taxa de referência usada pelos bancos. Quando um investimento rende '100% do CDI', significa que ele acompanha essa taxa. Hoje o CDI está próximo da Selic. Quer que eu explique a diferença entre os dois?"

**Análise de gastos:**
> 👤 "Onde estou gastando mais?"
> 🤖 "Olhando suas transações de outubro, sua maior despesa é moradia (R$ 1.380), seguida de alimentação (R$ 570). Juntas representam quase 80% dos seus gastos. Quer que eu explique algumas estratégias de organização?"

**Pergunta fora do escopo:**
> 👤 "Qual a previsão do tempo para amanhã?"
> 🤖 "Sou especializado em finanças e não tenho informações sobre previsão do tempo. Posso ajudar com algo relacionado às suas finanças?"

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.9+
- [Ollama](https://ollama.ai/) instalado e rodando localmente
- Modelo `gpt-oss:20b` disponível no Ollama

### Instalação

```bash
# Clone o repositório
git clone https://github.com/Oladir-Hora/dio-lab-bia-do-futuro.git
cd dio-lab-bia-do-futuro

# Instale as dependências
pip install streamlit pandas requests

# Inicie o Ollama com o modelo
ollama run gpt-oss:20b

# Execute a aplicação
streamlit run src/app.py
```

### Fluxo de uso

1. Preencha o formulário de onboarding com seus dados financeiros
2. O perfil é salvo na sessão e usado para personalizar as respostas
3. Converse com o Gui pelo chat e tire suas dúvidas sobre finanças

---

## 🛡️ Segurança e Anti-Alucinação

O Gui foi projetado para ser confiável no contexto financeiro:

- ✅ Responde apenas com base nos dados fornecidos
- ✅ Admite quando não sabe algo
- ✅ Foca em **educar**, não em aconselhar
- ✅ Não recomenda investimentos específicos
- ❌ Não acessa dados bancários sensíveis
- ❌ Não substitui um profissional certificado (CFP, assessor de investimentos)

---

## 📊 Avaliação e Métricas

| Métrica | O que avalia | Resultado |
|---|---|---|
| **Assertividade** | O agente respondeu o que foi perguntado? | ✅ Aprovado |
| **Segurança** | Evitou inventar informações? | ✅ Aprovado |
| **Coerência** | Resposta coerente com o perfil do cliente? | ✅ Aprovado |
| **Escopo** | Recusa perguntas fora de finanças? | ✅ Aprovado |

**O que funcionou bem:** Tudo funcionou como esperado nos testes estruturados.

**Pontos de melhoria:**
- O uso da rede local (Ollama) adiciona latência nas respostas
- Incorporar produtos financeiros reais no catálogo

---

## 🛠️ Tecnologias Utilizadas

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=flat&logo=ollama&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)

---

## 👤 Autor

Desenvolvido por **Oladir da Hora** como solução para o laboratório **Bia do Futuro** da [DIO](https://www.dio.me/).

---

## 📄 Licença

Este projeto é um fork de [digitalinnovationone/dio-lab-bia-do-futuro](https://github.com/digitalinnovationone/dio-lab-bia-do-futuro) e segue a licença do repositório original. 
