import pandas as pd 
import csv 
import plotly_express as px

df = pd.read_csv("p107Data.csv") 
mean = df.groupby(["student_id", "level"], as_index=False)["attempt"].mean() 
print(mean)
fig = px.scatter(mean, x="student_id", y="level", size="attempt", color="attempt")
fig.show()
