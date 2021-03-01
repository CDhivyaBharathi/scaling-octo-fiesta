import pandas as pd 
import csv 
import plotly_express as px

df = pd.read_csv("p107Data.csv") 
mean = df.groupby("level")["attempt"].mean()


print(mean)

fig = px.scatter(mean, x= mean , y="attempt" ,color='attempt',
                   size_max=60)
fig.show()