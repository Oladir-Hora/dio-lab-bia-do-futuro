# Passo a passo de execução

## Setup do Ollama
```bash
# 1. Instalar Ollama (ollama.com)
# 2. Baixar um modelo leve
ollama pull gpt-oss:20b
# 3. Testar se funciona
ollama run gpt-oss "Olá!"
```



## Codigo completo


Todo codigo fonte esta no arquivo `app.py`


## Exemplo de requirements.txt

```
streamlit
openai
python-dotenv
```

## Como Rodar

```bash
# 1. Instalar dependências  
   pip install streamlit pandas requests  

# 2. Garantir que Ollama está rodando  
   ollama serve  

# 3. Rodar o app  
   sstreamlit run .\src\app.py   

```
