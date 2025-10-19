import math
from math import sqrt

# Función que estamos estudiando
def funcion(x):
    """
    Calcula f(x) = 2 * sqrt(1 - x^2)
    Esta función representa un semicírculo de radio 1.
    """
    result = 2 * (sqrt(1 - (x**2)))
    return result


# ============================================================================
# EJERCICIO 3: Comparación de métodos de integración numérica
# ============================================================================

def particion_equiespaciada(n):
    """
    Genera una partición equiespaciada del intervalo [-1, 1].
    (Importada de ej2.py)
    
    Parámetros:
    - n: Cantidad de puntos de la partición (incluyendo los extremos)
    
    Retorna:
    - Lista ordenada de n puntos equiespaciados en [-1, 1]
    """
    if n < 2:
        raise ValueError("n debe ser al menos 2")
    
    # El paso entre puntos consecutivos
    delta_x = 2.0 / (n - 1)  # 2.0 porque el intervalo tiene longitud 2 (de -1 a 1)
    
    # Generar los puntos
    particion = [-1.0 + i * delta_x for i in range(n)]
    
    return particion


# ============================================================================
# MÉTODOS DE INTEGRACIÓN NUMÉRICA
# ============================================================================

def metodo_rectangulos(n):
    """
    Método de rectángulos: usa el valor de la función en el extremo izquierdo
    de cada subintervalo para calcular el área.
    
    Este es el método usual de suma de Riemann con rectángulos.
    
    Parámetros:
    - n: Cantidad de puntos de la partición equiespaciada
    
    Retorna:
    - Aproximación de π usando el método de rectángulos
    """
    particion = particion_equiespaciada(n)
    suma = 0.0
    
    # Para cada subintervalo [x_i, x_{i+1}]
    for i in range(len(particion) - 1):
        x_izq = particion[i]
        x_der = particion[i + 1]
        
        dx = x_der - x_izq
        
        # Usar el extremo izquierdo para calcular la altura
        altura = funcion(x_izq)
        suma += altura * dx
    
    return suma


def metodo_trapecio(n):
    """
    Método del trapecio: en vez de áreas de rectángulos se suman áreas de
    trapecios definidos por los extremos de cada subintervalo.
    
    El área de un trapecio es: A = (base * (altura_izq + altura_der)) / 2
    
    Parámetros:
    - n: Cantidad de puntos de la partición equiespaciada
    
    Retorna:
    - Aproximación de π usando el método del trapecio
    """
    particion = particion_equiespaciada(n)
    suma = 0.0
    
    # Para cada subintervalo [x_i, x_{i+1}]
    for i in range(len(particion) - 1):
        x_izq = particion[i]
        x_der = particion[i + 1]
        
        dx = x_der - x_izq
        
        # Calcular alturas en ambos extremos
        altura_izq = funcion(x_izq)
        altura_der = funcion(x_der)
        
        # Área del trapecio = base * (altura_izq + altura_der) / 2
        area_trapecio = dx * (altura_izq + altura_der) / 2.0
        suma += area_trapecio
    
    return suma


def metodo_punto_medio(n):
    """
    Método del punto medio: evalúa la función en el centro de cada subintervalo.
    
    Este método suele dar mejores aproximaciones que el método de rectángulos
    porque el punto medio representa mejor el comportamiento promedio de la función.
    
    Parámetros:
    - n: Cantidad de puntos de la partición equiespaciada
    
    Retorna:
    - Aproximación de π usando el método del punto medio
    """
    particion = particion_equiespaciada(n)
    suma = 0.0
    
    # Para cada subintervalo [x_i, x_{i+1}]
    for i in range(len(particion) - 1):
        x_izq = particion[i]
        x_der = particion[i + 1]
        
        dx = x_der - x_izq
        
        # Usar el punto medio del subintervalo
        x_medio = (x_izq + x_der) / 2.0
        
        # Verificar que el punto medio esté en el dominio
        if -1.0 <= x_medio <= 1.0:
            altura = funcion(x_medio)
            suma += altura * dx
    
    return suma


# ============================================================================
# FUNCIÓN PRINCIPAL DE PRUEBA
# ============================================================================

if __name__ == "__main__":
    print("\n")
    print("=" * 80)
    print("EJERCICIO 3: COMPARACIÓN DE MÉTODOS DE INTEGRACIÓN NUMÉRICA")
    print("=" * 80)
    
    valor_pi = math.pi
    
    # Probar los tres métodos con diferentes valores de n
    print("\n" + "=" * 80)
    print("PRUEBA DE LOS TRES MÉTODOS CON DIFERENTES VALORES DE N")
    print("=" * 80)
    
    n_valores = [10, 50, 100, 500, 1000, 5000, 10000]
    
    print(f"\n{'N':>6} | {'Rectángulos':>15} | {'Residuo':>12} | {'Trapecio':>15} | {'Residuo':>12} | {'Pto Medio':>15} | {'Residuo':>12}")
    print("-" * 110)
    
    for n in n_valores:
        rect = metodo_rectangulos(n)
        trap = metodo_trapecio(n)
        medio = metodo_punto_medio(n)
        
        res_rect = abs(rect - valor_pi)
        res_trap = abs(trap - valor_pi)
        res_medio = abs(medio - valor_pi)
        
        print(f"{n:6d} | {rect:15.10f} | {res_rect:12.10f} | {trap:15.10f} | {res_trap:12.10f} | {medio:15.10f} | {res_medio:12.10f}")
    
    print("\n" + "=" * 80)
    print(f"Valor de π (referencia): {valor_pi:.10f}")
    print("=" * 80)

