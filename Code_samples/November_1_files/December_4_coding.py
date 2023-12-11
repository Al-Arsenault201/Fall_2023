import pandas as pd

data = pd.read_csv("/Users/alfredarsenault/Downloads/1976-2020-president.csv")

#print(data)

data.sort_values("state", axis=0, ascending=True,
                 inplace=True, na_position='last')

#print(data)
rslt_df = data.loc[(data['state'] == "MARYLAND") & (data['year']== 1980) ]

print('\nResult dataframe :\n', rslt_df)