<h1>Predicción de la Puntuación APGAR en Recién Nacidos mediante Aprendizaje Automático</h1>
<p>
Este repositorio contiene un proyecto de análisis y predicción de la puntuación APGAR en recién nacidos, utilizando técnicas de aprendizaje automático. La puntuación APGAR es un indicador clave de la salud del bebé inmediatamente después del nacimiento, evaluándose en función de cinco criterios: apariencia, pulso, gesticulación, actividad y respiración. Este proyecto tiene como objetivo identificar los factores maternos, del embarazo y del parto que pueden influir en la puntuación APGAR, para anticipar riesgos y mejorar la atención perinatal.
</p>

<h3>Objetivo: </h3>
<p>
Desarrollar y evaluar modelos predictivos robustos para predecir la puntuación APGAR, identificando factores clave que puedan ayudar en la intervención temprana en el contexto perinatal.
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
<p>
   Este proyecto combina un enfoque de análisis exploratorio de datos y modelado predictivo utilizando estos tres algoritmos, con el objetivo de construir un sistema confiable para predecir el riesgo en la puntuación APGAR de los recién nacidos.
</p>
<h3>Pasos: </h3>
<p>Instalar: <i>pip install pandas numpy scikit-learn matplotlib seaborn</i></p>
<br>
<h2>Resultados:</h2>
<p>
Random Forest - R^2:         0.511889502464703 <br>
Random Forest - RMSE:        6.023673560949253 <br>
Regresión Lineal - R^2:      0.0029446936190182793 <br>
Regresión Lineal - RMSE:     8.609183781870966 <br>
KNN - R^2:                   -0.10963266365699997 <br>
KNN - RMSE:                  9.082219012818523 <br>
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



