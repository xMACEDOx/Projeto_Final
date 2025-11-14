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

![Projeto (2)](https://github.com/user-attachments/assets/fc1373c2-0c58-4a60-a531-cbc7e7430c9a)





## 🧠 Competências Demonstradas

Arquitetura Medallion (Bronze → Silver → Gold)

Data Lake com MinIO (S3 compatível)

Ingestão automatizada com Apache NiFi

Processamento distribuído com Apache Spark (PySpark)

Orquestração e execução via Docker / Docker Compose

Modelagem analítica e camada Gold em PostgreSQL

Visualização de dados com Power BI

Manipulação de APIs (SPTrans, Open-Meteo), GTFS e dados geoespaciais

Exposição de dados e KPIs com FastAPI

Boas práticas de versionamento, modularização e organização de pipelines


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

Com a evolução natural do projeto, a arquitetura foi pensada para suportar maior volume de dados, automação completa e análises avançadas. Essa versão escalável integra novos componentes que fortalecem a robustez da pipeline, ampliam o alcance analítico e habilitam o projeto para operações em tempo quase real.


![Projeto (3)](https://github.com/user-attachments/assets/ab515503-8313-4361-a521-e8ea991aae14)


## 🚀 Orquestração Completa com Apache Airflow

O Airflow passa a ser responsável por gerenciar, agendar e monitorar toda a pipeline de dados:

Execução automática dos jobs Spark (batch ou streaming)

Dependências entre tarefas (ingestão → transformação → carga → dashboard)

Reprocessamentos e retries

Histórico de execução e visibilidade completa do fluxo

Isso transforma a solução em um sistema totalmente automatizado, confiável e pronto para operar 24/7.


## 🌦️ Ingestão Climática com Open-Meteo via Spark

Para enriquecer as análises e prever impactos no transporte público, o projeto passa a incluir uma nova ingestão:

Coleta contínua da API Open-Meteo usando Spark

Armazenamento dos dados de clima em formato bruto na camada Raw

Normalização e padronização na camada Silver

Possibilidade de gerar KPIs climáticos e correlações com atrasos de linhas

Essa integração adiciona uma dimensão importante ao projeto, permitindo análises como:

“Atraso médio por condição climática”

“Impacto de chuva/temperatura no headway”

“Regiões mais sensíveis a variações climáticas”


## 🧱 Lakehouse Moderno na Camada Silver

Na arquitetura escalável, a camada Silver passa a operar como um Lakehouse, unificando:

Formatos colunares de alta performance (ex.: Parquet / Delta Lake)

Versionamento de dados

Esquema organizado e padronizado

Dados prontos para analytics e ML

Isso garante:

Performance superior nas consultas

Escalabilidade horizontal

Flexibilidade para análises avançadas

Base confiável para dashboards e modelos preditivos


## ⚙️ Spark como Motor Central de Processamento

O Apache Spark é o núcleo de processamento da solução, responsável por:

Ingestão dos dados da SPTrans e Open-Meteo

Limpeza, transformação e enriquecimento

Junções entre clima × previsões × posições × GTFS

Escrita das tabelas Gold no PostgreSQL

Suporte a workflows batch e near real-time

Graças à orquestração do Airflow, todo o pipeline Spark é executado em ciclos automatizados, garantindo dados atualizados continuamente.


## 📊 Dashboards Inteligentes (Power BI)

Com uma arquitetura mais poderosa, os dashboards passam a refletir:

Desempenho operacional das linhas

Previsões de chegada atualizadas

Tempo médio entre chegadas

Atrasos por faixa horária ou região

Alertas baseados em condições climáticas




























































































