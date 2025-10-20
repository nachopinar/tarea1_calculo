import math
import random
import csv
import matplotlib.pyplot as plt
import numpy as np

# Función que estamos estudiando
def funcion(x):
    """
    Calcula f(x) = 2 * sqrt(1 - x^2)
    Esta función representa un semicírculo de radio 1.
    """
    result = 2 * (math.sqrt(1 - (x**2)))
    return result


# ============================================================================
# EJERCICIO 4 (BONUS): Integración Monte Carlo
# ============================================================================

def metodo_montecarlo(n):
    """
    Método de Monte Carlo para aproximar la integral de f(x) = 2*sqrt(1-x²) en [-1, 1].
    
    El método consiste en:
    1. Generar n puntos aleatorios (x, y) en el rectángulo [-1, 1] × [0, 2]
    2. Contar cuántos puntos caen debajo de la curva f(x)
    3. Estimar el área como: (puntos_debajo / n_total) × área_rectángulo
    
    Parámetros:
    - n: Cantidad de puntos aleatorios a generar
    
    Retorna:
    - Aproximación de π usando el método de Monte Carlo
    """
    puntos_debajo = 0
    
    # Generar n puntos aleatorios
    for _ in range(n):
        # Generar coordenadas aleatorias en el rectángulo [-1, 1] × [0, 2]
        x = random.uniform(-1.0, 1.0)
        y = random.uniform(0.0, 2.0)
        
        # Verificar si el punto está en el dominio de la función
        if -1.0 < x < 1.0:
            # Calcular el valor de la función en x
            f_x = funcion(x)
            
            # Verificar si el punto (x, y) está debajo de la curva
            if y <= f_x:
                puntos_debajo += 1
    
    # El área del rectángulo es base × altura = 2 × 2 = 4
    area_rectangulo = 2.0 * 2.0
    
    # Estimar el área bajo la curva
    area_estimada = (puntos_debajo / n) * area_rectangulo
    
    return area_estimada


# ============================================================================
# EJERCICIO 4.2: Tablas comparativas del método Monte Carlo
# ============================================================================

def generar_tabla_comparativa_montecarlo(n_inicio, n_fin, incremento, numero_tabla, repeticiones=5):
    """
    Genera una tabla comparativa del método Monte Carlo para un rango específico de N.
    Como Monte Carlo es aleatorio, se ejecuta varias veces y se muestra el promedio.
    
    Parámetros:
    - n_inicio: Valor inicial de N
    - n_fin: Valor final de N
    - incremento: Paso entre valores consecutivos de N
    - numero_tabla: Número de la tabla para el título
    - repeticiones: Número de veces que se ejecuta Monte Carlo para cada N (para promediar)
    """
    valor_pi = math.pi
    
    print("\n" + "=" * 100)
    print(f"TABLA {numero_tabla}: Método Monte Carlo - N variando de {n_inicio} a {n_fin} (incremento de {incremento})")
    print(f"(Promedio de {repeticiones} ejecuciones por cada N)")
    print("=" * 100)
    print(f"{'N':>8} | {'Aproximación':>15} | {'Residuo':>12} | {'Desv. Est.':>12}")
    print("-" * 100)
    
    for n in range(n_inicio, n_fin + 1, incremento):
        # Ejecutar Monte Carlo varias veces para cada N
        aproximaciones = [metodo_montecarlo(n) for _ in range(repeticiones)]
        
        # Calcular promedio y desviación estándar
        aprox_promedio = sum(aproximaciones) / repeticiones
        desv_est = math.sqrt(sum((x - aprox_promedio)**2 for x in aproximaciones) / repeticiones)
        
        # Calcular residuo
        residuo = abs(aprox_promedio - valor_pi)
        
        print(f"{n:8d} | {aprox_promedio:15.10f} | {residuo:12.10f} | {desv_est:12.10f}")


def generar_tablas_comparativas_montecarlo():
    """
    Genera tres tablas comparativas del método Monte Carlo.
    """
    # Tabla 1: N de 10 a 100, variando de 10 en 10
    generar_tabla_comparativa_montecarlo(n_inicio=10, n_fin=100, incremento=10, numero_tabla=1, repeticiones=10)
    
    # Tabla 2: N de 100 a 1000, variando de 100 en 100
    generar_tabla_comparativa_montecarlo(n_inicio=100, n_fin=1000, incremento=100, numero_tabla=2, repeticiones=10)
    
    # Tabla 3: N de 1000 a 10000, variando de 1000 en 1000
    generar_tabla_comparativa_montecarlo(n_inicio=1000, n_fin=10000, incremento=1000, numero_tabla=3, repeticiones=5)
    
    # Mostrar valor de referencia de π
    print("\n" + "=" * 100)
    print(f"Valor de π (referencia): {math.pi:.10f}")
    print("=" * 100)


