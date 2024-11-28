<h1>Predicción de Casos Confirmados de Dengue en el Perú mediante Modelos Probabilísticos y de Aprendizaje Supervisado</h1>
<p>
Este repositorio contiene un proyecto de análisis y predicción de la notificación de casos confirmados de dengue en el Perú, utilizando técnicas de aprendizaje supervisado y modelos probabilísticos. El dengue es una enfermedad viral transmitida por mosquitos, con alta incidencia en diversas regiones del Perú, y constituye un problema de salud pública. Este proyecto busca explorar factores geográficos, demográficos y temporales asociados a la notificación de casos, para anticipar brotes y mejorar las estrategias de control y prevención.
</p>

<h3>Objetivo: </h3>
<p>
Desarrollar y evaluar modelos predictivos robustos que permitan estimar la probabilidad de casos confirmados de dengue en función de variables geográficas, demográficas y temporales, con el objetivo de identificar patrones clave que puedan guiar intervenciones de salud pública.
</p>
<h3>Integrantes: </h3>
<p>
   <ul>
      <li>Barrientos Huillca, Oscar David</li>
      <li>Cancinas Cardenas, Denis Jair</li>
      <li>Quispe Castillo, Brayan Rodrigo</li>
   </ul>
</p>
<h3>Algoritmos utilizados: </h3>
<p>
   <ul>
      <li>Random Forest</li>
      <li>Regresión Lineal</li>
      <li>K-Nearest Neighbors (KNN)</li>
   </ul>
</p>

<h2>Resultados:</h2>
<p>
Random Forest - R^2:         &nbsp;0.511889502464703 <br>
Random Forest - RMSE:        &nbsp;6.023673560949253 <br>
Regresión Lineal - R^2:      &nbsp;0.0029446936190182793 <br>
Regresión Lineal - RMSE:     &nbsp;8.609183781870966 <br>
KNN - R^2:                   &nbsp;-0.10963266365699997 <br>
KNN - RMSE:                  &nbsp;&nbsp;&nbsp;&nbsp;9.082219012818523 <br>
</p>
<h3>Interpretación: </h3>
<p>
   <ol>
      <li>Random Forest</li>
         <ul>
            <li>
               R²: 0.5119: Este valor indica que el modelo Random Forest explica aproximadamente el 51.19% de la variabilidad de los datos. Aunque no es excelente, está funcionando razonablemente bien, ya que un R² cercano a 1 indica una muy buena predicción, y valores cercanos a 0 indican un mal desempeño.
            </li>  
            <li>
               RMSE: 6.02: Este valor nos da la magnitud del error promedio entre las predicciones y los valores reales. En este caso, el error promedio es de aproximadamente 6.02 unidades. Un RMSE bajo indica que el modelo está haciendo buenas predicciones en comparación con los valores reales.
            </li>
         </ul>
      <li>Regresión Lineal</li>
         <ul>
            <li>
               R²: 0.0029: Este valor indica que el modelo de regresión lineal apenas explica el 0.29% de la variabilidad de los datos, lo que significa que el modelo no está ajustando bien los datos. Este es un indicador claro de que la regresión lineal no es adecuada para este conjunto de datos o para el tipo de relación que existe entre las variables.
            </li>
            <li>
               RMSE: 8.61: El error promedio es de 8.61 unidades, lo que indica que las predicciones del modelo son menos precisas que las de Random Forest.
            </li>
         </ul>
      <li>KNN</li>
         <ul>
            <li>
               R²: -0.1096: Un valor negativo de R² significa que el modelo KNN está realizando predicciones peores que simplemente predecir la media de los valores. Este es un mal resultado, ya que sugiere que el modelo está sobreajustando o no está capturando la relación en los datos.
            </li>
            <li>
               RMSE: 9.08: Este es el mayor valor de RMSE de los tres modelos, lo que confirma que las predicciones del modelo KNN son las menos precisas.
            </li>
         </ul>
   </ol>
</p>
<h3>Análisis</h3>
<p>
   <ul>
      <li>
         Random Forest está funcionando mejor que los otros dos modelos, aunque aún se puede mejorar. Tiene un R² decente y el RMSE más bajo, lo que indica que tiene un buen rendimiento general en este conjunto de datos.
      </li>
      <li>
         Regresión Lineal está teniendo un desempeño muy pobre. El valor de R² es muy bajo, lo que sugiere que la relación entre las variables es más compleja y no puede ser modelada adecuadamente con una simple regresión lineal.
      </li>
      <li>
         KNN** también está teniendo un desempeño negativo (R² negativo), lo que sugiere que este modelo no está funcionando bien para el conjunto de datos. El valor de RMSE más alto también lo confirma.
      </li>
   </ul>
</p>
<h3>Conclusión</h3>
<p>
   Después de evaluar los tres modelos, Random Forest ha demostrado ser el modelo más prometedor, con un rendimiento razonable en cuanto a R² y RMSE. Aunque no es perfecto, su R² de 0.51 indica que puede capturar una cantidad significativa de la variabilidad en los datos. En comparación, tanto la Regresión Lineal como KNN no han logrado generar buenos resultados, con valores negativos de R² y altos valores de RMSE, lo que sugiere que no son adecuados para este conjunto de datos.
<br>
Dado el rendimiento positivo de Random Forest, se recomienda proceder con el ajuste de sus hiperparámetros utilizando técnicas como GridSearchCV. Esta estrategia permitirá explorar de manera eficiente un espacio de hiperparámetros más amplio sin caer en un sobreajuste. Si bien un ajuste más fino puede mejorar aún más el rendimiento, es crucial encontrar un equilibrio entre la mejora de los hiperparámetros y la evitación del sobreajuste, asegurándose de que el modelo generalice bien a nuevos datos. Un ajuste excesivo puede llevar a un modelo que se adapta demasiado a las particularidades del conjunto de entrenamiento, comprometiendo su capacidad para predecir en situaciones reales.
</p>



