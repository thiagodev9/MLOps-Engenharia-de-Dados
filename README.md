# MLOps-Engenharia-de-Dados

## Brewery Data Pipeline (PySpark + Docker)

Pipeline de dados completo para ingestão de dados via API REST, utilizando PySpark e Docker.

### Funcionalidades
- Ingestão paginada da API Open Brewery
- Tratamento de inconsistências de schema
- Persistência em formato Parquet
- Arquitetura containerizada com Docker Compose
- Integração com MLflow para rastreabilidade

### Desafios Técnicos
- Inconsistência de tipos retornados pela API (Long, Double, null)
- Falha na inferência automática de schema do Spark

### Solução
- Definição explícita de schema com StructType
- Estratégia permissiva na camada Bronze
- Padronização para evitar falhas em produção