def generar_tabla_individual_csv_montecarlo(archivo_csv, n_inicio, n_fin, incremento, numero_tabla, repeticiones=5):
    """
    Genera una tabla comparativa del método Monte Carlo y la escribe en un archivo CSV.
    
    Parámetros:
    - archivo_csv: Objeto writer de CSV donde escribir los datos
    - n_inicio: Valor inicial de N
    - n_fin: Valor final de N
    - incremento: Paso entre valores consecutivos de N
    - numero_tabla: Número de la tabla para identificación
    - repeticiones: Número de veces que se ejecuta Monte Carlo para cada N
    """
    valor_pi = math.pi
    
    # Escribir encabezado de la tabla
    archivo_csv.writerow([])  # Línea en blanco
    archivo_csv.writerow([f"TABLA {numero_tabla}: N variando de {n_inicio} a {n_fin} (incremento de {incremento})"])
    archivo_csv.writerow([f"Promedio de {repeticiones} ejecuciones por cada N"])
    archivo_csv.writerow(['N', 'Aproximación Monte Carlo', 'Residuo', 'Desviación Estándar'])
    
    # Calcular y escribir los datos
    for n in range(n_inicio, n_fin + 1, incremento):
        # Ejecutar Monte Carlo varias veces
        aproximaciones = [metodo_montecarlo(n) for _ in range(repeticiones)]
        
        # Calcular estadísticas
        aprox_promedio = sum(aproximaciones) / repeticiones
        desv_est = math.sqrt(sum((x - aprox_promedio)**2 for x in aproximaciones) / repeticiones)
        residuo = abs(aprox_promedio - valor_pi)
        
        archivo_csv.writerow([n, aprox_promedio, residuo, desv_est])


def generar_tablas_csv_montecarlo(nombre_archivo='tablas_montecarlo.csv'):
    """
    Genera un archivo CSV con las tres tablas comparativas del método Monte Carlo.
    
    Parámetros:
    - nombre_archivo: Nombre del archivo CSV a crear
    """
    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo:
        writer = csv.writer(archivo)
        
        # Escribir encabezado general
        writer.writerow(['Tablas Comparativas - Método de Integración Monte Carlo'])
        writer.writerow([f'Valor de π (referencia): {math.pi:.10f}'])
        
        # Tabla 1: N de 10 a 100, variando de 10 en 10
        generar_tabla_individual_csv_montecarlo(writer, n_inicio=10, n_fin=100, incremento=10, numero_tabla=1, repeticiones=10)
        
        # Tabla 2: N de 100 a 1000, variando de 100 en 100
        generar_tabla_individual_csv_montecarlo(writer, n_inicio=100, n_fin=1000, incremento=100, numero_tabla=2, repeticiones=10)
        
        # Tabla 3: N de 1000 a 10000, variando de 1000 en 1000
        generar_tabla_individual_csv_montecarlo(writer, n_inicio=1000, n_fin=10000, incremento=1000, numero_tabla=3, repeticiones=5)
    
    print(f"\n✓ Archivo CSV generado: {nombre_archivo}")


# ============================================================================
# EJERCICIO 4.3: Gráficas de convergencia del método Monte Carlo
# ============================================================================

