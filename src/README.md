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
## Evidências

<img width="453" height="799" alt="image" src="https://github.com/user-attachments/assets/2e40927b-d6b6-4436-ae6c-deef4b1aab4a" />


