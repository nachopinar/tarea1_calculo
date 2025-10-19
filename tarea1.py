from math import sqrt
import math
import csv


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

#Ejercicio 1.2

def generar_tabla_individual(n_inicio, n_fin, incremento, numero_tabla):
    """
    Genera una tabla comparativa individual para un rango específico de N.
    
    Parámetros:
    - n_inicio: Valor inicial de N
    - n_fin: Valor final de N (se sumará el incremento para incluirlo)
    - incremento: Paso entre valores consecutivos de N
    - numero_tabla: Número de la tabla para el título
    """
    valor_pi = math.pi
    
    print("\n" + "=" * 90)
    print(f"TABLA {numero_tabla}: N variando de {n_inicio} a {n_fin} (incremento de {incremento})")
    print("=" * 90)
    print(f"{'N':>6} | {'Suma Inferior':>15} | {'Residuo Inf':>15} | {'Suma Superior':>15} | {'Residuo Sup':>15}")
    print("-" * 90)
    
    for n in range(n_inicio, n_fin + 1, incremento):
        inf = suma_inferior(n)
        sup = suma_superior(n)
        residuo_inf = abs(inf - valor_pi)
        residuo_sup = abs(sup - valor_pi)
        print(f"{n:6d} | {inf:15.10f} | {residuo_inf:15.10f} | {sup:15.10f} | {residuo_sup:15.10f}")

def generar_tablas_comparativas():
    """
    Genera tres tablas comparativas variando el tamaño de la partición.
    Muestra la aproximación y el residuo para ambas sumas.
    """
    # Tabla 1: N de 10 a 100, variando de 10 en 10
    generar_tabla_individual(n_inicio=10, n_fin=100, incremento=10, numero_tabla=1)
    
    # Tabla 2: N de 100 a 1000, variando de 100 en 100
    generar_tabla_individual(n_inicio=100, n_fin=1000, incremento=100, numero_tabla=2)
    
    # Tabla 3: N de 1000 a 10000, variando de 1000 en 1000
    generar_tabla_individual(n_inicio=1000, n_fin=10000, incremento=1000, numero_tabla=3)
    
    # Mostrar valor de referencia de π
    print("\n" + "=" * 90)
    print(f"Valor de π (referencia): {math.pi:.10f}")
    print("=" * 90)

def generar_tabla_individual_csv(archivo_csv, n_inicio, n_fin, incremento, numero_tabla):
    """
    Genera una tabla comparativa individual y la escribe en un archivo CSV.
    
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
    archivo_csv.writerow(['N', 'Suma Inferior', 'Residuo Inf', 'Suma Superior', 'Residuo Sup'])
    
    # Calcular y escribir los datos
    for n in range(n_inicio, n_fin + 1, incremento):
        inf = suma_inferior(n)
        sup = suma_superior(n)
        residuo_inf = abs(inf - valor_pi)
        residuo_sup = abs(sup - valor_pi)
        archivo_csv.writerow([n, inf, residuo_inf, sup, residuo_sup])

def generar_tablas_csv(nombre_archivo='tablas_comparativas.csv'):
    """
    Genera un archivo CSV con las tres tablas comparativas.
    
    Parámetros:
    - nombre_archivo: Nombre del archivo CSV a crear (por defecto 'tablas_comparativas.csv')
    """
    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo:
        writer = csv.writer(archivo)
        
        # Escribir encabezado general
        writer.writerow(['Tablas Comparativas - Aproximación de π mediante Sumas de Riemann'])
        writer.writerow([f'Valor de π (referencia): {math.pi:.10f}'])
        
        # Tabla 1: N de 10 a 100, variando de 10 en 10
        generar_tabla_individual_csv(writer, n_inicio=10, n_fin=100, incremento=10, numero_tabla=1)
        
        # Tabla 2: N de 100 a 1000, variando de 100 en 100
        generar_tabla_individual_csv(writer, n_inicio=100, n_fin=1000, incremento=100, numero_tabla=2)
        
        # Tabla 3: N de 1000 a 10000, variando de 1000 en 1000
        generar_tabla_individual_csv(writer, n_inicio=1000, n_fin=10000, incremento=1000, numero_tabla=3)
    
    print(f"\n✓ Archivo CSV generado: {nombre_archivo}")

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
    
    # Ejercicio 1.2: Generar tablas comparativas
    print("\n\n")
    print("EJERCICIO 1.2: TABLAS COMPARATIVAS")
    generar_tablas_comparativas()
    
    # Generar también archivo CSV con las tablas
    generar_tablas_csv('tablas_comparativas.csv')


