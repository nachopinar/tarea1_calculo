import math
import csv
import matplotlib.pyplot as plt
import numpy as np
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
# EJERCICIO 3.3: Gráficas de convergencia de los métodos
# ============================================================================

def graficar_convergencia_metodos():
    """
    Genera gráficas mostrando la convergencia de los tres métodos hacia π.
    Crea gráficas separadas para diferentes rangos de N.
    """
    valor_pi = math.pi
    
    # Configuración general de estilo
    plt.style.use('seaborn-v0_8-darkgrid')
    
    # Gráfica 1: N de 10 a 100, variando de 10 en 10
    print("\nGenerando gráficas de convergencia...")
    n_valores_1 = list(range(10, 101, 10))
    aprox_rect_1 = [metodo_rectangulos(n) for n in n_valores_1]
    aprox_trap_1 = [metodo_trapecio(n) for n in n_valores_1]
    aprox_medio_1 = [metodo_punto_medio(n) for n in n_valores_1]
    pi_valores_1 = [valor_pi] * len(n_valores_1)
    
    plt.figure(figsize=(10, 6))
    plt.plot(n_valores_1, aprox_rect_1, 'b-o', label='Rectángulos', linewidth=2.5, markersize=7, alpha=0.7)
    plt.plot(n_valores_1, aprox_trap_1, 'r--s', label='Trapecio', linewidth=2, markersize=6, alpha=0.8)
    plt.plot(n_valores_1, aprox_medio_1, 'm-^', label='Punto Medio', linewidth=2, markersize=6)
    plt.plot(n_valores_1, pi_valores_1, 'g--', label='π (teórico)', linewidth=2.5)
    plt.xlabel('N (tamaño de partición)', fontsize=12)
    plt.ylabel('Valor de la aproximación', fontsize=12)
    plt.title('Convergencia de métodos de integración hacia π\n(N = 10 a 100)', fontsize=14, fontweight='bold')
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('grafica_metodos_10_100.png', dpi=300)
    print("✓ Gráfica guardada: grafica_metodos_10_100.png")
    
    # Gráfica 2: N de 100 a 1000, variando de 100 en 100
    n_valores_2 = list(range(100, 1001, 100))
    aprox_rect_2 = [metodo_rectangulos(n) for n in n_valores_2]
    aprox_trap_2 = [metodo_trapecio(n) for n in n_valores_2]
    aprox_medio_2 = [metodo_punto_medio(n) for n in n_valores_2]
    pi_valores_2 = [valor_pi] * len(n_valores_2)
    
    plt.figure(figsize=(10, 6))
    plt.plot(n_valores_2, aprox_rect_2, 'b-o', label='Rectángulos', linewidth=2.5, markersize=7, alpha=0.7)
    plt.plot(n_valores_2, aprox_trap_2, 'r--s', label='Trapecio', linewidth=2, markersize=6, alpha=0.8)
    plt.plot(n_valores_2, aprox_medio_2, 'm-^', label='Punto Medio', linewidth=2, markersize=6)
    plt.plot(n_valores_2, pi_valores_2, 'g--', label='π (teórico)', linewidth=2.5)
    plt.xlabel('N (tamaño de partición)', fontsize=12)
    plt.ylabel('Valor de la aproximación', fontsize=12)
    plt.title('Convergencia de métodos de integración hacia π\n(N = 100 a 1000)', fontsize=14, fontweight='bold')
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('grafica_metodos_100_1000.png', dpi=300)
    print("✓ Gráfica guardada: grafica_metodos_100_1000.png")
    
    # Gráfica 3: N de 1000 a 10000, variando de 1000 en 1000
    n_valores_3 = list(range(1000, 10001, 1000))
    aprox_rect_3 = [metodo_rectangulos(n) for n in n_valores_3]
    aprox_trap_3 = [metodo_trapecio(n) for n in n_valores_3]
    aprox_medio_3 = [metodo_punto_medio(n) for n in n_valores_3]
    pi_valores_3 = [valor_pi] * len(n_valores_3)
    
    plt.figure(figsize=(10, 6))
    plt.plot(n_valores_3, aprox_rect_3, 'b-o', label='Rectángulos', linewidth=2.5, markersize=7, alpha=0.7)
    plt.plot(n_valores_3, aprox_trap_3, 'r--s', label='Trapecio', linewidth=2, markersize=6, alpha=0.8)
    plt.plot(n_valores_3, aprox_medio_3, 'm-^', label='Punto Medio', linewidth=2, markersize=6)
    plt.plot(n_valores_3, pi_valores_3, 'g--', label='π (teórico)', linewidth=2.5)
    plt.xlabel('N (tamaño de partición)', fontsize=12)
    plt.ylabel('Valor de la aproximación', fontsize=12)
    plt.title('Convergencia de métodos de integración hacia π\n(N = 1000 a 10000)', fontsize=14, fontweight='bold')
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('grafica_metodos_1000_10000.png', dpi=300)
    print("✓ Gráfica guardada: grafica_metodos_1000_10000.png")
    
    # Gráfica 4: Visión completa con todos los valores
    n_valores_todos = n_valores_1 + n_valores_2 + n_valores_3
    aprox_rect_todos = aprox_rect_1 + aprox_rect_2 + aprox_rect_3
    aprox_trap_todos = aprox_trap_1 + aprox_trap_2 + aprox_trap_3
    aprox_medio_todos = aprox_medio_1 + aprox_medio_2 + aprox_medio_3
    pi_valores_todos = [valor_pi] * len(n_valores_todos)
    
    plt.figure(figsize=(12, 7))
    plt.plot(n_valores_todos, aprox_rect_todos, 'b-o', label='Rectángulos', linewidth=2.5, markersize=5, alpha=0.7)
    plt.plot(n_valores_todos, aprox_trap_todos, 'r--s', label='Trapecio', linewidth=2, markersize=4, alpha=0.8)
    plt.plot(n_valores_todos, aprox_medio_todos, 'm-^', label='Punto Medio', linewidth=2, markersize=4)
    plt.plot(n_valores_todos, pi_valores_todos, 'g--', label='π (teórico)', linewidth=2.5)
    plt.xlabel('N (tamaño de partición)', fontsize=12)
    plt.ylabel('Valor de la aproximación', fontsize=12)
    plt.title('Convergencia de métodos de integración hacia π\n(Visión completa: N = 10 a 10000)', fontsize=14, fontweight='bold')
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('grafica_metodos_completa.png', dpi=300)
    print("✓ Gráfica guardada: grafica_metodos_completa.png")
    
    # Gráfica 5: Zoom en rango pequeño (10 a 50) para ver mejor el comportamiento inicial
    n_valores_zoom = list(range(10, 51, 5))
    aprox_rect_zoom = [metodo_rectangulos(n) for n in n_valores_zoom]
    aprox_trap_zoom = [metodo_trapecio(n) for n in n_valores_zoom]
    aprox_medio_zoom = [metodo_punto_medio(n) for n in n_valores_zoom]
    pi_valores_zoom = [valor_pi] * len(n_valores_zoom)
    
    plt.figure(figsize=(10, 6))
    plt.plot(n_valores_zoom, aprox_rect_zoom, 'b-o', label='Rectángulos', linewidth=2.5, markersize=8, alpha=0.7)
    plt.plot(n_valores_zoom, aprox_trap_zoom, 'r--s', label='Trapecio', linewidth=2, markersize=7, alpha=0.8)
    plt.plot(n_valores_zoom, aprox_medio_zoom, 'm-^', label='Punto Medio', linewidth=2, markersize=7)
    plt.plot(n_valores_zoom, pi_valores_zoom, 'g--', label='π (teórico)', linewidth=2.5)
    plt.xlabel('N (tamaño de partición)', fontsize=12)
    plt.ylabel('Valor de la aproximación', fontsize=12)
    plt.title('Convergencia de métodos de integración hacia π\n(Zoom: N = 10 a 50, para observar comportamiento inicial)', fontsize=14, fontweight='bold')
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('grafica_metodos_zoom_10_50.png', dpi=300)
    print("✓ Gráfica guardada: grafica_metodos_zoom_10_50.png")
    
    # Gráfica 6: Gráfica de residuos (errores) - escala logarítmica
    residuos_rect = [abs(aprox - valor_pi) for aprox in aprox_rect_todos]
    residuos_trap = [abs(aprox - valor_pi) for aprox in aprox_trap_todos]
    residuos_medio = [abs(aprox - valor_pi) for aprox in aprox_medio_todos]
    
    plt.figure(figsize=(12, 7))
    plt.semilogy(n_valores_todos, residuos_rect, 'b-o', label='Rectángulos', linewidth=2.5, markersize=5, alpha=0.7)
    plt.semilogy(n_valores_todos, residuos_trap, 'r--s', label='Trapecio', linewidth=2, markersize=4, alpha=0.8)
    plt.semilogy(n_valores_todos, residuos_medio, 'm-^', label='Punto Medio', linewidth=2, markersize=4)
    plt.xlabel('N (tamaño de partición)', fontsize=12)
    plt.ylabel('Residuo (error) - Escala logarítmica', fontsize=12)
    plt.title('Evolución del residuo |aproximación - π| con diferentes métodos\n(Escala logarítmica)', fontsize=14, fontweight='bold')
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3, which='both')
    plt.tight_layout()
    plt.savefig('grafica_residuos_metodos.png', dpi=300)
    print("✓ Gráfica guardada: grafica_residuos_metodos.png")
    
    print("\n" + "=" * 70)
    print("Todas las gráficas han sido generadas exitosamente")
    print("=" * 70)


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
    
    # EJERCICIO 3.3: Generar gráficas de convergencia de los métodos
    print("\n\n")
    print("=" * 80)
    print("EJERCICIO 3.3: GRÁFICAS DE CONVERGENCIA DE MÉTODOS")
    print("=" * 80)
    graficar_convergencia_metodos()

