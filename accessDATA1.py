import pandas as pd

csv_file = "/Users/roberta/Documents/IOSDEV/PythonLab/PythonTest/testo.txt"
df_from_csv = pd.read_csv(csv_file)
#df_from_csv.info()

#d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=df_from_csv)
df

"""df_from_csv.plot(kind="scatter",x='Sale Date',
               y='Odometer (KM)',
               c='Sale Date');
df_from_csv"""