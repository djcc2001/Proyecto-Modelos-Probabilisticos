# 🩺✨ Predicción de la Tasa de Recuperación de Niños Menores de 36 Meses con Anemia en la Región Junín

Este repositorio contiene un proyecto de análisis y predicción de la tasa de recuperación de niños menores de 36 meses diagnosticados con anemia en la Región Junín, utilizando técnicas de aprendizaje supervisado y modelos probabilísticos. La anemia infantil es un problema de salud pública que afecta a muchos niños en diversas regiones del Perú. Su diagnóstico temprano y tratamiento adecuado son cruciales para prevenir complicaciones. 

El objetivo principal de este proyecto es explorar factores como los niveles de hemoglobina, el tipo de seguro, las fechas de diagnóstico y tratamiento, entre otros, para predecir la probabilidad de recuperación de los niños, mejorando así las estrategias de intervención médica.

## 🎯 Objetivo

Desarrollar y evaluar modelos predictivos que estimen la probabilidad de recuperación de niños menores de 36 meses con anemia en función de variables clínicas y demográficas. Esto permitirá identificar patrones clave para guiar las intervenciones médicas y optimizar los recursos de salud en la región.

## 👨‍💻👩‍💻 Integrantes

- **Barrientos Huillca, Oscar David**  
- **Cancinas Cardenas, Denis Jair**  
- **Quispe Castillo, Brayan Rodrigo**

## 🤖 Algoritmos Utilizados

- **📊 Regresión Logística**  
- **🌲 Random Forest**  
- **📍 K-Nearest Neighbors (KNN)**

## 📈 Resultados

| Modelo             | R²          | RMSE       |
|--------------------|-------------|------------|
| 📊 Regresión Logística | 0.5438      | 0.6754     |
| 🌲 Random Forest       | 0.7840      | 0.4647     |
| 📍 KNN                | 0.7608      | 0.4891     |

## 🔍 Interpretación de Resultados

### 📊 Regresión Logística
- **R² (0.5438):** Explica el 54.38% de la variabilidad en los datos. Esto indica que no captura una gran parte de la información.  
- **RMSE (0.6754):** Relativamente alto, lo que sugiere un margen de error considerable en las predicciones.

### 🌲 Random Forest
- **R² (0.7840):** Excelente, ya que explica el 78.4% de la variabilidad. Indica un modelo robusto y adecuado.  
- **RMSE (0.4647):** El más bajo de los modelos evaluados, mostrando alta precisión y menor error en las predicciones.

### 📍 KNN
- **R² (0.7608):** Muy bueno, explicando el 76.08% de la variabilidad. Sin embargo, está ligeramente por debajo del modelo Random Forest.  
- **RMSE (0.4891):** Aunque menor al de Regresión Logística, es superior al de Random Forest, indicando un mayor margen de error.

## 🧐 Análisis

1. **📊 Regresión Logística:**  
   Es un modelo simple y fácil de interpretar, pero su desempeño en este caso es limitado, con un R² bajo y un RMSE alto. No parece ser la mejor opción para este conjunto de datos.  

2. **🌲 Random Forest:**  
   Este modelo mostró el mejor desempeño. Su alto R² y bajo RMSE indican que captura bien la variabilidad de los datos y tiene predicciones precisas. Su capacidad para manejar relaciones no lineales y variables interdependientes lo hace ideal para este caso.  

3. **📍 KNN:**  
   Aunque competitivo, tiene un desempeño ligeramente inferior al de Random Forest. Su R² es bueno, pero su RMSE es mayor, lo que indica un margen de error más amplio.  

## ✅ Conclusión

El modelo **🌲 Random Forest** es el más prometedor para este proyecto, con un **R² de 0.7840** y un **RMSE de 0.4647**, superando a la 📊 Regresión Logística y 📍 KNN en términos de precisión y capacidad de generalización. 

Se recomienda:  
- Continuar con el uso de 🌲 Random Forest como modelo principal.  
- Ajustar los hiperparámetros del modelo para optimizar aún más su rendimiento, teniendo cuidado de evitar el sobreajuste.  

🌲 Random Forest proporciona un balance sólido entre precisión y robustez, siendo adecuado para predecir la tasa de recuperación de niños con anemia en la región.

---

✨ ¡Gracias por revisar este proyecto! Si tienes alguna pregunta o sugerencia, no dudes en abrir un **issue** o contribuir con un **pull request**.
