# 🚌 Projeto SPTrans Data Pipeline

### Monitoramento em Near Real-Time do Transporte Público de São Paulo

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Apache Spark](https://img.shields.io/badge/Spark-3.3-orange)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100-green)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)
![NiFi](https://img.shields.io/badge/Apache%20NiFi-Dataflow-success)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-informational)
![MinIO](https://img.shields.io/badge/MinIO-S3%20Storage-critical)

Este projeto implementa uma arquitetura moderna de dados para monitorar em tempo quase real o transporte público de São Paulo, utilizando a API Olho Vivo (SPTrans).
Toda a solução foi construída com ferramentas open source, seguindo boas práticas de engenharia de dados, arquitetura Medallion (Bronze → Silver → Gold) e processamento distribuído.

O objetivo é coletar, tratar, enriquecer e analisar informações das principais linhas de ônibus da cidade, gerando KPIs estratégicos como pontualidade, atraso médio, headway e frota ativa — tudo exibido em um dashboard profissional no Power BI.

A solução final demonstra habilidades completas de ponta a ponta em engenharia de dados, incluindo ingestão, transformação, modelagem analítica e visualização.


## 🚀 Destaques do Projeto

Ingestão automatizada com Apache NiFi, incluindo autenticação dinâmica, manipulação de cookies e coleta contínua da API Olho Vivo. e a ingestão com spark, garantindo o looping continuo da previsão de chegada de alguns dos principais onibus de cada região de SP.

Data Lake estruturado em camadas Raw, Silver e Gold, armazenado no MinIO (S3 compatível).

Processamento distribuído com Apache Spark (batch e streaming), incluindo:

Tratamento completo dos arquivos GTFS (linhas, viagens, paradas).

Cálculo e normalização da previsão de chegada das principais linhas por região.

Enriquecimento e consolidação dos dados para análise operacional.

Modelo analítico (Camada Gold) armazenado no PostgreSQL, com KPIs prontos para consumo.

Dashboard interativo no Power BI com insights sobre desempenho, atrasos e operação por linha e região.

Infra totalmente containerizada via Docker Compose, reproduzível em qualquer máquina.


# ARQUITETURA DO PROJETO


<img width="502" height="748" alt="Projeto drawio (6)" src="https://github.com/user-attachments/assets/71da1095-0825-4272-ab06-7885668da372" />




## 🧠 Competências Demonstradas

Arquitetura Medallion (Bronze → Silver → Gold)

Data Lake com MinIO (S3)

Ingestão automatizada com Apache NiFi

Processamento com Apache Spark (PySpark)

Orquestração com Docker / Docker Compose

Modelagem analítica em PostgreSQL

Visualização de dados com Power BI

Manipulação de APIs, GTFS e dados geoespaciais

Boas práticas de versionamento e organização de pipelines


## 🎯 Objetivo

Criar uma infraestrutura completa de engenharia de dados capaz de:

Monitorar o transporte público em tempo real

Calcular previsões e métricas avançadas de operação

Disponibilizar indicadores confiáveis para tomada de decisão

Demonstrar domínio técnico de ponta a ponta para ambientes corporativos.



## ⚙️ Como executar o projeto (passo a passo)

### 1.Clonar o repositório
```
git clone https://github.com/xMACEDOX/Projeto_Final.git
cd Projeto_Final
```


### 2 .Configurar variáveis de ambiente

Duplicar o arquivo .env (ou criar um) e ajustar:

Credenciais do PostgreSQL

Credenciais do MinIO

Token da API Olho Vivo (SPTrans), se estiver parametrizado

Versões das imagens (MinIO, NiFi, Spark, etc.)



### 3 .Subir a infraestrutura com Docker Compose
```
docker compose up -d
```

Isso deve subir, pelo menos:

MinIO (armazenamento S3 compatível)

NiFi (ingestão de dados)

Spark (processamento)

PostgreSQL (camada Gold / Data Mart)


### 4. Importar e iniciar o fluxo no NiFi

Acessar a UI do NiFi (ex.: http://localhost:8080/nifi)

Importar o fluxo (Projeto.json)

Iniciar os processadores responsáveis por:

Autenticação na API Olho Vivo

Coleta de posições dos veículos

Ingestão dos arquivos GTFS

Escrita na camada Raw (MinIO)


### 5. Executar os notebooks Spark na ordem

Na pasta de notebooks (ou scripts):

0gtfs_silver.ipynb – trata e estrutura os arquivos GTFS na camada Silver

1Previsao_Linhas2.ipynb – calcula/organiza previsões de chegada das principais linhas

2previsao_silver.ipynb – normaliza a previsão em formato analítico

3nova_silver.ipynb – faz o enriquecimento e junções finais

4processamento_batch_gold.ipynb – grava as tabelas de KPIs na camada Gold (PostgreSQL)


### 6. Validar as tabelas no PostgreSQL

Conectar no banco e verificar se as tabelas / views de KPIs foram criadas

```
SELECT * FROM vw_kpi_dashboard LIMIT 10;
```


### 7. Abrir o dashboard no Power BI

Abrir o arquivo KPI'S.pbix

Configurar a conexão com o PostgreSQL (host, porta, database, usuário, senha)

Clicar em Atualizar para carregar os KPIs



## 🗂️ ESTRUTURA DO REPOSITÓRIO
```
.
├── docker-compose.yaml
├── .env
├── .gitignore
├── nifi/
│   └── Projeto.json
├── notebooks/
│   ├── 0gtfs_silver.ipynb
│   ├── 1Previsao_Linhas2.ipynb
│   ├── 2previsao_silver.ipynb
│   ├── 3nova_silver.ipynb
│   └── 4processamento_batch_gold.ipynb
├── powerbi/
│   └── KPI'S.pbix
└── README.md
```

## 🏆 RESULTADOS

Pipeline totalmente automatizada

KPIs estratégicos calculados

Dashboard profissional

Arquitetura replicável

Documentação completa

Demonstração clara de habilidades avançadas de engenharia de dados


# 🌐 ARQUITETURA ESCALÁVEL — PRÓXIMOS PASSOS DO PROJETO

Esta seção é para documentar como o projeto pode evoluir para uma solução corporativa e altamente escalável.
Aqui estão alguns tópicos já estruturados — você pode preencher cada um deles com seus futuros projetos..




























































































