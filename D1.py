"""
# MM2015 - Desafío de programación 1: Lógica proposicional
# autor: macastillo

# NOTA:
# Debe utilizar letras minúsculas para los nombres de las variables, por ejemplo, a, b, c.
# Puede utilizar paréntesis para agrupar expresiones, como «a and (b or c)».

# Implemente las cuatro funciones siguientes:
# tabla_verdad, tautologia, equivalentes e inferencia

# Entrega:
# Deberá subir este archivo a la página del curso en Canvas.
"""


######## No modifique el siguiente bloque de código ########
# ********************** COMIENZO *******************************

from functools import partial
import re


class Infix(object):
    def __init__(self, func):
        self.func = func
    def __or__(self, other):
        return self.func(other)
    def __ror__(self, other):
        return Infix(partial(self.func, other))
    def __call__(self, v1, v2):
        return self.func(v1, v2)

@Infix
def implies(p, q) :
    return not p or q

@Infix
def iff(p, q) :
    return (p |implies| q) and (q |implies| p)

# Debe utilizar esta función para extraer variables.
# Esta función toma una expresión como entrada y devuelve una lista ordenada de variables.
# NO modifique esta función.

def extract_variables(expression):
    sorted_variable_set = sorted(set(re.findall(r'\b[a-z]\b', expression)))
    return sorted_variable_set


# ********************** FIN *******************************



############## IMPLEMENTAR LAS SIGUIENTES FUNCIONES  ##############
############## No modificar las definiciones de las funciones ##############

# Función: tabla_verdad
# Esta función calcula una tabla de verdad para una expresión dada.
# Entrada: expresión.
# Salida: tabla de verdad como una lista de listas.

def tabla_verdad(expr):
    # Extrae las variables proposicionales de la expresión (letras minúsculas)
    variables = extract_variables(expr)
    n = len(variables) 
    tabla = []
    # Recorre todas las combinaciones posibles (2^n)
    for i in range(2 ** n):
        # Genera la combinación de valores de verdad para las variables usando operaciones de bits
        valores = [(i >> j) & 1 == 1 for j in reversed(range(n))]
        # Crea un diccionario que asigna cada variable a su valor de verdad
        contexto = dict(zip(variables, valores))
        try:
            # Evalúa la expresión lógica usando los valores actuales de las variables
            resultado = eval(expr, {"implies": implies, "iff": iff}, contexto)
        except Exception:
            resultado = None
        # Agrega la fila a la tabla: valores de las variables + resultado de la expresión
        fila = valores + [resultado]
        tabla.append(fila)
    return tabla

# Función: tautologia
# Esta función determina si la expresión es una tautología, devuelve True;
# en caso contrario, devuelve False.
# Entrada: expresión.
# Salida: booleano.
def tautologia(expr):
    #tabla de vdd del expresión ingresado
    tabla = tabla_verdad(expr)
    #Last elememt of each table is the result 
    for fila in tabla:
        if fila [-1] is not True: #si hay una Falsa, no es taut
            return False
    return True #en caso deonde no hay false

# Función: equivalentesif 
# Esta función determina si expr1 es equivalente a expr2, devuelve True;
# en caso contrario, devuelve False.
# Entrada: expresión 1 y expresión 2.
# Salida: booleano.
def equivalentes(expr1, expr2):
    
    # Extraer variables de ambas expresiones
    vars1 = set(extract_variables(expr1))
    vars2 = set(extract_variables(expr2))

    # Si los conjuntos de variables no son iguales, no pueden ser equivalentes
    if vars1 != vars2:
        return False

    # Ordenar las variables en orden ascendente
    variables = sorted(vars1)
    n = len(variables)

    # Probar todas las combinaciones posibles de valores
    for i in range(2 ** n):
        valores = [(i >> j) & 1 == 1 for j in reversed(range(n))]
        contexto = dict(zip(variables, valores))

        try:
            r1 = eval(expr1, {"implies": implies, "iff": iff}, contexto)
            r2 = eval(expr2, {"implies": implies, "iff": iff}, contexto)
        except Exception:
            return False  # En caso de error de sintaxis o evaluación

        if r1 != r2:
            return False  # En al menos una combinación difieren

    return True  # Todas las combinaciones coinciden


# Función: inferencia
# Esta función determina los valores de verdad para una evaluación de una proposición dada.
# Entrada: expresión.
# Salida: lista de listas.

def inferencia(expr):
    try:
        #Para evitar espacios
        expr = expr.strip()
        # Revisar que tenga el signo "="
        if "=" not in expr:
            print("Error. La expresión debe contener '='. Vuelva a intentarlo")
            return []
        
        #Separar proposición y la igualdad (valor 0 o 1)
        partes = expr.split("=") #Se separa justo en el =
        proposicion = partes[0].strip() 
        valor = partes[1].strip() 

        #Revisar que este bien igualado
        if valor not in ["0", "1"]:
            print("Error: el valor debe ser 0 o 1.")
            return []
        
        # Convertir valor esperado a booleano
        if valor == "1":
            valor_esperado = True
        else:
            valor_esperado = False

        # Obtener tabla de verdad
        tabla = tabla_verdad(proposicion)

        # Filtrar las filas que cumplen la condición
        resultados = []
        for fila in tabla:
            if fila[-1] == valor_esperado:
                resultados.append(fila[:-1])
        return resultados
    
    except Exception:
        print("Error: expresión no válida.")
        return []