def graficar_convergencia_montecarlo():
    """
    Genera gráficas mostrando la convergencia del método Monte Carlo hacia π.
    Crea gráficas separadas para diferentes rangos de N.
    Como Monte Carlo es aleatorio, se ejecuta varias veces y se grafica el promedio.
    """
    valor_pi = math.pi
    
    # Configuración general de estilo
    plt.style.use('seaborn-v0_8-darkgrid')
    
    repeticiones = 10  # Número de ejecuciones para promediar
    
    # Gráfica 1: N de 10 a 100, variando de 10 en 10
    print("\nGenerando gráficas de convergencia del método Monte Carlo...")
    n_valores_1 = list(range(10, 101, 10))
    aprox_mc_1 = []
    desv_mc_1 = []
    
    for n in n_valores_1:
        aproximaciones = [metodo_montecarlo(n) for _ in range(repeticiones)]
        promedio = sum(aproximaciones) / repeticiones
        desv = math.sqrt(sum((x - promedio)**2 for x in aproximaciones) / repeticiones)
        aprox_mc_1.append(promedio)
        desv_mc_1.append(desv)
    
    pi_valores_1 = [valor_pi] * len(n_valores_1)
    
    plt.figure(figsize=(10, 6))
    plt.errorbar(n_valores_1, aprox_mc_1, yerr=desv_mc_1, fmt='b-o', 
                 label='Monte Carlo (promedio)', linewidth=2, markersize=6, 
                 capsize=5, capthick=2, elinewidth=1.5, alpha=0.7)
    plt.plot(n_valores_1, pi_valores_1, 'g--', label='π (teórico)', linewidth=2.5)
    plt.xlabel('N (cantidad de puntos aleatorios)', fontsize=12)
    plt.ylabel('Valor de la aproximación', fontsize=12)
    plt.title('Convergencia del método Monte Carlo hacia π\n(N = 10 a 100)', fontsize=14, fontweight='bold')
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('grafica_montecarlo_10_100.png', dpi=300)
    print("✓ Gráfica guardada: grafica_montecarlo_10_100.png")
    
    # Gráfica 2: N de 100 a 1000, variando de 100 en 100
    n_valores_2 = list(range(100, 1001, 100))
    aprox_mc_2 = []
    desv_mc_2 = []
    
    for n in n_valores_2:
        aproximaciones = [metodo_montecarlo(n) for _ in range(repeticiones)]
        promedio = sum(aproximaciones) / repeticiones
        desv = math.sqrt(sum((x - promedio)**2 for x in aproximaciones) / repeticiones)
        aprox_mc_2.append(promedio)
        desv_mc_2.append(desv)
    
    pi_valores_2 = [valor_pi] * len(n_valores_2)
    
    plt.figure(figsize=(10, 6))
    plt.errorbar(n_valores_2, aprox_mc_2, yerr=desv_mc_2, fmt='b-o', 
                 label='Monte Carlo (promedio)', linewidth=2, markersize=6, 
                 capsize=5, capthick=2, elinewidth=1.5, alpha=0.7)
    plt.plot(n_valores_2, pi_valores_2, 'g--', label='π (teórico)', linewidth=2.5)
    plt.xlabel('N (cantidad de puntos aleatorios)', fontsize=12)
    plt.ylabel('Valor de la aproximación', fontsize=12)
    plt.title('Convergencia del método Monte Carlo hacia π\n(N = 100 a 1000)', fontsize=14, fontweight='bold')
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('grafica_montecarlo_100_1000.png', dpi=300)
    print("✓ Gráfica guardada: grafica_montecarlo_100_1000.png")
    
    # Gráfica 3: N de 1000 a 10000, variando de 1000 en 1000
    n_valores_3 = list(range(1000, 10001, 1000))
    aprox_mc_3 = []
    desv_mc_3 = []
    
    repeticiones_3 = 5  # Menos repeticiones para valores grandes de N (más rápido)
    
    for n in n_valores_3:
        aproximaciones = [metodo_montecarlo(n) for _ in range(repeticiones_3)]
        promedio = sum(aproximaciones) / repeticiones_3
        desv = math.sqrt(sum((x - promedio)**2 for x in aproximaciones) / repeticiones_3)
        aprox_mc_3.append(promedio)
        desv_mc_3.append(desv)
    
    pi_valores_3 = [valor_pi] * len(n_valores_3)
    
    plt.figure(figsize=(10, 6))
    plt.errorbar(n_valores_3, aprox_mc_3, yerr=desv_mc_3, fmt='b-o', 
                 label='Monte Carlo (promedio)', linewidth=2, markersize=6, 
                 capsize=5, capthick=2, elinewidth=1.5, alpha=0.7)
    plt.plot(n_valores_3, pi_valores_3, 'g--', label='π (teórico)', linewidth=2.5)
    plt.xlabel('N (cantidad de puntos aleatorios)', fontsize=12)
    plt.ylabel('Valor de la aproximación', fontsize=12)
    plt.title('Convergencia del método Monte Carlo hacia π\n(N = 1000 a 10000)', fontsize=14, fontweight='bold')
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('grafica_montecarlo_1000_10000.png', dpi=300)
    print("✓ Gráfica guardada: grafica_montecarlo_1000_10000.png")
    
    # Gráfica 4: Visión completa con todos los valores
    n_valores_todos = n_valores_1 + n_valores_2 + n_valores_3
    aprox_mc_todos = aprox_mc_1 + aprox_mc_2 + aprox_mc_3
    desv_mc_todos = desv_mc_1 + desv_mc_2 + desv_mc_3
    pi_valores_todos = [valor_pi] * len(n_valores_todos)
    
    plt.figure(figsize=(12, 7))
    plt.errorbar(n_valores_todos, aprox_mc_todos, yerr=desv_mc_todos, fmt='b-o', 
                 label='Monte Carlo (promedio)', linewidth=2, markersize=4, 
                 capsize=4, capthick=1.5, elinewidth=1, alpha=0.7)
    plt.plot(n_valores_todos, pi_valores_todos, 'g--', label='π (teórico)', linewidth=2.5)
    plt.xlabel('N (cantidad de puntos aleatorios)', fontsize=12)
    plt.ylabel('Valor de la aproximación', fontsize=12)
    plt.title('Convergencia del método Monte Carlo hacia π\n(Visión completa: N = 10 a 10000)', fontsize=14, fontweight='bold')
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('grafica_montecarlo_completa.png', dpi=300)
    print("✓ Gráfica guardada: grafica_montecarlo_completa.png")
    
    # Gráfica 5: Zoom en rango pequeño (10 a 50)
    n_valores_zoom = list(range(10, 51, 5))
    aprox_mc_zoom = []
    desv_mc_zoom = []
    
    for n in n_valores_zoom:
        aproximaciones = [metodo_montecarlo(n) for _ in range(repeticiones)]
        promedio = sum(aproximaciones) / repeticiones
        desv = math.sqrt(sum((x - promedio)**2 for x in aproximaciones) / repeticiones)
        aprox_mc_zoom.append(promedio)
        desv_mc_zoom.append(desv)
    
    pi_valores_zoom = [valor_pi] * len(n_valores_zoom)
    
    plt.figure(figsize=(10, 6))
    plt.errorbar(n_valores_zoom, aprox_mc_zoom, yerr=desv_mc_zoom, fmt='b-o', 
                 label='Monte Carlo (promedio)', linewidth=2, markersize=7, 
                 capsize=5, capthick=2, elinewidth=1.5, alpha=0.7)
    plt.plot(n_valores_zoom, pi_valores_zoom, 'g--', label='π (teórico)', linewidth=2.5)
    plt.xlabel('N (cantidad de puntos aleatorios)', fontsize=12)
    plt.ylabel('Valor de la aproximación', fontsize=12)
    plt.title('Convergencia del método Monte Carlo hacia π\n(Zoom: N = 10 a 50, para observar comportamiento inicial)', fontsize=14, fontweight='bold')
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('grafica_montecarlo_zoom_10_50.png', dpi=300)
    print("✓ Gráfica guardada: grafica_montecarlo_zoom_10_50.png")
    
    # Gráfica 6: Gráfica de residuos (errores) - escala logarítmica
    residuos_mc = [abs(aprox - valor_pi) for aprox in aprox_mc_todos]
    
    plt.figure(figsize=(12, 7))
    plt.semilogy(n_valores_todos, residuos_mc, 'b-o', label='Monte Carlo', 
                 linewidth=2, markersize=4, alpha=0.7)
    plt.xlabel('N (cantidad de puntos aleatorios)', fontsize=12)
    plt.ylabel('Residuo (error) - Escala logarítmica', fontsize=12)
    plt.title('Evolución del residuo |aproximación - π| con Monte Carlo\n(Escala logarítmica)', fontsize=14, fontweight='bold')
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3, which='both')
    plt.tight_layout()
    plt.savefig('grafica_residuos_montecarlo.png', dpi=300)
    print("✓ Gráfica guardada: grafica_residuos_montecarlo.png")
    
    print("\n" + "=" * 70)
    print("Todas las gráficas han sido generadas exitosamente")
    print("=" * 70)


