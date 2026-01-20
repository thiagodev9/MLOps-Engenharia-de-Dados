import requests
from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType, StructField, StringType
)

BASE_URL = "https://api.openbrewerydb.org/v1/breweries"
PER_PAGE = 200

spark = SparkSession.builder \
    .appName("BreweryIngestionParquet") \
    .getOrCreate()

all_data = []
page = 1

print("Iniciando ingestão paginada com PySpark...")

while True:
    params = {
        "per_page": PER_PAGE,
        "page": page
    }

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()

    data = response.json()

    if not data:
        print("Fim da paginação.")
        break

    all_data.extend(data)
    print(f"Página {page} coletada com {len(data)} registros")

    page += 1

# 🔐 SCHEMA DEFINIDO EXPLICITAMENTE (EVITA ERRO)
schema = StructType([
    StructField("id", StringType(), True),
    StructField("name", StringType(), True),
    StructField("brewery_type", StringType(), True),
    StructField("city", StringType(), True),
    StructField("state", StringType(), True),
    StructField("country", StringType(), True),
])

# Criar DataFrame Spark com schema fixo
df = spark.createDataFrame(all_data, schema=schema)

# Salvar em Parquet
output_path = "data/breweries_raw_parquet"

df.write \
    .mode("overwrite") \
    .parquet(output_path)

print("Dados salvos em PARQUET com sucesso!")

spark.stop()
