from math import sqrt


#funcion que estamos estudiando
def funcion (x) :
    result = 2 * (sqrt(1-(x**2)))
    return result

#Ejercicio 1.1

def suma_inferior(n):
    """
    Para f(x) = 2*sqrt(1-x^2), el mínimo en cada subintervalo
    está en el extremo más alejado de x=0.
    """
    a, b = -1, 1
    dx = (b - a) / (n - 1)
    suma = 0
    
    for i in range(n - 1):
        x_izq = a + i * dx
        x_der = a + (i + 1) * dx
        
        # El mínimo está en el punto más alejado de 0
        if abs(x_izq) > abs(x_der):
            min_val = funcion(x_izq)
        else:
            min_val = funcion(x_der)
        
        suma += min_val * dx
    
    return suma

def suma_superior(n):
    """
    Para f(x) = 2*sqrt(1-x^2), el máximo en cada subintervalo
    está en el punto más cercano a x=0.
    """
    a, b = -1, 1
    dx = (b - a) / (n - 1)
    suma = 0
    
    for i in range(n - 1):
        x_izq = a + i * dx
        x_der = a + (i + 1) * dx
        
        # El máximo está en el punto más cercano a 0
        # Si 0 está en el intervalo, ese es el máximo
        if x_izq <= 0 <= x_der:
            max_val = funcion(0)
        elif abs(x_izq) < abs(x_der):
            max_val = funcion(x_izq)
        else:
            max_val = funcion(x_der)
        
        suma += max_val * dx
    
    return suma

# Prueba de las funciones
if __name__ == "__main__":
    print("Convergencia de sumas inferior y superior")
    print("=" * 50)
    
    # Probamos con diferentes valores de n
    n_valores = [10, 50, 100, 500, 1000]
    
    for n in n_valores:
        inf = suma_inferior(n)
        sup = suma_superior(n)
        diferencia = sup - inf
        print(f"\nn = {n:4d}:")
        print(f"  Suma inferior:  {inf:.10f}")
        print(f"  Suma superior:  {sup:.10f}")
        print(f"  Diferencia:     {diferencia:.10f}")




