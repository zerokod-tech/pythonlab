import pandas as pd
import psycopg2
import config
conn = psycopg2.connect(
    host=config.host,
    database=config.database,
    user=config.user,
    password=config.password)
df1 = pd.read_sql_query("SELECT * FROM invoice", conn)
