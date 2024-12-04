# -*- coding: utf-8 -*-
"""Proyecto_ANEMIA.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1eiS5m8EfEOwOwH5mHyjH2sFsvHc9hTuT

#**Predicción de la Tasa de Recuperación de Niños Menores de 36 Meses con Anemia en la Región Junín mediante Modelos Probabilísticos y de Aprendizaje Supervisado**

**Objetivo:**

Desarrollar y evaluar modelos predictivos capaces de estimar la probabilidad de recuperación de niños menores de 36 meses con anemia en función de variables clínicas y demográficas, con el fin de identificar patrones clave que puedan guiar las intervenciones médicas y optimizar los recursos de salud en la región de Junín.

##**Librerias:**
"""

# Librerías de procesamiento y análisis de datos
import pandas as pd                                                             # Para la manipulación de datos en DataFrames
import numpy as np                                                              # Para operaciones numéricas
import matplotlib.pyplot as plt                                                 # Para visualización de gráficos
import seaborn as sns                                                           # Para gráficos estadísticos más avanzados
from sklearn.preprocessing import LabelEncoder                                  # Para preparar los datos
from sklearn.model_selection import train_test_split                            # Para dividir los datos en entrenamiento y prueba
from sklearn.preprocessing import StandardScaler                                # Para escalar características
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix, mean_squared_error  # Para evaluar modelos

# Modelos de machine learning
from sklearn.linear_model import LogisticRegression                             # Regresión logística
from sklearn.ensemble import RandomForestClassifier                             # Random Forest
from sklearn.neighbors import KNeighborsClassifier                              # KNN

"""##**Cargar y Pre-Procesar los Datos:**
Cargar el dataset, explorar los primeros registros y realizar un preprocesamiento básico, como manejar valores faltantes, convertir columnas de fechas y transformar variables si es necesario.
"""

# Cargar el dataset
df = pd.read_csv("/content/dataset_ANEMIA.csv")


# Lista de columnas de tipo fecha
fecha_columns = ['fecha_nac', 'fecha_dx', 'fecha_dosaje_dx', 'fecha_dosaje_mes',
                 'fecha_dosaje_3_meses', 'fecha_dosaje_6_meses', 'fecha_recup',
                 'fecha_supT1', 'fecha_supT2', 'fecha_supT3', 'fecha_supT4',
                 'fecha_supT5', 'fecha_supT6', 'fecha_ta']

# Convertir las columnas de fecha a tipo datetime con dayfirst=True para manejar el formato dd/mm/yyyy
for fecha_col in fecha_columns:
    df[fecha_col] = pd.to_datetime(df[fecha_col], errors='coerce', dayfirst=True)

# Para cada columna de fecha, rellenamos los valores nulos con la fecha máxima
for fecha_col in fecha_columns:
    fecha_maxima = df[fecha_col].max()  # Obtenemos la fecha máxima de la columna
    df[fecha_col] = df[fecha_col].fillna(fecha_maxima)

# Lista de columnas numéricas
numeric_columns = ['hb_dx', 'hb', 'hb_tresmeses', 'hb_seismeses']

# Para cada columna numérica, rellenamos los valores nulos con la media de la columna
for col in numeric_columns:
    df[col] = df[col].fillna(df[col].mean())  # Asignamos el valor de la media a la columna

# Mostramos el DataFrame modificado
print(df.head())

"""##**Preparar los Datos para el Modelado**
Este paso es importante para estructurar los datos de manera que el modelo pueda aprender correctamente. Debemos separar las características (X) y la variable objetivo (y) para poder entrenar los modelos.
"""

# Seleccionar características relevantes para la predicción
features = ['valor_lab_dx', 'hb_dx', 'hb', 'hb_tresmeses', 'hb_seismeses', 'seguro']
target = 'recup'  # Variable objetivo

# Separar las características (X) y la variable objetivo (y)
X = df[features]
y = df[target]

# Convertir las columnas categóricas a numéricas (por ejemplo, 'valor_lab_dx')
le = LabelEncoder()
X.loc[:, 'valor_lab_dx'] = le.fit_transform(X['valor_lab_dx'])

# Dividir los datos en conjunto de entrenamiento y conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Escalar las características
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

"""##**Entrenar el Modelo de Regresión Logística**
La regresión logística es un modelo de clasificación que predice la probabilidad de una clase. Se usa para predecir una variable categórica o binaria (por ejemplo, si un paciente tiene una enfermedad o no, si un correo electrónico es spam o no).
"""

# Entrenar el modelo de regresión logística
log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)

# Hacer predicciones sobre el conjunto de prueba
y_pred_log_reg = log_reg.predict(X_test)

