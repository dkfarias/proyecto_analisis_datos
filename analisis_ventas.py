

import pandas as pd
import matplotlib.pyplot as plt
#cargar datos cvs
df = pd.read_csv('ventas_productos.csv')
#mostrar los primeros productos
print(df.head ())
#calcular el precio total de cada producto
def calcular_precio_total(Precio, Cantidad):
    return Precio * Cantidad
#aplicar funcion al data frame
df['Precio Total'] = df.apply(lambda row: calcular_precio_total(row['Precio'], row['Cantidad']), axis=1)
#mostrar los primeros productos
print(df.head())
#crear grafico de barras
plt.bar(df['Producto'], df['Precio Total'])
plt.xlabel('Producto')
plt.ylabel('Precio Total')
plt.title('Precio Total de Productos')
plt.show()

"""[enlace a github](https://github.com/dkfarias/proyecto_analisis_datos.git)"""