def visualizar_montecarlo(n=1000, seed=42):
    """
    Visualiza el método Monte Carlo mostrando los puntos generados.
    Los puntos debajo de la curva se muestran en verde, los de arriba en rojo.
    
    Parámetros:
    - n: Cantidad de puntos aleatorios a generar
    - seed: Semilla para reproducibilidad
    """
    print(f"\nGenerando visualización del método Monte Carlo (N={n})...")
    
    # Fijar semilla para reproducibilidad
    random.seed(seed)
    
    # Generar puntos aleatorios y clasificarlos
    x_dentro = []
    y_dentro = []
    x_fuera = []
    y_fuera = []
    
    for _ in range(n):
        x = random.uniform(-1.0, 1.0)
        y = random.uniform(0.0, 2.0)
        
        if -1.0 < x < 1.0:
            f_x = funcion(x)
            if y <= f_x:
                x_dentro.append(x)
                y_dentro.append(y)
            else:
                x_fuera.append(x)
                y_fuera.append(y)
    
    # Graficar la función continua
    x_continuo = np.linspace(-1, 1, 1000)
    y_continuo = [funcion(x) for x in x_continuo]
    
    plt.figure(figsize=(12, 8))
    
    # Dibujar puntos
    plt.scatter(x_dentro, y_dentro, c='green', s=1, alpha=0.5, label='Puntos debajo de la curva')
    plt.scatter(x_fuera, y_fuera, c='red', s=1, alpha=0.5, label='Puntos fuera de la curva')
    
    # Dibujar la curva
    plt.plot(x_continuo, y_continuo, 'b-', linewidth=3, label='f(x) = 2√(1-x²)', zorder=3)
    
    # Dibujar el rectángulo de muestreo
    rect_x = [-1, 1, 1, -1, -1]
    rect_y = [0, 0, 2, 2, 0]
    plt.plot(rect_x, rect_y, 'k--', linewidth=2, label='Rectángulo de muestreo', alpha=0.7)
    
    # Calcular aproximación
    puntos_dentro = len(x_dentro)
    aproximacion = (puntos_dentro / n) * 4.0
    
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.title(f'Visualización del Método Monte Carlo (N={n} puntos)\n' + 
              f'Puntos dentro: {puntos_dentro} | Aproximación: π ≈ {aproximacion:.6f}', 
              fontsize=14, fontweight='bold')
    plt.legend(fontsize=10, loc='upper right')
    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    plt.tight_layout()
    
    nombre_archivo = f'grafica_visualizacion_montecarlo_n{n}.png'
    plt.savefig(nombre_archivo, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Gráfica guardada: {nombre_archivo}")
    
    # Restaurar el generador aleatorio
    random.seed()


# ============================================================================
# FUNCIÓN PRINCIPAL DE PRUEBA
# ============================================================================

if __name__ == "__main__":
    # EJERCICIO 4.1: Prueba inicial del método Monte Carlo
    print("\n")
    print("=" * 80)
    print("EJERCICIO 4 (BONUS): INTEGRACIÓN MONTE CARLO")
    print("=" * 80)
    
    valor_pi = math.pi
    
    # Probar el método Monte Carlo con diferentes valores de n
    print("\n" + "=" * 80)
    print("PRUEBA DEL MÉTODO MONTE CARLO CON DIFERENTES VALORES DE N")
    print("(Promedio de 10 ejecuciones)")
    print("=" * 80)
    
    n_valores = [10, 50, 100, 500, 1000, 5000, 10000]
    repeticiones = 10
    
    print(f"\n{'N':>6} | {'Aproximación':>15} | {'Residuo':>12} | {'Desv. Est.':>12}")
    print("-" * 60)
    
    for n in n_valores:
        aproximaciones = [metodo_montecarlo(n) for _ in range(repeticiones)]
        promedio = sum(aproximaciones) / repeticiones
        desv_est = math.sqrt(sum((x - promedio)**2 for x in aproximaciones) / repeticiones)
        residuo = abs(promedio - valor_pi)
        
        print(f"{n:6d} | {promedio:15.10f} | {residuo:12.10f} | {desv_est:12.10f}")
    
    print("\n" + "=" * 80)
    print(f"Valor de π (referencia): {valor_pi:.10f}")
    print("=" * 80)
    
    # EJERCICIO 4.2: Generar tablas comparativas del método Monte Carlo
    print("\n\n")
    print("=" * 80)
    print("EJERCICIO 4.2: TABLAS COMPARATIVAS DEL MÉTODO MONTE CARLO")
    print("=" * 80)
    generar_tablas_comparativas_montecarlo()
    
    # Generar también archivo CSV con las tablas
    try:
        generar_tablas_csv_montecarlo('tablas_montecarlo.csv')
    except PermissionError:
        print("\n⚠ No se pudo generar el archivo CSV (el archivo puede estar abierto en otro programa)")
    
    # EJERCICIO 4.3: Generar gráficas de convergencia del método Monte Carlo
    print("\n\n")
    print("=" * 80)
    print("EJERCICIO 4.3: GRÁFICAS DE CONVERGENCIA DEL MÉTODO MONTE CARLO")
    print("=" * 80)
    graficar_convergencia_montecarlo()
    
    # EJERCICIO 4.4: Visualización del método Monte Carlo
    print("\n\n")
    print("=" * 80)
    print("EJERCICIO 4.4: VISUALIZACIÓN DEL MÉTODO MONTE CARLO")
    print("=" * 80)
    visualizar_montecarlo(n=1000, seed=42)
    visualizar_montecarlo(n=5000, seed=42)