# Evaluar el modelo
print("Regresión Logística - Precisión:", accuracy_score(y_test, y_pred_log_reg))

"""##**Entrenar el Modelo de Random Forest**
Random Forest es un modelo de aprendizaje supervisado basado en árboles de decisión. Es muy eficiente para manejar datos con relaciones no lineales y es robusto frente a sobreajuste.
"""

# Entrenar el modelo de Random Forest
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Hacer predicciones sobre el conjunto de prueba
y_pred_rf = rf.predict(X_test)

# Evaluar el modelo
print("Random Forest - Precisión:", accuracy_score(y_test, y_pred_rf))

"""##**Entrenar el Modelo K-Nearest Neighbors (KNN)**
El modelo KNN (K-Vecinos más Cercanos) predice el valor de una observación según los valores de sus vecinos más cercanos. Es otro enfoque para la predicción.
"""

# Entrenar el modelo de KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Hacer predicciones sobre el conjunto de prueba
y_pred_knn = knn.predict(X_test)

# Evaluar el modelo
print("KNN - Precisión:", accuracy_score(y_test, y_pred_knn))

"""##**Comparar los Modelos**
 comparar los modelos para ver cuál tiene el mejor desempeño en términos de precisión.
"""

# Comparar los modelos en términos de precisión
accuracies = {
    'Logística': accuracy_score(y_test, y_pred_log_reg),
    'Random Forest': accuracy_score(y_test, y_pred_rf),
    'KNN': accuracy_score(y_test, y_pred_knn)
}

# Crear gráfico de barras para comparación
plt.figure(figsize=(8, 6))
plt.bar(accuracies.keys(), accuracies.values(), color=['blue', 'green', 'red'])
plt.title('Comparación de Modelos')
plt.xlabel('Modelo')
plt.ylabel('Precisión')
plt.show()

"""##**Evaluación de los modelos**

"""

# Evaluación del modelo de Regresión Logistica
y_pred_lr = log_reg.predict(X_test)
r2_lr = log_reg.score(X_test, y_test)
rmse_lr = np.sqrt(mean_squared_error(y_test, y_pred_lr))

print(f"Regresión Logistica - R^2: \t{r2_lr}")
print(f"Regresión Logistica - RMSE: \t{rmse_lr}")

# Evaluación del modelo Random Forest
y_pred_rf = rf.predict(X_test)
r2_rf = rf.score(X_test, y_test)
rmse_rf = np.sqrt(mean_squared_error(y_test, y_pred_rf))

print(f"Random Forest - R^2: \t\t{r2_rf}")
print(f"Random Forest - RMSE: \t\t{rmse_rf}")

# Evaluación del modelo KNN
y_pred_knn = knn.predict(X_test)
r2_knn = knn.score(X_test, y_test)
rmse_knn = np.sqrt(mean_squared_error(y_test, y_pred_knn))

print(f"KNN - R^2: \t\t\t{r2_knn}")
print(f"KNN - RMSE: \t\t\t{rmse_knn}")

"""###**Interpretación:**

1.   Regresión Logística
  *   R² (0.5438): Un valor de R² de aproximadamente 0.54 indica que el modelo puede explicar el 54.38% de la variabilidad de los datos. Esto sugiere que la regresión logística no está capturando una gran parte de la variabilidad en los datos.
  *   RMSE (0.6754): El error cuadrático medio (RMSE) de 0.6754 muestra la magnitud del error de las predicciones en relación con los valores reales. Es relativamente alto, lo que indica que el modelo tiene un margen de error considerable.


2.   Random Forest
  *   R² (0.7840): Un valor de R² de 0.7840 es excelente, lo que indica que el modelo de Random Forest puede explicar el 78.4% de la variabilidad de los datos. Este es un buen indicador de que el modelo es adecuado para los datos.
  *   RMSE (0.4647): El RMSE de 0.4647 es el más bajo entre los modelos evaluados, lo que indica que Random Forest tiene un mejor rendimiento en términos de precisión de las predicciones y un menor error en comparación con los otros modelos.


3.   KNN
  *   R² (0.7608): Un valor de R² de 0.7608 es también muy bueno, indicando que el modelo puede explicar el 76.08% de la variabilidad en los datos. Es muy cercano al de Random Forest, pero aún algo por debajo.
  *   RMSE (0.4891): El RMSE de 0.4891 es mayor que el de Random Forest, lo que sugiere que, aunque KNN es un modelo eficaz, sus predicciones tienen un margen de error mayor que las de Random Forest.

###**Visualización:**
"""

# Datos de los modelos
modelos = ['Regresión Logística', 'Random Forest', 'KNN']
r2_scores = [r2_lr, r2_rf, r2_knn]
rmse_scores = [rmse_lr, rmse_rf, rmse_knn]

