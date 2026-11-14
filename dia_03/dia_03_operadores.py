r"""
=====================================================================
 PYTHON EN 30 DÍAS — DÍA 3: Operadores y booleanos
 Versión aplicada a la ingeniería
=====================================================================
 Temas:
   1. Booleanos: True y False
   2. Operadores de asignación: =, +=, -=, *=, /=, **=
   3. Operadores aritméticos (repaso) y orden de prioridad
   4. Operadores de comparación: ==, !=, <, >, <=, >=
   5. Operadores lógicos: and, or, not
   6. Operadores de pertenencia e identidad: in, not in, is
   7. Aplicación: comprobaciones de diseño

 Ejecutar (con el .venv activado):
     python dia_03\dia_03_operadores.py
=====================================================================
"""

import math

# ---------------------------------------------------------------
# 1. BOOLEANOS
# ---------------------------------------------------------------
# Solo tienen dos valores: True y False (con mayúscula inicial).
# Son el resultado de cualquier pregunta de "sí o no".

valvula_abierta = True
alarma_activa = False
print("¿Válvula abierta?", valvula_abierta, "->", type(valvula_abierta).__name__)

# Curiosidad: internamente True vale 1 y False vale 0
print("True + True + False =", True + True + False)
print()

# ---------------------------------------------------------------
# 2. OPERADORES DE ASIGNACIÓN
# ---------------------------------------------------------------
# Atajos para modificar una variable a partir de su propio valor.

carga_total = 0          # kN
carga_total += 25        # equivale a: carga_total = carga_total + 25
carga_total += 40        # se suma otra carga puntual
print("Carga acumulada:", carga_total, "kN")

carga_total *= 1.35      # se mayora (coeficiente de seguridad ELU)
print("Carga mayorada :", carga_total, "kN")

nivel_deposito = 3.0     # m
nivel_deposito -= 0.4    # se vacía 40 cm
print("Nivel depósito :", nivel_deposito, "m")

# Otros: /=  //=  %=  **=
lado = 3
lado **= 2               # lado = lado ** 2
print("Área del cuadrado:", lado)
print()

# ---------------------------------------------------------------
# 3. PRIORIDAD DE OPERADORES
# ---------------------------------------------------------------
# Igual que en matemáticas:  ()  ->  **  ->  * / // %  ->  + -
# Ante la duda: PARÉNTESIS. Hacen el código más legible.

q, L = 10, 6
print("q * L ** 2 / 8   =", q * L ** 2 / 8)     # 45.0  (correcto: qL²/8)
print("(q * L) ** 2 / 8 =", (q * L) ** 2 / 8)   # 450.0 (¡otra cosa!)

# Trampa clásica: el signo menos y la potencia
print("-2 ** 2   =", -2 ** 2)     # -4  -> primero 2**2, luego el signo
print("(-2) ** 2 =", (-2) ** 2)   #  4
print()

# ---------------------------------------------------------------
# 4. OPERADORES DE COMPARACIÓN  -> siempre devuelven True/False
# ---------------------------------------------------------------
sigma = 180       # MPa, tensión calculada
sigma_adm = 235   # MPa, tensión admisible

print("sigma <  sigma_adm :", sigma < sigma_adm)
print("sigma >  sigma_adm :", sigma > sigma_adm)
print("sigma <= sigma_adm :", sigma <= sigma_adm)
print("sigma == 180       :", sigma == 180)   # == compara, = asigna
print("sigma != 180       :", sigma != 180)   # != significa "distinto de"

# Comparaciones encadenadas (muy pythónico, como en matemáticas)
Re = 3000
print("¿Flujo de transición? 2000 <= Re <= 4000 :", 2000 <= Re <= 4000)

# ⚠️ CUIDADO al comparar floats con == (recuerda el 5.800000000000011)
print("0.1 + 0.2 == 0.3 ?", 0.1 + 0.2 == 0.3)               # False (!)
print("math.isclose(0.1 + 0.2, 0.3) ?", math.isclose(0.1 + 0.2, 0.3))  # True
print()

# ---------------------------------------------------------------
# 5. OPERADORES LÓGICOS: and, or, not
# ---------------------------------------------------------------
#   and -> True solo si AMBAS son True
#   or  -> True si AL MENOS UNA es True
#   not -> invierte el valor
#
#   A      B      | A and B | A or B
#   True   True   |  True   |  True
#   True   False  |  False  |  True
#   False  True   |  False  |  True
#   False  False  |  False  |  False

flecha = 18        # mm
flecha_adm = 24    # mm (L/250 para L = 6 m)

cumple_resistencia = sigma <= sigma_adm
cumple_flecha = flecha <= flecha_adm

