import math
import random
import csv

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


# ============================================================================
# EJERCICIO 2.2: Cálculo de aproximaciones usando diferentes particiones
# ============================================================================

def calcular_suma_riemann(particion):
    """
    Calcula la suma de Riemann para una partición dada.
    Usa el punto medio de cada subintervalo para evaluar la función.
    
    Parámetros:
    - particion: Lista ordenada de puntos que definen la partición
    
    Retorna:
    - Valor aproximado de la integral (aproximación de π)
    """
    suma = 0.0
    
    # Para cada subintervalo [x_i, x_{i+1}]
    for i in range(len(particion) - 1):
        x_izq = particion[i]
        x_der = particion[i + 1]
        
        # Ancho del subintervalo
        dx = x_der - x_izq
        
        # Punto medio del subintervalo
        x_medio = (x_izq + x_der) / 2.0
        
        # Evaluar la función en el punto medio (evitando valores fuera del dominio)
        if -1.0 <= x_medio <= 1.0 and abs(x_medio) < 0.9999:
            altura = funcion(x_medio)
        else:
            # Si estamos muy cerca de los extremos, usar 0
            altura = 0.0
        
        # Área del rectángulo
        suma += altura * dx
    
    return suma


def aproximar_pi_con_particion(n, tipo_particion):
    """
    Aproxima el valor de π usando una partición específica.
    
    Parámetros:
    - n: Cantidad de puntos de la partición
    - tipo_particion: 'equiespaciada', 'aleatoria', o 'coseno'
    
    Retorna:
    - Aproximación de π usando la partición especificada
    """
    # Generar la partición según el tipo
    if tipo_particion == 'equiespaciada':
        particion = particion_equiespaciada(n)
    elif tipo_particion == 'aleatoria':
        particion = particion_aleatoria_uniforme(n)
    elif tipo_particion == 'coseno':
        particion = particion_coseno(n)
    else:
        raise ValueError(f"Tipo de partición desconocido: {tipo_particion}")
    
    # Calcular la suma de Riemann
    aproximacion = calcular_suma_riemann(particion)
    
    return aproximacion


def generar_tabla_comparativa_particiones(n_inicio, n_fin, incremento, numero_tabla):
    """
    Genera una tabla comparativa de las tres particiones para un rango de N.
    
    Parámetros:
    - n_inicio: Valor inicial de N
    - n_fin: Valor final de N
    - incremento: Paso entre valores consecutivos de N
    - numero_tabla: Número de la tabla para el título
    """
    valor_pi = math.pi
    
    print("\n" + "=" * 110)
    print(f"TABLA {numero_tabla}: Comparación de particiones - N variando de {n_inicio} a {n_fin} (incremento de {incremento})")
    print("=" * 110)
    print(f"{'N':>6} | {'Equiespaciada':>15} | {'Residuo':>12} | {'Aleatoria':>15} | {'Residuo':>12} | {'Coseno':>15} | {'Residuo':>12}")
    print("-" * 110)
    
    for n in range(n_inicio, n_fin + 1, incremento):
        # Calcular aproximaciones con cada tipo de partición
        aprox_equi = aproximar_pi_con_particion(n, 'equiespaciada')
        aprox_alea = aproximar_pi_con_particion(n, 'aleatoria')
        aprox_cos = aproximar_pi_con_particion(n, 'coseno')
        
        # Calcular residuos
        residuo_equi = abs(aprox_equi - valor_pi)
        residuo_alea = abs(aprox_alea - valor_pi)
        residuo_cos = abs(aprox_cos - valor_pi)
        
        print(f"{n:6d} | {aprox_equi:15.10f} | {residuo_equi:12.10f} | {aprox_alea:15.10f} | {residuo_alea:12.10f} | {aprox_cos:15.10f} | {residuo_cos:12.10f}")


def generar_tablas_comparativas_particiones():
    """
    Genera tres tablas comparativas de las particiones.
    """
    # Tabla 1: N de 10 a 100, variando de 10 en 10
    generar_tabla_comparativa_particiones(n_inicio=10, n_fin=100, incremento=10, numero_tabla=1)
    
    # Tabla 2: N de 100 a 1000, variando de 100 en 100
    generar_tabla_comparativa_particiones(n_inicio=100, n_fin=1000, incremento=100, numero_tabla=2)
    
    # Tabla 3: N de 1000 a 10000, variando de 1000 en 1000
    generar_tabla_comparativa_particiones(n_inicio=1000, n_fin=10000, incremento=1000, numero_tabla=3)
    
    # Mostrar valor de referencia de π
    print("\n" + "=" * 110)
    print(f"Valor de π (referencia): {math.pi:.10f}")
    print("=" * 110)


