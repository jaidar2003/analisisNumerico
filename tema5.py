# Tema 5: Aproximación de funciones por mínimos cuadrados

class AnalsisNumerico:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.n = len(x)
        self.x_sum = sum(x)
        self.y_sum = sum(y)
        self.x2_sum = sum([i**2 for i in x])
        self.xy_sum = sum([x[i]*y[i] for i in range(self.n)])
        self.a = (self.n*self.xy_sum - self.x_sum*self.y_sum)/(self.n*self.x2_sum - self.x_sum**2)
        self.b = (self.x2_sum*self.y_sum - self.x_sum*self.xy_sum)/(self.n*self.x2_sum - self.x_sum**2)

    def __str__(self):
        return f"y = {self.a}x + {self.b}"

    def evaluar(self, x):
        return self.a*x + self.b

    def error(self):
        return sum([(self.y[i] - self.evaluar(self.x[i]))**2 for i in range(self.n)])

