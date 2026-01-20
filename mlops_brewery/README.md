# 🍺 MLOps Brewery Project

## 🇧🇷 Visão Geral 

Este projeto foi desenvolvido com o objetivo de **conceitos de Engenharia de Dados e MLOps**, utilizando ferramentas modernas amplamente usadas no mercado.

O pipeline realiza a **ingestão paginada de dados** da API pública **Open Brewery**, processa os dados com **PySpark**, armazena os resultados em **formato Parquet** e registra experimentos utilizando **MLflow**. Todo o ambiente é **containerizado com Docker Compose**, garantindo reprodutibilidade e facilidade de execução.

---

## 🇺🇸 Overview 

This project was created to **Data Engineering and MLOps concepts**.

The pipeline collects data from the public **Open Brewery API**. It uses **pagination** to get all data. The data is processed with **PySpark** and saved in **Parquet format**.

The project uses **Docker Compose**, so it is easy to run on any machine. **MLflow** is used to track experiments and runs.

---

## 🧱 Arquitetura do Projeto | Project Architecture

* API REST (Open Brewery)
* PySpark (Ingestão e processamento)
* Parquet (Camada de armazenamento)
* MLflow (Rastreamento de experimentos)
* Docker & Docker Compose (Ambiente)

---

## 📂 Estrutura de Pastas | Folder Structure

```
mlops_brewery/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── src/
│   ├── ingest.py          # Ingestão paginada com PySpark
│   ├── preprocess.py     # Limpeza e preparação dos dados
│   ├── train.py          # Treinamento simples de modelo
│   └── run_pipeline.py   # Orquestração do pipeline
├── data/
│   └── bronze/            # Dados brutos em Parquet
└── README.md
```

---

## ⚙️ Tecnologias Utilizadas | Technologies Used

* **Python 3.10**
* **PySpark**
* **Docker & Docker Compose**
* **MLflow**
* **Parquet**
* **Open Brewery API**

---

## ▶️ Como Executar o Projeto | How to Run the Project

### Pré-requisitos | Prerequisites

* Docker
* Docker Compose

### Passos | Steps

```bash
# Clonar o repositório
git clone <repo-url>
cd mlops_brewery

# Build e execução
docker compose build --no-cache
docker compose up
```

Após a execução:

* O pipeline será executado automaticamente
* Os dados serão salvos em Parquet
* O MLflow ficará disponível em:

👉 [http://localhost:5000](http://localhost:5000)

---

## 🧠 Principais Aprendizados | Key Learnings

### 🇧🇷 Português

* Ingestão paginada de APIs REST
* Uso do PySpark para processamento distribuído
* Resolução de problemas de schema inconsistente
* Persistência de dados em Parquet
* Containerização de pipelines de dados
* Uso do MLflow para rastreamento de experimentos

### 🇺🇸 English (Simple A2)

During data ingestion, PySpark had an error because some fields had different data types.

To fix this problem, the schema was defined manually. This made the ingestion process stable and correct.

The Java version was also updated to **OpenJDK 21** to work correctly with Spark.
