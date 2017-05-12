import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

rated_movies= pd.read_csv('/home/saira/Documentos/trabajospython/tareas/movies/rated_movies.csv')
#To get the top 10
count=rated_movies.groupby('title')["title"].count().reset_index(name="count")
count_sort=count.sort_values('count', ascending=False)
top10=count_sort[0:10]

Forest=rated_movies.where(rated_movies["title"]=='Forrest Gump (1994)').dropna()
Pulp=rated_movies.where(rated_movies["title"]=='Pulp Fiction (1994)').dropna()
Shawshank=rated_movies.where(rated_movies["title"]=='Shawshank Redemption, The (1994)').dropna()
Silence=rated_movies.where(rated_movies["title"]=='Silence of the Lambs, The (1991)').dropna()
Star=rated_movies.where(rated_movies["title"]=='Star Wars: Episode IV - A New Hope (1977)').dropna()

Forest['rating']=pd.to_numeric(Forest['rating'])
Pulp['rating']=pd.to_numeric(Pulp['rating'])
Shawshank['rating']=pd.to_numeric(Shawshank['rating'])
Silence['rating']=pd.to_numeric(Silence['rating'])
Star['rating']=pd.to_numeric(Star['rating'])

#To get united graph
plt.figure()
plt.hist([Forest['rating'], Pulp['rating'], Shawshank['rating'], Silence['rating'], Star['rating']], bins=np.arange(0,5+2,1), color=['green','blue','black', 'red', 'yellow'], label=['Forrest Gump', 'Pulp fiction', 'Shawshank Redemption', 'Silence of the Lambs', 'Star Wars: Episode IV - A New Hope'])
plt.title("Top 10")
plt.ylabel("Votos")
plt.legend()
plt.show()
