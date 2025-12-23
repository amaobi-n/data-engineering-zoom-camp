import sys
import pandas as pd

month = int(sys.argv[1])

df = pd.DataFrame({"Day": [1, 2], "Num_passengers": [3, 4]})
df['month'] = month
print(df.head())
df.to_parquet(f"output_day_{sys.argv[1]}.parquet")

print(f'hello pipeline, month={month}')

