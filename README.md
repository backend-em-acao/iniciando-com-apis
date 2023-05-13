# Python e FastAPI: Iniciando com APIs de forma prática

Este projeto faz parte do vídeo **Python e FastAPI: Iniciando com APIs de forma prática** do canal **Backend em Ação**. Estamos no YouTube, considere se inscrever e ajudar o canal.

**Para dúvidas ou sugestões, entre em contato pelo YouTube. Obrigado!**


## Como executar o projeto

1. Na pasta do projeto rode o comando abaixo para criar um ambiente virtual usando venv
    ```bash
    python -m venv .venv
    ```

2. Ative o ambiente virtual usando o comando apropriado para seu sistema operacional

    Linux/Mac (bash/zsh)
    ```bash
    source .venv/bin/activate
    ```

    Windows
    ```powershell
    .venv\Scripts\activate.bat
    ```

    Em caso de problema, entre em contato comigo ou consulte a documentação: https://docs.python.org/3/library/venv.html

3. Instale as dependências necessárias usando pip
    ```bash
    pip install -r requirements.txt
    ```

4. Inicialize o servidor com Uvicorn utilizando

    ```bash
    uvicorn main:app --reload
    ```

    > Se o servidor não incializar, verifique se o ambiente virtual está ativado usando o passo 2.

    > O atributo reload irá reiniciar a aplicação em caso de alterações, caso você queira testar algo.

5. Feito isso o projeto deverá estar rodando. Você pode confirmar isso pelos logs de sucesso em seu terminal e acessando as documentações em http://localhost:8000/docs ou http://localhost:8000/redoc

6. Aproveite o mundo do python!
