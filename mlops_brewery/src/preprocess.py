from pyspark.sql import SparkSession
from pyspark.sql.functions import when
import pandas as pd

spark = SparkSession.builder \
    .appName("BreweryPreprocess") \
    .getOrCreate()

# Ler Parquet
df = spark.read.parquet("data/breweries_raw_parquet")

# Selecionar colunas
df = df.select("brewery_type", "city", "state", "country")

# Remover nulos
df = df.dropna()

# Criar target
df = df.withColumn(
    "is_micro",
    when(df.brewery_type == "micro", 1).otherwise(0)
)

# Converter para Pandas (dataset pequeno)
pdf = df.toPandas()

pdf.to_csv("data/breweries_processed.csv", index=False)

print("Preprocessamento concluído e salvo para ML")

spark.stop()
