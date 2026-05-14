import json
import pandas as pd
import requests
import streamlit as st

# ************** CONFIGURAÇÃO **************
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss:20b"

SYSTEM_PROMPT = """ Você é o Gui, um guia financeiro amigável e didático.

OBJETIVO:
Ensinar conceitos de finanças pessoais de forma simples, usando os dados do cliente como exemplos práticos.

REGRAS:
- NUNCA recomende investimentos específicos, apenas explique como funcionam;
- JAMAIS responda a perguntas fora do tema ensino de finanças pessoais;
- Use os dados fornecidos para dar exemplos personalizados;
- Linguagem simples, como se explicasse para um amigo;
- Sempre pergunte se o cliente entendeu;
- Responda de forma sucinta e direta, com no máximo 3 parágrafos.
"""

# ============== FUNÇÃO DE PERGUNTA ==============
def perguntar(msg, perfil, transacoes, historico, produtos):
    saldo_mensal = perfil['ganhos_mensais'] - perfil['despesas_mensais']

    contexto = f"""
    CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
    OBJETIVO: {perfil['objetivo_principal']}
    GANHOS MENSAIS: R$ {perfil['ganhos_mensais']} | DESPESAS MENSAIS: R$ {perfil['despesas_mensais']}
    SALDO MENSAL: R$ {saldo_mensal}
    DÍVIDAS: {perfil['dividas']}
    RESERVA DE EMERGÊNCIA: R$ {perfil['reserva_emergencia']}
    HORIZONTE DE TEMPO: {perfil['horizonte_tempo']}
    PRIORIDADES DE GASTO: {perfil['prioridades_gasto']}

    TRANSAÇÕES RECENTES:
    {transacoes.to_string(index=False)}

    ATENDIMENTOS ANTERIORES:
    {historico.to_string(index=False)}

    PRODUTOS DISPONÍVEIS:
    {json.dumps(produtos, indent=2, ensure_ascii=False)}
    """

    prompt = f"{SYSTEM_PROMPT}\n\nCONTEXTO DO CLIENTE:\n{contexto}\n\nPergunta: {msg}"
    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']

# ************ INTERFACE STREAMLIT ************
st.title("🤖 Gui, Seu Guia Financeiro")

# ====== ONBOARDING ======
if "perfil" not in st.session_state:
    st.header("📊 Dados Básicos")
    nome = st.text_input("Qual é o seu nome?")
    idade = st.number_input("Idade", min_value=18, max_value=100, step=1)
    perfil_investidor = st.selectbox("Perfil de investidor", ["Conservador", "Moderado", "Arrojado"])
    objetivo = st.text_input("Qual é seu objetivo financeiro principal?")

    st.header("💰 Fluxo de Caixa")
    ganhos = st.number_input("Ganhos mensais (R$)", min_value=0.0, step=100.0)
    despesas = st.number_input("Despesas mensais (R$)", min_value=0.0, step=100.0)
    saldo_mensal = ganhos - despesas
    st.info(f"💵 Seu saldo mensal estimado é: R$ {saldo_mensal}")

    st.header("🏦 Situação Financeira")
    dividas = st.text_area("Você possui dívidas atuais? (ex.: cartão de crédito, empréstimos, financiamentos)")
    reserva = st.number_input("Reserva de emergência atual (R$)", min_value=0.0, step=500.0)

    st.header("🎯 Hábitos e Metas")
    horizonte = st.selectbox("Horizonte de tempo para seus objetivos", ["Curto prazo", "Médio prazo", "Longo prazo"])
    prioridades = st.text_area("Quais são suas prioridades de gasto? (ex.: lazer, educação, família)")

    if st.button("Salvar informações"):
        st.session_state.perfil = {
            "nome": nome,
            "idade": idade,
            "perfil_investidor": perfil_investidor,
            "objetivo_principal": objetivo,
            "ganhos_mensais": ganhos,
            "despesas_mensais": despesas,
            "saldo_mensal": saldo_mensal,
            "dividas": dividas,
            "reserva_emergencia": reserva,
            "horizonte_tempo": horizonte,
            "prioridades_gasto": prioridades
        }
        st.success("✅ Informações salvas! Agora posso te ajudar com exemplos personalizados.")

# ====== CHAT SEMPRE VISÍVEL ======
if "perfil" in st.session_state:
    # Carregar dados adicionais
    transacoes = pd.read_csv('./data/transacoes.csv')
    historico = pd.read_csv('./data/historico_atendimento.csv')
    produtos = json.load(open('./data/produtos_financeiros.json'))

    # Mostrar saldo mensal na interface
    saldo_mensal = st.session_state.perfil['ganhos_mensais'] - st.session_state.perfil['despesas_mensais']
    st.info(f"💰 Seu saldo mensal atual é: R$ {saldo_mensal}")

    if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
        st.chat_message("user").write(pergunta)
        with st.spinner("..."):
            resposta = perguntar(pergunta, st.session_state.perfil, transacoes, historico, produtos)
            st.chat_message("assistant").write(resposta)
