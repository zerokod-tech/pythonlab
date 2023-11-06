import pandas as pd
import sqlite3 as sql
conn = sql.connect('/Users/johnreid/Downloads/chinook.db')
# First pattern - turn query directly into dataframe:
df1 = pd.read_sql_query("SELECT * FROM invoice", conn)
# Second pattern - get row-level data, but no column names
cur = conn.cursor()
results = cur.execute("SELECT * FROM invoice LIMIT 5").fetchall()
df2 = pd.DataFrame(results)
