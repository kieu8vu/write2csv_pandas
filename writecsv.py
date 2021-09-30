import pandas as pd
data={"country":["Belgium", "India", "Brazil"],
	"Capital":["Brussels","Newdehi","Brassilia"],
	"Population":["11190846","1303171035","207847528"]
	}
df=pd.DataFrame(data,
	columns=["country","Capital","Population"])
print(df)
df.to_csv("df.csv")