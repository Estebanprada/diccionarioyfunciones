# Se define una funcion llamada 'saludar'
def saludar():
    print("Saludo") 

# Se define una funcion llamada 'retornarnumero'
def retornarnumero():
    return 1  # Devolver el valor 1 cuando la funcion es llamada.

# Llamar a la función 'saludar', que imprimirá el mensaje "Saludo".
saludar()

# Llamar a la función 'retornarnumero' y guardar el resultado en la variable 'resultado'.
resultado = retornarnumero()

# Verificar si el valor devuelto por 'retornarnumero' es igual a 1.
if resultado == 1:
    print("Devolvió solo uno")  # Imprimir el mensaje "Devolvió solo uno" si la condición es verdadera.
else:
    print("No devolvió solo uno")  # Imprimir el mensaje "No devolvió solo uno" si la condición es falsa.