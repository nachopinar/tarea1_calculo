import math
import random

# Función que estamos estudiando
def funcion(x):
    """
    Calcula f(x) = 2 * sqrt(1 - x^2)
    Esta función representa un semicírculo de radio 1.
    """
    result = 2 * (math.sqrt(1 - (x**2)))
    return result

# ============================================================================
# EJERCICIO 2.1: Funciones para generar particiones
# ============================================================================

def particion_equiespaciada(n):
    """
    Genera una partición equiespaciada del intervalo [-1, 1].
    
    Parámetros:
    - n: Cantidad de puntos de la partición (incluyendo los extremos)
    
    Retorna:
    - Lista ordenada de n puntos equiespaciados en [-1, 1]
    
    Ejemplo:
    - n=5 genera: [-1.0, -0.5, 0.0, 0.5, 1.0]
    """
    if n < 2:
        raise ValueError("n debe ser al menos 2 para incluir los extremos")
    
    # El paso entre puntos consecutivos
    delta_x = 2.0 / (n - 1)  # 2.0 porque el intervalo tiene longitud 2 (de -1 a 1)
    
    # Generar los puntos
    particion = [-1.0 + i * delta_x for i in range(n)]
    
    return particion


def particion_aleatoria_uniforme(n):
    """
    Genera una partición aleatoria uniforme del intervalo [-1, 1].
    Los puntos se generan aleatoriamente y luego se ordenan.
    Siempre incluye los extremos -1 y 1.
    
    Parámetros:
    - n: Cantidad de puntos de la partición (incluyendo los extremos)
    
    Retorna:
    - Lista ordenada de n puntos aleatorios en [-1, 1]
    
    Nota:
    - Usa random.uniform() para generar números reales uniformemente distribuidos
    """
    if n < 2:
        raise ValueError("n debe ser al menos 2 para incluir los extremos")
    
    # Generar n-2 puntos aleatorios en el interior del intervalo
    puntos_interiores = [random.uniform(-1.0, 1.0) for _ in range(n - 2)]
    
    # Agregar los extremos y ordenar
    particion = [-1.0] + puntos_interiores + [1.0]
    particion.sort()
    
    return particion


def particion_coseno(n):
    """
    Genera una partición usando la función coseno: xi = cos(i*π/N).
    Esta partición tiene más puntos concentrados cerca de los extremos.
    
    Parámetros:
    - n: Cantidad de puntos de la partición (tamaño N)
    
    Retorna:
    - Lista ordenada de n puntos generados con xi = cos(i*π/N) para i = 0, 1, ..., n-1
    
    Nota:
    - Esta partición es útil para interpolación de Chebyshev
    - Los puntos están más concentrados cerca de x = -1 y x = 1
    """
    if n < 1:
        raise ValueError("n debe ser al menos 1")
    
    # Generar los puntos usando la fórmula xi = cos(i*π/N)
    particion = [math.cos(i * math.pi / n) for i in range(n + 1)]
    
    # Ordenar de menor a mayor (cos genera puntos en orden decreciente)
    particion.sort()
    
    return particion


# ============================================================================
# Función de prueba para visualizar las particiones
# ============================================================================

def mostrar_particiones_ejemplo(n=10):
    """
    Muestra ejemplos de las tres particiones para un valor de n dado.
    """
    print("\n" + "=" * 80)
    print(f"EJEMPLOS DE PARTICIONES CON N = {n}")
    print("=" * 80)
    
    # Partición equiespaciada
    print(f"\n1. PARTICIÓN EQUIESPACIADA:")
    print("-" * 80)
    equi = particion_equiespaciada(n)
    print(f"Puntos: {[f'{x:.6f}' for x in equi]}")
    print(f"Cantidad de puntos: {len(equi)}")
    
    # Partición aleatoria
    print(f"\n2. PARTICIÓN ALEATORIA UNIFORME:")
    print("-" * 80)
    alea = particion_aleatoria_uniforme(n)
    print(f"Puntos: {[f'{x:.6f}' for x in alea]}")
    print(f"Cantidad de puntos: {len(alea)}")
    
    # Partición coseno
    print(f"\n3. PARTICIÓN COSENO xi = cos(i*π/N):")
    print("-" * 80)
    cos = particion_coseno(n)
    print(f"Puntos: {[f'{x:.6f}' for x in cos]}")
    print(f"Cantidad de puntos: {len(cos)}")
    
    print("\n" + "=" * 80)


if __name__ == "__main__":
    # Probar las funciones con un ejemplo
    mostrar_particiones_ejemplo(10)
    
    # Mostrar otro ejemplo con menos puntos para ver mejor
    mostrar_particiones_ejemplo(5)