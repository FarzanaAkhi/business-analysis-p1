#Statistics: Mean

from sympy import symbols, Sum, IndexedBase
from sympy.abc import i, n

# Define an indexed variable
x = IndexedBase('x')

# Define the expression for mean
expr = Sum(x[i], (i, 1, n)) / n

print(expr)

'''#The variables are as follows:

Team

League

Year

Runs Scored (RS)

Runs Allowed (RA)

Wins (W)

On-Base Percentage (OBP)

Slugging Percentage (SLG)

Batting Average (BA)

Playoffs (binary)

RankSeason

RankPlayoffs

Games Played (G)

Opponent On-Base Percentage (OOBP)

Opponent Slugging Percentage (OSLG)'''

import pandas as pd
data = pd.read_csv("C:\\Users\\Farzana Saif\\Downloads\\archive\\baseball.csv")
print (data)

#Simplest mean : Mean of any column

mean_RS= data['RS'].mean()
print(mean_RS)

#Or##

data.RS.mean()

#Mean : Mean of any column by any team

data.loc[data.Team == "ARI"]
data.loc[data.Team == "ARI"].RS.mean()

#Mean : Mean of any column by any team of any specific year

data.loc[(data.Team == "ARI") & (data.Year > 2009)].RS.mean()
data.loc[(data.Team == "ARI") & (data.Year.isin([2005, 2007, 2009]))].RS.mean()
data.loc[(data.Team == "ARI") & (data.Year.isin([2005, 2007, 2009]))]
data.loc[data.Team == "ARI"].sort_values(by="RS", ascending=False).iloc[0]
data.loc[data.Team == "ARI"].groupby("Year")["RS"].mean()
mean_rs = data.loc[data.Team == "ARI"].groupby("Year")["RS"].mean()
max_mean_year = mean_rs.idxmax()
print("Year:", max_mean_year, "Mean RS:", mean_rs[max_mean_year])




