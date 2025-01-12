
## TESTE - MANOEL MESSIAS DA SILVA NETO

Essa aplicação foi construída em Python, utilizando , SQLAlchemy Async para interação com o banco de dados e Alembic para migrações de banco de dados. A aplicação possui módulos distintos, cada um oferecendo funcionalidades específicas.

# PRIMEIROS PASSOS [NÃO NECESSARIOS VIA DOCKER]
***Recomendo "make up", conforme execução via docker.***
* ## INSTALE AS DEPENDÊNCIAS NECESSÁRIAS:
    bash
    * poetry install
    * poetry shell

* ### DEFINA AS ENVIROMENTS
    .env
    * DATABASE_URL="postgresql+asyncpg://usuario_do_banco:{senha_do_banco}@{host_do_banco}:{porta_do_banco}/{nome_do_banco}" 
    * BASE_URL_CASHBACK="https://mdaqk8ek5j.execute-api.us-east-1.amazonaws.com/"
    * TOKEN_CASHBACK="ZXPURQOARHiMc6Y0flhRC1LVlZQVFRnm"
    * ELASTIC_SERVICE_NAME="o-boticario-service"
    * ELASTIC_SERVER_URL=http://apm-server:8200
    * ELASTIC_USER=elastic
    * ELASTIC_PASSWORD=changeme
* ## BANCO DE DADOS
    * EM SEGUIDA EXECUTE AS MIGRAÇÕES DO BANCO DE DADOS USANDO -> ALEMBIC
    * ATENCÃO ***O ALEMBIC NÃO CRIA O BANCO DE DADOS É NCESSARIO CRIAR MANUALMENTE***
    * ## INICIE A ESTRUTURA DO BANCO DE DADOS
        bash
        * #### COMANDO RESPONSAVEL POR VALIDAR AS ESTRUTURA
            * alembic revision --autogenerate -m "init"
        * #### COMANDO RESPONSAVEL POR EXECUTAR AS ALTERAÇÕES
            * alembic upgrade head
# INICIANDO O PROJETO
* FOI CONFIGURADO DUAS OPÇÕES DE DEPURAÇÃOO SENDO ELAS.

* EXECUÇÃO MANUAL -> TERMINAL.
    * ATENÇÃO NECESSARIO SUBIR DEPENDECIAS MANUAL.
    * API FASTAPI
        * uvicorn main:app --reload --host 0.0.0.0 --port 8000
* EXECUÇÃO AUTOMATICA -> VIA DOCKER.
    * API FASTAPI
        * make up
# EXECUTAR VIA DOCKER
### comandos:
* ###    make up
    * Este comando irá iniciar alguns serviços, caso seja necessario alterar a porta dos serviços no arquivo docker-compose.yml
        * api-backend -> http://localhost:8002
        * postgresql -> localhost:54321
        * elastic-apm -> localhost:9200
        * elastic-search -> localhost:8200
        * elastic-kiabna -> http://localhost:5601
            * usuario:elastic
            * senha:changeme
            * para ver os logs acesso APM->SERVICES->o-botiario-service
* ###    make down
    * Este comando irá remover os container, porem mantem a imagens,network e volumes criados.
* ###    make clean
    * Este comando irá remover os container,imagens,network e volumes criados.

## TECNOLOGIAS UTILIZADAS
* Python 3.12

    * Descrição: 
        * Python é uma linguagem de programação de alto nível, conhecida por sua simplicidade e legibilidade. A versão 3.12 inclui várias melhorias de desempenho, novas funcionalidades e aprimoramentos na linguagem.
    * Para que serve: 
        * É a linguagem de programação principal utilizada para desenvolver a aplicação.
* FastAPI

    * Descrição:
        * FastAPI é um framework web moderno e de alto desempenho para construir APIs com Python 3.6+ baseado em padrões como OpenAPI e JSON Schema. Ele é conhecido por sua facilidade de uso, velocidade e suporte automático à documentação.
    * Para que serve:
        * É o framework principal utilizado para desenvolver APIs na aplicação, proporcionando uma maneira eficiente e rápida de criar endpoints robustos e bem documentados.

* Uvicorn

    * Descrição:
        * Uvicorn é um servidor ASGI (Asynchronous Server Gateway Interface) rápido e leve, criado para rodar aplicações Python de alto desempenho. Ele é baseado no loop de eventos uvloop e no servidor HTTP httptools, oferecendo suporte total a asyncio, WebSockets e HTTP/2. Uvicorn é conhecido por sua simplicidade, eficiência e compatibilidade com frameworks modernos como FastAPI e Starlette.
    * Para que serve:
        * Uvicorn é utilizado para servir aplicações web assíncronas, proporcionando baixa latência e alta capacidade de processamento. É ideal para desenvolver APIs rápidas e eficientes, além de suportar recursos modernos como WebSockets e comunicação assíncrona.