# Crear gráfico combinado
fig, ax1 = plt.subplots(figsize=(10, 6))

# Gráfico de barras para R^2
ax1.bar(modelos, r2_scores, color='skyblue', label='R^2')
ax1.set_ylabel('R^2', fontsize=12, color='blue')
ax1.set_ylim(0, 1)
ax1.set_xlabel('Modelo', fontsize=12)
ax1.set_title('Comparación Combinada: R^2 y RMSE', fontsize=14)

# Añadir RMSE en el mismo gráfico
ax2 = ax1.twinx()
ax2.plot(modelos, rmse_scores, color='salmon', marker='o', label='RMSE', linewidth=2)
ax2.set_ylabel('RMSE', fontsize=12, color='red')

# Añadir leyendas y mostrar
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9), fontsize=12)
plt.show()

"""###**Análisis:**

*   **Regresión Logística:** Aunque es un modelo muy utilizado y fácil de interpretar, en este caso no parece ser el más adecuado. Su R² de 0.5438 es relativamente bajo, lo que indica que no captura bien la variabilidad de los datos. Además, su RMSE es más alto en comparación con los otros modelos, lo que significa que tiene un mayor margen de error en sus predicciones.

*   **Random Forest:** Este modelo ha demostrado ser el más fuerte en este caso, con un R² de 0.7840, lo que indica que es capaz de explicar una gran parte de la variabilidad de los datos. También tiene el RMSE más bajo, lo que significa que tiene las predicciones más precisas y consistentes entre los modelos evaluados. Random Forest es robusto y maneja muy bien tanto las relaciones no lineales como las interacciones complejas entre las características.

*   **KNN:** Aunque también es un modelo sólido con un buen R² (0.7608), su RMSE es ligeramente superior al de Random Forest, lo que indica que tiene un margen de error más grande. Sin embargo, KNN sigue siendo una opción competitiva en términos de capacidad de explicación de los datos y rendimiento en general.

###**Conclusión:**

Después de evaluar los tres modelos, Random Forest ha demostrado ser el modelo más prometedor, con el mejor rendimiento en cuanto a R² y RMSE. Su R² de 0.78 indica que puede capturar una cantidad significativa de la variabilidad en los datos, lo que sugiere que es capaz de generalizar bien. Comparado con la Regresión Logística (R² de 0.54) y KNN (R² de 0.76), Random Forest ha superado a los otros dos modelos en cuanto a precisión y capacidad de predicción.

Aunque el modelo de Random Forest no es perfecto, su rendimiento es sólido y su RMSE de 0.46 es relativamente bajo, lo que sugiere que las predicciones son bastante precisas. En comparación, la Regresión Logística y KNN muestran un desempeño inferior, con KNN superando a la regresión logística, pero aún lejos de los resultados de Random Forest.

Por lo tanto, se recomienda continuar con el modelo de Random Forest y considerar el ajuste de sus hiperparámetros si se desea una mejora adicional. Aunque el modelo ya ofrece buenos resultados, una optimización fina podría mejorar aún más su desempeño, pero es importante mantener un equilibrio para evitar el sobreajuste.

###Código para el ajuste de hiperparámetros
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, classification_report

# Definir el modelo Random Forest
rf = RandomForestClassifier(random_state=42)

# Definir el espacio de hiperparámetros a explorar
param_grid_rf = {
    'n_estimators': [50, 100, 200],  # Número de árboles en el bosque
    'max_depth': [None, 10, 20],  # Profundidad máxima de los árboles
    'min_samples_split': [2, 5],  # Número mínimo de muestras necesarias para dividir un nodo
    'min_samples_leaf': [1, 2],  # Número mínimo de muestras en una hoja
    'max_features': ['auto', 'sqrt', 'log2']  # Número de características a considerar
}

# Crear el objeto GridSearchCV
grid_search_rf = GridSearchCV(estimator=rf, param_grid=param_grid_rf, cv=5, scoring='accuracy')

# Ajustar el modelo
grid_search_rf.fit(X_train, y_train)

# Ver los mejores hiperparámetros y el rendimiento
print("Mejores hiperparámetros:", grid_search_rf.best_params_)
print("Mejor puntuación de validación cruzada:", grid_search_rf.best_score_)

# Predecir con el mejor modelo encontrado
y_pred_rf = grid_search_rf.best_estimator_.predict(X_test)

# Evaluar el modelo
print("Random Forest - Accuracy:", accuracy_score(y_test, y_pred_rf))
print("Random Forest - Reporte de clasificación:\n", classification_report(y_test, y_pred_rf))