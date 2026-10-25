"""
=====================================================================
 PYTHON EN 30 DÍAS — DÍA 1: Introducción
 Versión aplicada a la ingeniería
=====================================================================
 Temas:
   1. Comprobar la versión de Python
   2. Operaciones aritméticas
   3. Comentarios
   4. Tipos de datos básicos y type()
   5. Primer cálculo de ingeniería: distancia entre dos nodos

 Cómo usarlo:
   - Lee cada bloque, ejecuta el archivo y mira la salida.
   - Completa los ejercicios marcados con  # TODO  (abajo del todo).
   - Ejecutar desde la terminal (con el .venv activado):
         python dia_01\dia_01_introduccion.py
=====================================================================
"""

# ---------------------------------------------------------------
# 1. VERSIÓN DE PYTHON
# ---------------------------------------------------------------
import sys

print("Versión de Python:", sys.version)
print()

# ---------------------------------------------------------------
# 2. OPERACIONES ARITMÉTICAS
# ---------------------------------------------------------------
# Ejemplo: una viga con carga repartida q (kN/m) y luz L (m)
q = 12.5      # kN/m
L = 6         # m

print("Suma         q + L  =", q + L)
print("Resta        q - L  =", q - L)
print("Producto     q * L  =", q * L)       # carga total (kN)
print("División     q / L  =", q / L)       # siempre devuelve float
print("Div. entera  17 // 5 =", 17 // 5)   # cuántas barras de 5 m caben en 17 m
print("Resto        17 % 5  =", 17 % 5)    # cuánto sobra
print("Potencia     L ** 2 =", L ** 2)

# Momento máximo en viga biapoyada: M = q·L² / 8
M_max = q * L ** 2 / 8
print(f"Momento máximo = {M_max:.2f} kN·m")
print()

# ---------------------------------------------------------------
# 3. COMENTARIOS
# ---------------------------------------------------------------
# Esto es un comentario de una línea: Python lo ignora.
# Úsalos para explicar el PORQUÉ, no el qué.

"""
Esto es un "docstring" / comentario multilínea.
Útil para documentar al principio de un archivo o función.
"""

# ---------------------------------------------------------------
# 4. TIPOS DE DATOS
# ---------------------------------------------------------------
n_barras = 24                              # int    -> entero
E_acero = 210e9                            # float  -> 210 GPa en Pa (notación científica)
Z = 3 + 4j                                 # complex-> impedancia R + jX (Ω)
material = "Acero S275"                    # str    -> texto
cumple_ELU = True                          # bool   -> verdadero/falso
cargas = [10.0, 12.5, 8.0]                 # list   -> secuencia modificable
nodo = (2.0, 3.0)                          # tuple  -> secuencia fija (coordenadas)
perfil = {"nombre": "IPE 300", "A_cm2": 53.8, "Iy_cm4": 8356}  # dict -> clave: valor
materiales = {"acero", "hormigón", "acero"}  # set    -> sin repetidos

for valor in [n_barras, E_acero, Z, material, cumple_ELU,
              cargas, nodo, perfil, materiales]:
    print(f"{str(valor):<55} -> {type(valor).__name__}")

print("Módulo de la impedancia |Z| =", abs(Z), "Ω")
print()

# ---------------------------------------------------------------
# 5. DISTANCIA ENTRE DOS NODOS (longitud de una barra)
# ---------------------------------------------------------------
# Nodo A (2, 3) y nodo B (10, 8), en metros
xA, yA = 2, 3
xB, yB = 10, 8

longitud = ((xB - xA) ** 2 + (yB - yA) ** 2) ** 0.5
print(f"Longitud de la barra AB = {longitud:.3f} m")
print()


# =================================================================
#  EJERCICIOS — Completa los TODO y ejecuta el archivo
# =================================================================

# --- Nivel 1 -----------------------------------------------------

# TODO 1: Escribe un comentario que diga qué día del reto es hoy.

# Hoy vamos a terminar con el día 1 y empezar con el día 2 del reto de Python en 30 días.

# TODO 2: Con a = 3 y b = 4, imprime: suma, resta, multiplicación,
#         división, resto, división entera y potencia (a ** b).

a = 3
b = 4

print(f"Suma de a + b = {a+b}")
print(f"Resta de a - b = {a-b}")
print(f"Multiplicación de a * b = {a*b}")
print(f"División entre a / b = {a/b}")
print(f"Resto de a % b = {a%b}")
print(f"División entera de a // b = {a//b}")
print(f"Potencia de a ** b = {a**b}")
print()

# TODO 3: Crea variables con TU nombre, tu ingeniería/especialidad,
#         y tu país, e imprímelas en una frase con un f-string.

nombre = "Mikel Pablogorran Alcibar"
ingeniería = "Ingeniería en Tecnología Industrial"
país = "España"
print()

print(f"Mi nombre es {nombre} , estudio el Máster de {ingeniería} y vivo en {país}")
print()

# TODO 4: Comprueba con type() el tipo de estos valores:
#         10, 9.8, 3.14, 4 - 4j, ['Asabeneh', 'Python'], tu nombre

print(f"La variable 10 es de tipo {type(10).__name__}")
print(f"La variable 9.8 es de tipo {type(9.8).__name__}")
print(f"La variable 3.14 es de tipo {type(3.14).__name__}")
print(f"La variable 4 - 4j es de tipo {type(4-4j).__name__}")
print(f"La variable ['Asabeneh', 'Python'] es de tipo {type(['Asabeneh','Python']).__name__}")
print()

# --- Nivel 2 (ingeniería) ----------------------------------------

# TODO 5: Una barra de acero de sección circular, d = 20 mm,
#         soporta un axil N = 50 kN.
#         Calcula el área A = π·d²/4 (en mm²) y la tensión σ = N/A (en MPa).
#         Pista: 1 kN = 1000 N, y N/mm² = MPa. Usa 3.14159 para π.

A = 3.14159 * (20 **2) / 4
N = 50 *1000 #Pasamos de Kn a N
print()

sigma = N / A #MPa
print()

print(f" El área de la superficie es de {A:.2f} mm^2 y la tensión axial que se ejerce sobre la barra es de {sigma:.2f} MPa")
print()

# TODO 6: Un circuito tiene R = 30 Ω y X = 40 Ω.
#         Crea la impedancia compleja Z, e imprime |Z|, Z.real y Z.imag.

Z = 30 + 40j

print (f"El módulo de la impedancia Z = 30 + 40j es {abs(Z)}")
print (f"La parte real de la impedancia Z = 30 + 40j es {Z.real}")
print (f"La parte imaginaria de la impedancia Z = 30 + 40j es {Z.imag}")
print()

# --- Nivel 3 (reto) ----------------------------------------------

# TODO 7: Calcula la longitud de una barra en 3D entre
#         P1 = (0, 0, 0) y P2 = (3, 4, 12). (Resultado esperado: 13)
longitud_3D = ((3-0)**2 + (4-0)**2 + (12-0)**2)**0.5
print(f"La longitud de la barra en 3D entre P1 y P2 es {longitud_3D:.2f}")
print()

# TODO 8: Convierte a Python estas ecuaciones y evalúalas para x = 2:
#         y = 2x - 2
#         y = x² + 6x + 9

x = 2
y1 = 2*x - 2
y2 = x**2 + 6*x + 9

print(f"Para x = {x}, y = 2x - 2 = {y1}")
print(f"Para x = {x}, y = x² + 6x + 9 = {y2}")

print()