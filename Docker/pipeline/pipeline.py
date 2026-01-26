import sys
import pandas as pd


print(sys.argv)

month = sys.argv[1]

print(f'arguments == {sys.argv} month == ({month})')

df = pd.DataFrame({"days": [1, 2], "number_of_passangers": [3, 4]})
df['month'] = month
print(df.head())

df.to_parquet(f'output_{month}.parquet')