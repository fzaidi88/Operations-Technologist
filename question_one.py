import quandl
# quandl.ApiConfig.api_key = '9--DbGHJvpBvyg4z6k8T
import pandas as pd
import csv

file_name='/Users/fzaidi/Desktop/stock.csv'
VZ = quandl.get("SSE/BAC", start_date="2017-04-10", end_date="2018-04-10", api_key="9--DbGHJvpBvyg4z6k8T")
VZ= pd.DataFrame(VZ)
VZ['vz_avg']=VZ[['High', 'Low']].mean(axis=1)
VZ=VZ[['High', 'Low', 'vz_avg']]
VZ.columns=['VZHigh', 'VZLow', 'vz_avg']
print(VZ)


T = quandl.get("SSE/TM5", start_date="2017-04-10", end_date="2018-04-10", api_key="9--DbGHJvpBvyg4z6k8T")
T= pd.DataFrame(T)
T['t_avg']=T[['High', 'Low']].mean(axis=1)
T=T[['High', 'Low', 't_avg']]
T.columns=['THigh', 'TLow', 't_avg']
print(T)

Difference_df =pd.concat([VZ,T], axis=1)
Difference_df["difference"] = Difference_df["vz_avg"] - Difference_df["t_avg"]
Difference_df=Difference_df[['vz_avg','t_avg','difference']]
print(Difference_df)

df = Difference_df.to_csv(path_or_buf=file_name, sep=',', index=True)

