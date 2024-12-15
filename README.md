# Amazon Stock (ML)
O projeto foi pensado para maximizar o ganho de uma ação em específico (No caso foi escolhida uma ação da Amazon) baseada em um modelo preditivo que visa prever o valor da ação em um período de 30 dias com umas variação de ±3%, que alimentará um dashboard com as principais informções e a predição.

Para isso foi criada uma API para a coleta das informações da ação, após isso foi feita uma análise exploratória (EDA) com gráficos e com a geração de novos atributos que colaboraram para a geração do modelo.


## Configurações de ambiente
### Pré-requisitos:

- [Python 3.9+](https://www.python.org)
- [Google Chrome](https://www.google.com/intl/pt-BR/chrome/)
- [Power BI](https://www.microsoft.com/pt-br/power-platform/products/power-bi/downloads)

### Instalação:
As bibliotecas listadas em [requirements.txt](requirements.txt) devem estar instaladas.
Pode-se utilizar o comando para a instalação:

```
pip install -r requirements.txt
```
### Configurações prévias ao uso

Crie um arquivo nomeado ".env" na raiz deste repositório. Ele deve conter a variável BASE_PATH sendo o caminho local do repositório na máquina do usuário, e as variáveis de conexão com o banco de dados utilizado conforme abaixo:

```
BASE_PATH = 
BD_HOST = 
BD_PORT = 
BD_DB_NAME = 
BD_USER = 
BD_PSWD = 
```

### Como usar?

Execute as células dos jupyter notebooks utilizando um ambiente virtual com as bibliotecas do requirements.txt instaladas.

Demais detalhes aqui

## Informações adicionais

Premissas que possam ser importantes, ou detalhes extras como por exemplo como acessar a documentação da API

## Contribuidores

* Anderson Pereira - RM 
* Gabriel Brites - RM 357307
* Lucas Soares - RM 
* Renan Serpa - RM 
* Ruan Costa - RM 

