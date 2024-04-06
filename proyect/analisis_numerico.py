# Tema 5: Aproximación de funciones por mínimos cuadrados

import numpy as np
import matplotlib.pyplot as plt

class MinimosCuadrados:
    def __init__(self):
        self.x = None
        self.y = None

    def ingresar_datos(self):
        n = int(input("Ingrese el número de puntos: "))
        self.x = np.zeros(n)
        self.y = np.zeros(n)
        
        print("Ingrese los valores de x y y:")
        
        for i in range(n):
            self.x[i] = float(input(f"x[{i+1}]: "))
            self.y[i] = float(input(f"y[{i+1}]: "))


    def ajuste_lineal(self):
        if self.x is None or self.y is None:
            print("Primero debe ingresar los datos.")
            return

        # Calculamos la matriz de diseño
        X = np.vstack([np.ones_like(self.x), self.x]).T

        # Calculamos los coeficientes del modelo lineal por mínimos cuadrados
        theta = np.linalg.lstsq(X, self.y, rcond=None)[0]

        # Imprimimos la ecuación de la línea
        print(f"La ecuación de la línea es y = {theta[1]}x + {theta[0]}")

        # Generamos la recta ajustada
        x_fit = np.linspace(min(self.x), max(self.x), 100)
        y_fit = theta[0] + theta[1] * x_fit

        # Creamos la cadena de texto con la ecuación de la línea
        equation = f"y = {theta[1]:.2f}x + {theta[0]:.2f}"


        # Graficamos los datos y la recta ajustada
        plt.text(1, 1, equation, transform=plt.gca().transAxes, fontsize=14, horizontalalignment='right')
        plt.scatter(self.x, self.y, label='Datos')
        plt.plot(x_fit, y_fit, 'r', label='Recta ajustada')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend()
        plt.title('Ajuste lineal por mínimos cuadrados')
        plt.grid(True)
        plt.show()


if __name__ == '__main__':
    mc = MinimosCuadrados()
    mc.ingresar_datos()
    mc.ajuste_lineal()