def generar_tabla_individual_csv_particiones(archivo_csv, n_inicio, n_fin, incremento, numero_tabla):
    """
    Genera una tabla comparativa de particiones y la escribe en un archivo CSV.
    
    Parámetros:
    - archivo_csv: Objeto writer de CSV donde escribir los datos
    - n_inicio: Valor inicial de N
    - n_fin: Valor final de N
    - incremento: Paso entre valores consecutivos de N
    - numero_tabla: Número de la tabla para identificación
    """
    valor_pi = math.pi
    
    # Escribir encabezado de la tabla
    archivo_csv.writerow([])  # Línea en blanco
    archivo_csv.writerow([f"TABLA {numero_tabla}: N variando de {n_inicio} a {n_fin} (incremento de {incremento})"])
    archivo_csv.writerow(['N', 'Equiespaciada', 'Residuo Equi', 'Aleatoria', 'Residuo Alea', 'Coseno', 'Residuo Cos'])
    
    # Calcular y escribir los datos
    for n in range(n_inicio, n_fin + 1, incremento):
        aprox_equi = aproximar_pi_con_particion(n, 'equiespaciada')
        aprox_alea = aproximar_pi_con_particion(n, 'aleatoria')
        aprox_cos = aproximar_pi_con_particion(n, 'coseno')
        
        residuo_equi = abs(aprox_equi - valor_pi)
        residuo_alea = abs(aprox_alea - valor_pi)
        residuo_cos = abs(aprox_cos - valor_pi)
        
        archivo_csv.writerow([n, aprox_equi, residuo_equi, aprox_alea, residuo_alea, aprox_cos, residuo_cos])


def generar_tablas_csv_particiones(nombre_archivo='tablas_particiones.csv'):
    """
    Genera un archivo CSV con las tres tablas comparativas de particiones.
    
    Parámetros:
    - nombre_archivo: Nombre del archivo CSV a crear
    """
    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo:
        writer = csv.writer(archivo)
        
        # Escribir encabezado general
        writer.writerow(['Tablas Comparativas - Aproximación de π usando diferentes particiones'])
        writer.writerow([f'Valor de π (referencia): {math.pi:.10f}'])
        
        # Tabla 1: N de 10 a 100, variando de 10 en 10
        generar_tabla_individual_csv_particiones(writer, n_inicio=10, n_fin=100, incremento=10, numero_tabla=1)
        
        # Tabla 2: N de 100 a 1000, variando de 100 en 100
        generar_tabla_individual_csv_particiones(writer, n_inicio=100, n_fin=1000, incremento=100, numero_tabla=2)
        
        # Tabla 3: N de 1000 a 10000, variando de 1000 en 1000
        generar_tabla_individual_csv_particiones(writer, n_inicio=1000, n_fin=10000, incremento=1000, numero_tabla=3)
    
    print(f"\n✓ Archivo CSV generado: {nombre_archivo}")


if __name__ == "__main__":
    # EJERCICIO 2.1: Probar las funciones de particiones con ejemplos
    print("\n")
    print("=" * 80)
    print("EJERCICIO 2.1: EJEMPLOS DE PARTICIONES")
    print("=" * 80)
    
    mostrar_particiones_ejemplo(10)
    mostrar_particiones_ejemplo(5)
    
    # EJERCICIO 2.2: Generar tablas comparativas de particiones
    print("\n\n")
    print("=" * 80)
    print("EJERCICIO 2.2: TABLAS COMPARATIVAS DE PARTICIONES")
    print("=" * 80)
    generar_tablas_comparativas_particiones()
    
    # Generar también archivo CSV con las tablas
    try:
        generar_tablas_csv_particiones('tablas_particiones.csv')
    except PermissionError:
        print("\n⚠ No se pudo generar el archivo CSV (el archivo puede estar abierto en otro programa)")