* Requests

    * Descrição:
        * Requests é uma biblioteca HTTP para Python, que facilita a realização de requisições HTTP, tratando detalhes complexos das requisições de uma maneira simples e legível.
    * Para que serve:
        * Utilizada para fazer chamadas HTTP de maneira fácil e eficiente, como consumo de APIs RESTful.
* SQLAlchemy

    * Descrição:
        * SQLAlchemy é uma biblioteca de mapeamento objeto-relacional (ORM) para Python, que fornece um conjunto completo de ferramentas para interagir com bancos de dados usando uma abordagem orientada a objetos.
    * Para que serve:
        * Utilizada para gerenciar a comunicação entre a aplicação e o banco de dados de forma eficiente e estruturada, mapeando classes Python para tabelas do banco de dados.
* Pydantic

    * Descrição:
        * Pydantic é uma biblioteca de validação de dados para Python, que permite a definição de modelos de dados claros e a validação rigorosa dos dados recebidos e enviados.
    * Para que serve:
        * Utilizada para garantir a integridade dos dados ao validar e converter dados entre tipos diferentes de maneira automática.
* Alembic

    * Descrição:
        * Alembic é uma ferramenta de migração de banco de dados para SQLAlchemy, que permite a gestão e o versionamento das alterações na estrutura do banco de dados.
    * Para que serve:
        * Utilizada para aplicar, revisar e gerenciar mudanças no esquema do banco de dados ao longo do desenvolvimento da aplicação.
* asyncpg

    * Descrição:
        * asyncpg é uma biblioteca assíncrona de driver de banco de dados para PostgreSQL em Python, projetada para ser rápida e eficiente.
    * Para que serve:
        * Utilizada para conectar e interagir com o banco de dados PostgreSQL de forma assíncrona, melhorando a performance de operações de I/O intensivo.
* Elasticsearch
    * Descrição:
        * Elasticsearch é um mecanismo de busca e análise distribuído, desenvolvido em Java e baseado no Apache Lucene.
    * Para que serve:
        * É utilizado para armazenar, buscar e analisar grandes volumes de dados em tempo quase real. Ideal para logs, dados estruturados e não estruturados.
* Kibana
    * Descrição:
        * Kibana é uma ferramenta de visualização de dados que trabalha em conjunto com o Elasticsearch, permitindo criar dashboards interativos.
    * Para que serve:
        * Serve para explorar, visualizar e criar gráficos baseados nos dados armazenados no Elasticsearch. Muito usado para monitoramento de sistemas e análise de logs.
* APM (Application Performance Monitoring)
    * Descrição:
        * APM é uma solução de monitoramento de desempenho de aplicações, que captura métricas como tempos de resposta, erros e uso de recursos.
    * Para que serve:
        * É utilizado para rastrear e diagnosticar problemas de performance em aplicações, identificando gargalos e melhorando a experiência do usuário fina

## MINI MODULOS
### APP AUTH
* Responsável pela regra de negocio e modelo com banco de dados do Modulo de autenticação.
### APP REVENDEDOR
* Responsável pela regra de negocio e modelo com banco de dados do Modulo de revendedor.
### APP COMPRA
* Responsável pela regra de negocio e modelo com banco de dados do modulo de compra.

## ESTRUTURA DE PASTA DO PROJETO
```
projeto/
│
├── src/
│   ├── system/
│   │   ├── alembic/
│   │   │   ├── env.py
│   │   │   ├── README
│   │   │   ├── script.py.mako
│   │   │   └── versions/
│   │   │       ├── __init__.py
│   │   │       └── ...
│   │   ├── core/
│   │   │   ├── model_core.py
│   │   │   ├── logger_core.py
│   │   │   ├── utils_core.py
│   │   │   ├── database.py
│   │   │   └── integrations/
│   │   │       └── cashback_api.py
│   │   ├── test
│   │   │   ├── test_cashback_api.py
│   │   │   ├── test_revendedor.py
│   │   │   └── test_compra.py
│   └── apps/
│       ├── auth
│       │   ├── controller.py
│       │   ├── route.py
│       │   └── model.py
│       ├── compra
│       │   ├── controller.py
│       │   ├── route.py
│       │   └── model.py
│       └── revendedor
│           ├── controller.py
│           ├── route.py
│           └── model.py
├── .env
├── alembic.ini
├── requirements.txt
└── main.py
```
# MANOEL MESSIAS DA SILVA NETO