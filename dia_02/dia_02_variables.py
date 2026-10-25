r"""
=====================================================================
 PYTHON EN 30 DÍAS — DÍA 2: Variables y funciones integradas
 Versión aplicada a la ingeniería
=====================================================================
 Temas:
   1. Qué es una variable y cómo nombrarla
   2. Asignación múltiple en una línea
   3. Funciones integradas (built-in): len, min, max, sum, round...
   4. Conversión de tipos (casting): int, float, str, list...
   5. input(): pedir datos al usuario

 Ejecutar (con el .venv activado):
     python dia_02\dia_02_variables.py
=====================================================================
"""

# ---------------------------------------------------------------
# 1. VARIABLES
# ---------------------------------------------------------------
# Una variable es un NOMBRE que apunta a un VALOR guardado en memoria.
# Se crea al asignarle algo con "=" (no es el "igual" matemático,
# es "guarda esto aquí").

longitud_viga = 6.0        # m
carga_repartida = 12.5     # kN/m

# Se puede reasignar: la variable pasa a apuntar al nuevo valor
longitud_viga = 7.5
print("Longitud actual de la viga:", longitud_viga, "m")

# REGLAS para nombrar variables:
#   ✅ letras, números y guion bajo:  sigma_adm, E_acero, nodo_2
#   ❌ no pueden empezar por número:   2nodo
#   ❌ no pueden tener espacios ni guiones:  carga total, carga-total
#   ❌ no pueden ser palabras reservadas: if, for, class, import...
#   ⚠️ distingue mayúsculas: E y e son variables distintas
#
# CONVENCIONES (no obligatorias, pero todo el mundo las sigue):
#   - snake_case: palabras en minúscula separadas por _  -> carga_total
#   - sin tildes ni ñ en los nombres
#   - nombres que expliquen qué son: "sigma_adm" mejor que "s"
#   - CONSTANTES en mayúsculas: G = 9.81, PI = 3.14159

G = 9.81  # m/s² (constante)
print()

# ---------------------------------------------------------------
# 2. ASIGNACIÓN MÚLTIPLE
# ---------------------------------------------------------------
# Varias variables en una sola línea
b, h, L = 0.30, 0.50, 6.0          # sección de hormigón (m) y luz (m)
print(f"Sección {b} x {h} m, luz {L} m")

# Intercambiar dos valores sin variable auxiliar
x_inicio, x_fin = 10, 2
x_inicio, x_fin = x_fin, x_inicio
print("Tras intercambiar:", x_inicio, x_fin)

# Desempaquetar una tupla (coordenadas de un nodo)
nodo_A = (2.0, 3.0, 0.0)
x, y, z = nodo_A
print(f"Nodo A -> x = {x}, y = {y}, z = {z}")
print()

# ---------------------------------------------------------------
# 3. FUNCIONES INTEGRADAS (built-in)
# ---------------------------------------------------------------
# Ya conoces: print(), type(), str(), abs(), input(), float()
# Hoy añadimos las que más vas a usar con datos:

lecturas_galga = [152.3, 149.8, 155.1, 150.6, 148.9]  # MPa, ensayo de tracción

print("Número de lecturas  len():", len(lecturas_galga))
print("Mínima              min():", min(lecturas_galga))
print("Máxima              max():", max(lecturas_galga))
print("Suma                sum():", sum(lecturas_galga))
media = sum(lecturas_galga) / len(lecturas_galga)
print("Media                     :", media)
print("Media redondeada  round():", round(media, 2))
print("Ordenadas        sorted():", sorted(lecturas_galga))

# len() también cuenta caracteres de un texto
designacion = "IPE 300"
print(f"'{designacion}' tiene {len(designacion)} caracteres")

# help() y dir() te ayudan a explorar (pruébalas en la consola >>>)
#   help(round)   -> explica cómo se usa round
#   dir(str)      -> lista todo lo que se puede hacer con textos
print()

# ---------------------------------------------------------------
# 4. CONVERSIÓN DE TIPOS (casting)
# ---------------------------------------------------------------
print(int(7.9))           # 7     -> int() TRUNCA, no redondea
print(round(7.9))         # 8     -> round() sí redondea
print(float(3))           # 3.0
print(float("998.2"))     # 998.2 -> texto a número (como en tu Reynolds)
print(str(210))           # '210'
print(list("ACERO"))      # ['A', 'C', 'E', 'R', 'O']

# ⚠️ Error típico: int() no entiende un texto con decimales
#   int("7.5")  -> ValueError
#   int(float("7.5"))  -> 7   ✅
print()

# ---------------------------------------------------------------
# 5. input(): PEDIR DATOS AL USUARIO
# ---------------------------------------------------------------
# input() SIEMPRE devuelve texto (str), por eso hay que convertirlo.
# Descomenta estas líneas para probarlo:

# masa = float(input("Masa del cuerpo (kg): "))
# peso = masa * G
# print(f"Peso = {peso:.2f} N")


# =================================================================
#  EJERCICIOS — Completa los TODO y ejecuta el archivo
# =================================================================

# --- Nivel 1 -----------------------------------------------------

# TODO 1: Crea variables con: nombre, apellidos, nombre_completo
#         (uniendo los dos anteriores con un f-string), ciudad,
#         edad, y una variable booleana estudias_master.
#         Imprímelas todas.

# TODO 2: Declara en UNA sola línea tres variables con las
#         dimensiones de un depósito: largo = 4, ancho = 2.5, alto = 3 (m).
#         Calcula e imprime su volumen en m³ y en litros.

# TODO 3: Comprueba con type() el tipo de todas las variables del TODO 1.

# --- Nivel 2 (ingeniería) ----------------------------------------

# TODO 4: Estas son las temperaturas (°C) medidas cada hora en un
#         intercambiador de calor:
#             temps = [78.2, 80.5, 79.1, 83.4, 81.0, 77.6, 82.2]
#         Imprime: nº de medidas, mínima, máxima, media (2 decimales)
#         y el rango (máx - mín).

# TODO 5: Un eje macizo de diámetro d = 40 mm.
#         Calcula su área y su perímetro usando math.pi
#         (recuerda: import math, al principio del todo o justo aquí).
#         Imprime ambos con 2 decimales.

# TODO 6: ¿Qué imprime cada línea? Piénsalo ANTES de ejecutarlo,
#         escribe tu predicción en un comentario y luego compruébalo:
#             print(int(9.99))
#             print(round(9.99))
#             print(len("Hormigón HA-25"))
#             print(float("3") + 2)
#             print("3" + "2")

# --- Nivel 3 (reto) ----------------------------------------------

# TODO 7: Escribe un mini-programa que pida por teclado (input):
#         la potencia de un motor en kW y su velocidad en rpm,
#         y calcule el par motor:   T = P / ω
#         donde ω = 2·π·n / 60  (rad/s) y P en W.
#         Imprime el par en N·m con 1 decimal.
#         Prueba con P = 15 kW, n = 1450 rpm  (resultado ≈ 98.8 N·m)
