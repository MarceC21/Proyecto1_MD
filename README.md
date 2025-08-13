# Proyecto1_MD

## Descripción

Este programa permite trabajar con proposiciones lógicas escritas en Python usando variables proposicionales de una sola letra en minúsculas (ej. `a`, `b`, `c`), operadores lógicos (`not`, `and`, `or`) y conectores personalizados (`|implies|`, `|iff|`).

A través de un menú interactivo, el usuario puede:

1. Generar la tabla de verdad de una proposición.
2. Verificar si una proposición es una tautología.
3. Verificar si dos proposiciones son lógicamente equivalentes.
4. Realizar inferencia (pendiente de implementación).
5. Salir del programa.

## Archivos

* **D1.py** Contiene la implementación de las funciones:

  * `tabla_verdad(expr)`
  * `tautologia(expr)`
  * `equivalentes(expr1, expr2)`
  * `inferencia(expr)` *(pendiente)*
* **Main.py** Programa principal con el menú de opciones.
* **README.md** Documento de descripción y uso del programa.

## Sintaxis de expresiones lógicas

* **Negación**: `not a`
* **Conjunción**: `a and b`
* **Disyunción**: `a or b`
* **Implicación**: `a |implies| b`
* **Doble implicación**: `a |iff| b`
* Se permiten paréntesis para agrupar:

  ```
  (a and b) or (c and not d)
  ```


## Ejemplos de uso

### **1. Tabla de verdad**

```
Seleccione una opción del menú: 1
Escriba una expresión: a or b
[False, False, False]
[False, True, True]
[True, False, True]
[True, True, True]
```

### **2. Tautología**

```
Seleccione una opción del menú: 2
Ingrese una expresión para ver si es una tautología: (a and b) |implies| a
SI es una tautología. :)
```

### **3. Equivalencias**

```
Seleccione una opción del menú: 3
Ingrese la primera expresión: a |implies| b
Ingrese la segunda expresión: not a or b
Las expresiones son lógicamente equivalentes
```

---

## Restricciones

* Solo se permiten variables proposicionales de una letra en minúscula (`a` a `z`).
* No se permiten dígitos, mayúsculas ni caracteres especiales en los nombres de variables.
* Las expresiones deben seguir la sintaxis de Python para operadores lógicos.


## Créditos

Proyecto realizado como parte del curso **MM2015 - Matemática Discreta 1**.


