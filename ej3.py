import math
import csv
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
# EJERCICIO 3.2: Tablas comparativas de los métodos
# ============================================================================

def generar_tabla_comparativa_metodos(n_inicio, n_fin, incremento, numero_tabla):
    """
    Genera una tabla comparativa de los tres métodos para un rango específico de N.
    
    Parámetros:
    - n_inicio: Valor inicial de N
    - n_fin: Valor final de N
    - incremento: Paso entre valores consecutivos de N
    - numero_tabla: Número de la tabla para el título
    """
    valor_pi = math.pi
    
    print("\n" + "=" * 120)
    print(f"TABLA {numero_tabla}: Comparación de métodos - N variando de {n_inicio} a {n_fin} (incremento de {incremento})")
    print("=" * 120)
    print(f"{'N':>6} | {'Rectángulos':>15} | {'Residuo':>12} | {'Trapecio':>15} | {'Residuo':>12} | {'Punto Medio':>15} | {'Residuo':>12}")
    print("-" * 120)
    
    for n in range(n_inicio, n_fin + 1, incremento):
        # Calcular aproximaciones con cada método
        aprox_rect = metodo_rectangulos(n)
        aprox_trap = metodo_trapecio(n)
        aprox_medio = metodo_punto_medio(n)
        
        # Calcular residuos
        residuo_rect = abs(aprox_rect - valor_pi)
        residuo_trap = abs(aprox_trap - valor_pi)
        residuo_medio = abs(aprox_medio - valor_pi)
        
        print(f"{n:6d} | {aprox_rect:15.10f} | {residuo_rect:12.10f} | {aprox_trap:15.10f} | {residuo_trap:12.10f} | {aprox_medio:15.10f} | {residuo_medio:12.10f}")


def generar_tablas_comparativas_metodos():
    """
    Genera tres tablas comparativas de los métodos de integración.
    """
    # Tabla 1: N de 10 a 100, variando de 10 en 10
    generar_tabla_comparativa_metodos(n_inicio=10, n_fin=100, incremento=10, numero_tabla=1)
    
    # Tabla 2: N de 100 a 1000, variando de 100 en 100
    generar_tabla_comparativa_metodos(n_inicio=100, n_fin=1000, incremento=100, numero_tabla=2)
    
    # Tabla 3: N de 1000 a 10000, variando de 1000 en 1000
    generar_tabla_comparativa_metodos(n_inicio=1000, n_fin=10000, incremento=1000, numero_tabla=3)
    
    # Mostrar valor de referencia de π
    print("\n" + "=" * 120)
    print(f"Valor de π (referencia): {math.pi:.10f}")
    print("=" * 120)


def generar_tabla_individual_csv_metodos(archivo_csv, n_inicio, n_fin, incremento, numero_tabla):
    """
    Genera una tabla comparativa de métodos y la escribe en un archivo CSV.
    
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
    archivo_csv.writerow(['N', 'Rectángulos', 'Residuo Rect', 'Trapecio', 'Residuo Trap', 'Punto Medio', 'Residuo Medio'])
    
    # Calcular y escribir los datos
    for n in range(n_inicio, n_fin + 1, incremento):
        aprox_rect = metodo_rectangulos(n)
        aprox_trap = metodo_trapecio(n)
        aprox_medio = metodo_punto_medio(n)
        
        residuo_rect = abs(aprox_rect - valor_pi)
        residuo_trap = abs(aprox_trap - valor_pi)
        residuo_medio = abs(aprox_medio - valor_pi)
        
        archivo_csv.writerow([n, aprox_rect, residuo_rect, aprox_trap, residuo_trap, aprox_medio, residuo_medio])


def generar_tablas_csv_metodos(nombre_archivo='tablas_metodos.csv'):
    """
    Genera un archivo CSV con las tres tablas comparativas de métodos.
    
    Parámetros:
    - nombre_archivo: Nombre del archivo CSV a crear
    """
    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo:
        writer = csv.writer(archivo)
        
        # Escribir encabezado general
        writer.writerow(['Tablas Comparativas - Métodos de Integración Numérica'])
        writer.writerow([f'Valor de π (referencia): {math.pi:.10f}'])
        
        # Tabla 1: N de 10 a 100, variando de 10 en 10
        generar_tabla_individual_csv_metodos(writer, n_inicio=10, n_fin=100, incremento=10, numero_tabla=1)
        
        # Tabla 2: N de 100 a 1000, variando de 100 en 100
        generar_tabla_individual_csv_metodos(writer, n_inicio=100, n_fin=1000, incremento=100, numero_tabla=2)
        
        # Tabla 3: N de 1000 a 10000, variando de 1000 en 1000
        generar_tabla_individual_csv_metodos(writer, n_inicio=1000, n_fin=10000, incremento=1000, numero_tabla=3)
    
    print(f"\n✓ Archivo CSV generado: {nombre_archivo}")


# ============================================================================
# FUNCIÓN PRINCIPAL DE PRUEBA
# ============================================================================

if __name__ == "__main__":
    # EJERCICIO 3.1: Prueba inicial de los tres métodos
    print("\n")
    print("=" * 80)
    print("EJERCICIO 3.1: IMPLEMENTACIÓN DE MÉTODOS DE INTEGRACIÓN NUMÉRICA")
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
    
    # EJERCICIO 3.2: Generar tablas comparativas de los métodos
    print("\n\n")
    print("=" * 80)
    print("EJERCICIO 3.2: TABLAS COMPARATIVAS DE MÉTODOS")
    print("=" * 80)
    generar_tablas_comparativas_metodos()
    
    # Generar también archivo CSV con las tablas
    try:
        generar_tablas_csv_metodos('tablas_metodos.csv')
    except PermissionError:
        print("\n⚠ No se pudo generar el archivo CSV (el archivo puede estar abierto en otro programa)")

