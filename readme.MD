# Receitas API

Esta é uma API simples construída com FastAPI que permite buscar receitas usando a API do Forkify.

## Instalação

1. Certifique-se de ter o Python instalado em seu sistema. Você pode baixá-lo em [Python.org](https://www.python.org/).
2. Instale o Poetry, um gerenciador de dependências para Python, seguindo as instruções em [https://python-poetry.org/docs/](https://python-poetry.org/docs/).
3. Clone ou faça o download deste repositório.
4. No diretório do projeto, execute o seguinte comando para instalar as dependências:

    ```bash
    poetry install
    ```

## Rodando o servidor

Após a instalação das dependências, você pode iniciar o servidor FastAPI usando o comando abaixo:

    ```bash
    uvicorn app:app --reload
    ```


Isso iniciará o servidor na porta padrão 8000. Se desejar, você pode especificar uma porta diferente adicionando `--port <PORTA>` ao comando acima.

## Usando a API

Uma vez que o servidor estiver em execução, você pode acessar a API para buscar receitas usando o endpoint `/recipes/{prato}`.

Por exemplo, para buscar receitas de pizza, você pode fazer uma requisição GET para:

    http://localhost:8000/recipes/pizza

Isso retornará as receitas de pizza encontradas pela API do Forkify.