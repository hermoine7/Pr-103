import pandas as pd
import plotly_express as pe

df=pd.read_csv("CovidData.csv")
graph=pe.scatter(df, x="date",y="cases",color="country", title="Covid cases per Counrty")
graph.show()