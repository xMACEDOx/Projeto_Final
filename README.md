# 🚌 Projeto SPTrans Data Pipeline

### Monitoramento em Near Real-Time do Transporte Público de São Paulo

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Apache Spark](https://img.shields.io/badge/Spark-3.3-orange)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100-green)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)
![NiFi](https://img.shields.io/badge/Apache%20NiFi-Dataflow-success)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-informational)
![MinIO](https://img.shields.io/badge/MinIO-S3%20Storage-critical)

---

## 📖 Visão Geral

Este projeto implementa um **pipeline de dados moderno e open source** para monitorar em *tempo quase real* a operação do transporte público de São Paulo, utilizando dados da **API Olho Vivo (SPTrans)** e do **GTFS (dados estáticos)**.  
A solução aplica o **modelo Medallion (Bronze, Silver, Gold)** e integra ferramentas como **NiFi, Spark, Airflow, MinIO, PostgreSQL, e FastAPI**, garantindo qualidade, rastreabilidade e automação no processamento.

---

## 🎯 Objetivos

- Coletar dados em tempo quase real (posições, linhas, paradas e previsões de chegada) por meio da API Olho Vivo.  
- Implementar arquitetura **Medalhão** para garantir governança e qualidade dos dados.  
- Armazenar e processar dados com ferramentas open source (**NiFi, Spark, MinIO, PostgreSQL,**).  
- Automatizar ingestão e transformação com **Aplicação em Spark**.  
- Criar camadas analíticas (Gold) e disponibilizar KPIs via **FastAPI**.  
- Gerar indicadores como:
  - Pontualidade das linhas  
  - Tempo médio entre chegadas  
     

---

## 🧱 Arquitetura da Solução

<img width="771" height="748" alt="Projeto drawio (1)" src="https://github.com/user-attachments/assets/842e7195-c0de-4870-8cd6-50957a0f6c57" />

## 🧩 Modelo Medalhão (Camadas)

| Camada | Descrição | Ferramentas |
|---------|------------|-------------|
| **Raw** | Dados brutos da API Olho Vivo armazenados no MinIO (JSON). | NiFi / Spark |
| **Silver** | Dados tratados e padronizados via Spark, prontos para análise. | Spark |
| **Gold** | Dados consolidados, limpos e enriquecidos com métricas e KPIs. | PostgreSQL / FastAPI |

---

## ⚙️ Ferramentas Utilizadas

| Categoria | Tecnologias |
|------------|-------------|
| Ingestão | Apache NiFi |
| Automação | Aplicação em Spark|
| Processamento | Apache Spark |
| Armazenamento | MinIO, PostgreSQL |
| KPIs | FastAPI |
| Containerização | Docker / Docker Compose |
| Linguagem | Python (PySpark, FastAPI) |

---

## 🚀 Execução Local

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/xMACEDOx/Projeto_Final.git

#Entrar na pasta
cd Projeto_Final
```
### 2️⃣ Subir o ambiente
```bash
docker-compose up -d
````
### 3️⃣ Acessar ferramentas
| Serviço     | URL                                                      | Descrição                              |
| ----------- | -------------------------------------------------------- | -------------------------------------- |
| **NiFi**    | [http://localhost:8080/nifi](http://localhost:8080/nifi) | Ingestão de dados da API Olho Vivo     |
| **MinIO**   | [http://localhost:9001](http://localhost:9001)           | Armazenamento S3 (dados Bronze/Silver) |
| **Spark**   | [http://localhost:8081](http://localhost:8889/)          | Exposição dos executores               |
| **Postgres** | [http://localhost:5433](http://localhost:5433/)         | Database com a camada gold             |
| **FastAPI** | [http://localhost:8000/docs](http://localhost:8000/docs) | Exposição de KPIs e indicadores        |




