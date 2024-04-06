<h1 align="center"> TEMA 5 </h1>

#  Aproximación continua por mínimos cuadrados

<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tema 5: Aproximación Continua por Mínimos Cuadrados</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
      padding: 20px;
    }
    .math {
      display: inline-block;
      font-style: italic;
    }
  </style>
</head>
<body>
  <h2>Tema 5: Aproximación Continua por Mínimos Cuadrados</h2>
  <p>Dado un conjunto de datos <span class="math">\( (x_i, y_i) \)</span> donde <span class="math">\( i = 1, 2, ..., n \)</span>, la aproximación continua por mínimos cuadrados busca encontrar una función <span class="math">\( f(x) \)</span> que minimiza la suma de los cuadrados de las diferencias entre los valores reales <span class="math">\( y_i \)</span> y los valores predichos <span class="math">\( f(x_i) \)</span>, es decir, buscamos minimizar la función de error cuadrático medio (MSE):</p>
  <p class="math">\[ \text{MSE} = \sum_{i=1}^{n} (y_i - f(x_i))^2 \]</p>
  <p>Dependiendo del contexto y de la naturaleza de los datos, la función <span class="math">\( f(x) \)</span> puede ser una línea recta (regresión lineal), una curva de grado superior (regresión polinómica), una función exponencial, logarítmica, entre otras. La función <span class="math">\( f(x) \)</span> se encuentra ajustando los coeficientes de los términos de la función de acuerdo con los datos observados, utilizando métodos de optimización como el método de los mínimos cuadrados. Una vez que se determinan los coeficientes, la función <span class="math">\( f(x) \)</span> puede utilizarse para predecir valores de <span class="math">\( y \)</span> para nuevos valores de <span class="math">\( x \)</span> dentro del rango observado.</p>
</body>
</html>