print("Cumple resistencia:", cumple_resistencia)
print("Cumple flecha     :", cumple_flecha)
print("Viga VÁLIDA (ambas):", cumple_resistencia and cumple_flecha)

presion_alta = False
temperatura_alta = True
print("¿Disparar alarma? (alguna):", presion_alta or temperatura_alta)
print("¿Sistema en reposo? not valvula_abierta:", not valvula_abierta)
print()

# ---------------------------------------------------------------
# 6. PERTENENCIA (in) E IDENTIDAD (is)
# ---------------------------------------------------------------
aceros = ["S235", "S275", "S355"]
print("¿'S275' está en la lista?   ", "S275" in aceros)
print("¿'S460' NO está en la lista?", "S460" not in aceros)
print("¿'HA' aparece en 'HA-25'?   ", "HA" in "HA-25")   # también en textos

# 'is' comprueba si es EL MISMO objeto. Se usa sobre todo con None:
resultado = None          # None = "todavía no hay valor"
print("¿Resultado vacío?", resultado is None)
print()

# ---------------------------------------------------------------
# 7. APLICACIÓN: COMPROBACIÓN DE UNA BARRA A TRACCIÓN
# ---------------------------------------------------------------
N = 120e3            # N
d = 25               # mm
fy = 275             # MPa (S275)
gamma_M0 = 1.05

A = math.pi * d ** 2 / 4
sigma_barra = N / A
sigma_resistente = fy / gamma_M0
aprovechamiento = sigma_barra / sigma_resistente

print(f"σ = {sigma_barra:.1f} MPa  |  fy/γM0 = {sigma_resistente:.1f} MPa")
print(f"Aprovechamiento = {aprovechamiento:.1%}")
print("¿CUMPLE?", sigma_barra <= sigma_resistente)


# =================================================================
#  EJERCICIOS — Completa los TODO y ejecuta el archivo
# =================================================================

# --- Nivel 1 -----------------------------------------------------

# TODO 1: Crea una variable contador = 0 y, usando SOLO operadores
#         de asignación (+=, *=, -=...), haz que valga:
#         primero 10, luego 30, luego 25 y finalmente 625.
#         Imprime el valor después de cada paso.

# TODO 2: Con a = 7 y b = 3, imprime el resultado (True/False) de:
#         a > b,  a < b,  a == b,  a != b,  a >= 7,  b <= 2

# TODO 3: Predice ANTES de ejecutar (escribe tu predicción en un
#         comentario) y luego comprueba:
#             print(True and False)
#             print(True or False)
#             print(not (3 > 2))
#             print(3 > 2 and 2 > 1)
#             print(10 == 10.0)
#             print("10" == 10)
#             print(2 + 3 * 4 ** 2)

# --- Nivel 2 (ingeniería) ----------------------------------------

# TODO 4: Una viga de luz L = 5 m tiene una flecha calculada de 22 mm.
#         La flecha admisible es L/250 (ojo con las unidades).
#         Calcula flecha_adm, y crea un booleano cumple_flecha.
#         Imprime ambos.

# TODO 5: Un motor eléctrico se considera en funcionamiento SEGURO si:
#           - la temperatura del bobinado es menor de 120 °C, Y
#           - la corriente está entre 5 y 32 A (ambos incluidos), Y
#           - NO está activada la parada de emergencia.
#         Con temp = 98, corriente = 27.5, emergencia = False,
#         crea una sola expresión booleana "seguro" e imprímela.
#         Luego cambia los datos para que dé False por cada motivo.

# TODO 6: Tienes la lista de materiales homologados en tu empresa:
#             homologados = ["S275", "S355", "HA-25", "HA-30", "B500S"]
#         Comprueba con "in" si están homologados: "S355", "HA-35"
#         y "B500S". Imprime los resultados.

# --- Nivel 3 (reto) ----------------------------------------------

# TODO 7: Pendiente y distancia entre dos puntos de un trazado.
#         P1 = (2, 2) y P2 = (6, 10)  (coordenadas en m)
#         - Calcula la pendiente m = (y2 - y1) / (x2 - x1)
#         - Calcula la pendiente en %  y el ángulo en grados
#           (pista: math.degrees(math.atan(m)))
#         - Calcula la distancia entre los puntos
#         - Comprueba con un booleano si la pendiente supera el 8 %
#           (límite típico de una rampa accesible)

# TODO 8: Revisa tu script reynolds.py: la condición
#             elif Re >= 2000 and Re <= 4000:
#         se puede escribir de forma más corta con lo visto hoy.
#         Escríbela aquí en un comentario (y si quieres, cámbiala allí).
