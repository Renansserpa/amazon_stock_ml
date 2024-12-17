# Amazon Stock (ML)
O projeto foi pensado para maximizar o ganho de uma ação em específico (No caso foi escolhida uma ação da Amazon) baseada em um modelo preditivo que visa prever o valor da ação em um período de 30 dias com umas variação de ±3%, que alimentará um dashboard com as principais informções e a predição.

Para isso foi criada uma API para a coleta das informações da ação, após isso foi feita uma análise exploratória (EDA) com gráficos e com a geração de novos atributos que colaboraram para a geração do modelo.


## Configurações de ambiente
### Pré-requisitos:

- [Python 3.9+](https://www.python.org)
- [Google Chrome](https://www.google.com/intl/pt-BR/chrome/)
- [Power BI](https://www.microsoft.com/pt-br/power-platform/products/power-bi/downloads)

### Instalação das dependências da API:
Para a instalação das dependências da API:

1. Instalação e configuração do [Pyenv](https://github.com/pyenv/pyenv) de acordo com seu S.O 

2. Após instalado e configurado o pyenv, instalar a versão 3.12.7 do Python 

    (projeto foi testado nas versões 3.12.3 e 3.12.7 e não foram observados bugs) 
    ```
    pyenv install 3.12.7
    ```

3. Após instalada a versão 3.12 do python, é necessário navegar através do terminal até o diretório raiz que contém os arquivos da API e executar o comando abaixo:

    ```
    pyenv local 3.12.7
    ```
 
4. Instalação e configuração do [Pipx](https://pipx.pypa.io/stable/) de acordo com seu S.O 

5. Instalação e configuração do poetry através do pipx
    ```
    pipx install poetry
    ```
6. Após instalado o poetry, é necessário navegar através do terminal até o diretório raiz que contém os arquivos da API e executar o comando abaixo:
    ```
    poetry shell
    poetry install 
    ```

### Instalação das demais dependências:
As bibliotecas listadas em [requirements.txt](requirements.txt) devem estar instaladas.
Pode-se utilizar o comando para a instalação:

```
pip install -r requirements.txt
```
### Configurações prévias ao uso

No arquivo ".env" na pasta da API alterar o download path para o caminho onde o chrome faz o download (Chrome > Configurações > Downloads):

```
DOWNLOAD_PATH= "Caminho do arquivo"
```

### Como usar?

1. Entrar no repositório na pasta da API abrir terminal e executar seguintes comandos:
    ```
    poetry shell
    fastapi dev app/main.py
    ```
    * Abrir link http://127.0.0.1:8000/docs 
    * Criar usuário: Users > Try it out > Ajustar json com username / email / senha > Execute
    * Clicar em Authorize
    * Colocar email e senha
    * Ir em webscrapper: Try it out > Execute  
2. Executar a etapa de análise exploratória na pasta EDA 
3. Executar modelo 
4. Abrir Power BI e abrir arquivo na pasta Dash do repositório

## Informações adicionais

Foi feito um modelo de classificação para TODO

## Contribuidores

* Anderson Pereira - RM 357310
* Gabriel Brites - RM 357307
* Lucas Soares - RM 356607
* Renan Serpa - RM 357478
* Ruan Costa - RM 

