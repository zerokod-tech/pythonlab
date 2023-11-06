import pandas as pd
import sqlalchemy as db

engine = db.create_engine('sqlite:///chinook.db')
connection = engine.connect()
metadata = db.MetaData()
invoice = db.Table('invoice', metadata, autoload=True,
                   autoload_with=engine)
# Get the first 10 invoices from the USA
query = (db.select([invoice])
         .filter_by(billing_country='USA')
         .limit(10)
         )
df = pd.read_sql(query, engine)
