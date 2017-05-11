import pandas as pd
import numpy as numpy
import matplotlib.pyplot as plt
import csv

#Jalamos nuestro dataset desde la dirección donde se encuentra
prueba= pd.read_csv('/home/saira/Documentos/trabajospython/tareas/movies/final.csv')
#Seseleccionan los atributos con los que vamos a trabajar
ratings = prueba[['rating', 'title']]
#Se realiza un count conforme a los titulos, despues se crea un idex en donde su nombre va a ser frecuencia
rag = ratings.groupby('rating')['rating'].count().reset_index(name="frecuencia")
conjuntos = rag.sort_values('frecuencia', ascending=False)
top10 = conjuntos[0:10]
print(top10)

plt.figure()
plt.bar(range(len(top10)), top10['frecuencia'])
plt.xticks(range(len(top10)), top10['rating'], rotation=90, size=10)
plt.title("Top 10")
plt.ylabel("Calificaciones")
plt.xlabel("Movies")
plt.tight_layout()
plt.show()
