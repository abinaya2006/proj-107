import pandas as pd
import plotly_express as px

df=pd.read_csv("data.csv")
print(df.groupby(["student_id","level"],as_index=False)["attempt"].mean())
mean_value=df.groupby(["student_id","level"],as_index=False)["attempt"].mean()


fig=px.scatter(mean_value,x="student_id",y="level",size="attempt",color="attempt")
fig.show()