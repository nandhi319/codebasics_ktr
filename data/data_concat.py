import pandas as pd

pd1 = pd.read_csv('domestic_visitors/domestic_visitors_2016.csv')
pd2 = pd.read_csv('domestic_visitors/domestic_visitors_2017.csv')
pd3 = pd.read_csv('domestic_visitors/domestic_visitors_2018.csv')
pd4 = pd.read_csv('domestic_visitors/domestic_visitors_2019.csv')


finald = pd.concat([pd1, pd2, pd3, pd4], ignore_index=True)
finald.to_csv('domestic_merged.csv', index = False)
print(finald)


pd1 = pd.read_csv('foreign_visitors/foreign_visitors_2016.csv')
pd2 = pd.read_csv('foreign_visitors/foreign_visitors_2017.csv')
pd3 = pd.read_csv('foreign_visitors/foreign_visitors_2018.csv')
pd4 = pd.read_csv('foreign_visitors/foreign_visitors_2019.csv')


finalf = pd.concat([pd1, pd2, pd3, pd4], ignore_index=True)
finalf.to_csv('foreign_merged.csv', index = False)
print(finalf)