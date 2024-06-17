import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import pandas as pd

# Cargar el dataset iris
iris = load_iris()
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df['species'] = iris.target

# Gráfico 1: Relación entre Longitud y Anchura del Sépalo
plt.figure(figsize=(10, 6))
sns.scatterplot(x=iris_df['sepal length (cm)'], y=iris_df['sepal width (cm)'], hue=iris_df['species'], palette='viridis')
plt.title('Relación entre Longitud y Anchura del Sépalo')
plt.xlabel('Longitud del Sépalo (cm)')
plt.ylabel('Anchura del Sépalo (cm)')
plt.show()

# Gráfico 2: Relación entre Longitud del Sépalo y Longitud del Pétalo
plt.figure(figsize=(10, 6))
sns.scatterplot(x=iris_df['sepal length (cm)'], y=iris_df['petal length (cm)'], hue=iris_df['species'], palette='coolwarm')
plt.title('Relación entre Longitud del Sépalo y Longitud del Pétalo')
plt.xlabel('Longitud del Sépalo (cm)')
plt.ylabel('Longitud del Pétalo (cm)')
plt.show()

# Cargar el dataset mtcars (seaborn dataset)
mtcars = sns.load_dataset('mpg').dropna()

# Gráfico 3: Promedio de MPG por Número de Cilindros
plt.figure(figsize=(10, 6))
sns.barplot(x='cylinders', y='mpg', data=mtcars, estimator='mean', ci=None, palette='Blues_d')
plt.title('Promedio de MPG por Número de Cilindros')
plt.xlabel('Número de Cilindros')
plt.ylabel('Promedio de MPG')
plt.show()

# Gráfico 4: Cuenta de Automóviles por Región de Origen
plt.figure(figsize=(10, 6))
sns.countplot(x='origin', data=mtcars, palette='Set2')
plt.title('Cuenta de Automóviles por Región de Origen')
plt.xlabel('Región de Origen')
plt.ylabel('Cuenta')
plt.show()

# Gráfico 5: Relación entre Peso y MPG
plt.figure(figsize=(10, 6))
sns.scatterplot(x='weight', y='mpg', data=mtcars, hue='origin', palette='deep')
plt.title('Relación entre Peso y MPG')
plt.xlabel('Peso del Vehículo')
plt.ylabel('MPG')
plt.show()
