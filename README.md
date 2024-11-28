<h1>Predicción de la Tasa de Recuperación de Niños Menores de 36 Meses con Anemia en la Región Junín mediante Modelos Probabilísticos y de Aprendizaje Supervisado</h1>
<p>
Este repositorio contiene un proyecto de análisis y predicción de la tasa de recuperación de niños menores de 36 meses diagnosticados con anemia en la Región Junín, utilizando técnicas de aprendizaje supervisado y modelos probabilísticos. La anemia infantil es un problema de salud pública que afecta a muchos niños en diversas regiones del Perú, y su diagnóstico temprano y tratamiento adecuado son cruciales para prevenir complicaciones. Este proyecto busca explorar factores como los niveles de hemoglobina, el tipo de seguro, las fechas de diagnóstico y tratamiento, entre otros, para predecir la probabilidad de recuperación de los niños y así mejorar las estrategias de intervención médica.
</p>

<h3>Objetivo: </h3>
<p>
Desarrollar y evaluar modelos predictivos capaces de estimar la probabilidad de recuperación de niños menores de 36 meses con anemia en función de variables clínicas y demográficas, con el fin de identificar patrones clave que puedan guiar las intervenciones médicas y optimizar los recursos de salud en la región.
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
      <li>Regresión Logística</li>
      <li>Random Forest</li>
      <li>K-Nearest Neighbors (KNN)</li>
   </ul>
</p>

<h2>Resultados:</h2>
<p>
Regresión Logistica - R^2: 	0.5437800320341698 <br>
Regresión Logistica - RMSE: 	0.675440573230414 <br>
Random Forest - R^2: 		0.7840363053924185 <br>
Random Forest - RMSE: 		0.4647189415201208 <br>
KNN - R^2: 			0.7608115323011212 <br>
KNN - RMSE: 			0.489068980511828 <br>
</p>
<h3>Interpretación: </h3>
<p>
   <ol>
      <li>Regresión Logística</li>
         <ul>
            <li>
               R² (0.5438): Un valor de R² de aproximadamente 0.54 indica que el modelo puede explicar el 54.38% de la variabilidad de los datos. Esto sugiere que la regresión logística no está capturando una gran parte de la variabilidad en los datos.
            </li>  
            <li>
               RMSE (0.6754): El error cuadrático medio (RMSE) de 0.6754 muestra la magnitud del error de las predicciones en relación con los valores reales. Es relativamente alto, lo que indica que el modelo tiene un margen de error considerable.
            </li>
         </ul>
      <li>Random Forest</li>
         <ul>
            <li>
               R² (0.7840): Un valor de R² de 0.7840 es excelente, lo que indica que el modelo de Random Forest puede explicar el 78.4% de la variabilidad de los datos. Este es un buen indicador de que el modelo es adecuado para los datos.
            </li>
            <li>
               RMSE (0.4647): El RMSE de 0.4647 es el más bajo entre los modelos evaluados, lo que indica que Random Forest tiene un mejor rendimiento en términos de precisión de las predicciones y un menor error en comparación con los otros modelos.
            </li>
         </ul>
      <li>KNN</li>
         <ul>
            <li>
               R² (0.7608): Un valor de R² de 0.7608 es también muy bueno, indicando que el modelo puede explicar el 76.08% de la variabilidad en los datos. Es muy cercano al de Random Forest, pero aún algo por debajo.
            </li>
            <li>
               RMSE (0.4891): El RMSE de 0.4891 es mayor que el de Random Forest, lo que sugiere que, aunque KNN es un modelo eficaz, sus predicciones tienen un margen de error mayor que las de Random Forest.
            </li>
         </ul>
   </ol>
</p>
<h3>Análisis</h3>
<p>
   <ul>
      <li>
         Regresión Logística: Aunque es un modelo muy utilizado y fácil de interpretar, en este caso no parece ser el más adecuado. Su R² de 0.5438 es relativamente bajo, lo que indica que no captura bien la variabilidad de los datos. Además, su RMSE es más alto en comparación con los otros modelos, lo que significa que tiene un mayor margen de error en sus predicciones.
      </li>
      <li>
         Random Forest: Este modelo ha demostrado ser el más fuerte en este caso, con un R² de 0.7840, lo que indica que es capaz de explicar una gran parte de la variabilidad de los datos. También tiene el RMSE más bajo, lo que significa que tiene las predicciones más precisas y consistentes entre los modelos evaluados. Random Forest es robusto y maneja muy bien tanto las relaciones no lineales como las interacciones complejas entre las características.
      </li>
      <li>
         KNN: Aunque también es un modelo sólido con un buen R² (0.7608), su RMSE es ligeramente superior al de Random Forest, lo que indica que tiene un margen de error más grande. Sin embargo, KNN sigue siendo una opción competitiva en términos de capacidad de explicación de los datos y rendimiento en general.
      </li>
   </ul>
</p>
<h3>Conclusión</h3>
<p>
   Después de evaluar los tres modelos, Random Forest ha demostrado ser el modelo más prometedor, con el mejor rendimiento en cuanto a R² y RMSE. Su R² de 0.78 indica que puede capturar una cantidad significativa de la variabilidad en los datos, lo que sugiere que es capaz de generalizar bien. Comparado con la Regresión Logística (R² de 0.54) y KNN (R² de 0.76), Random Forest ha superado a los otros dos modelos en cuanto a precisión y capacidad de predicción.
<br>
Aunque el modelo de Random Forest no es perfecto, su rendimiento es sólido y su RMSE de 0.46 es relativamente bajo, lo que sugiere que las predicciones son bastante precisas. En comparación, la Regresión Logística y KNN muestran un desempeño inferior, con KNN superando a la regresión logística, pero aún lejos de los resultados de Random Forest.
<br>
Por lo tanto, se recomienda continuar con el modelo de Random Forest y considerar el ajuste de sus hiperparámetros si se desea una mejora adicional. Aunque el modelo ya ofrece buenos resultados, una optimización fina podría mejorar aún más su desempeño, pero es importante mantener un equilibrio para evitar el sobreajuste.
</p>



