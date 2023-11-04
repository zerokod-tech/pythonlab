import pandas as pd


results = []


with open('/Users/roberta/Documents/IOSDEV/PythonLab/PythonTest/testo3.txt') as f:
    for line in f:
        print(line.strip().split("\n"))
        # a = line.strip().split("/n")
        results.append(line.strip().split(","))


df_from_textfile = pd.DataFrame(results,  columns=["Item", "Quantity"])
df_from_textfile
