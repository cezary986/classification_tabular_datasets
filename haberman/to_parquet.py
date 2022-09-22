import pandas as pd

pd.read_csv('./haberman.csv').to_parquet('./haberman.parquet')

print(pd.read_parquet('./haberman.parquet').columns)