# se crear un diccionario vacio llamado 'datos'
datos = dict()
# se puede crear un diccionario vacio utilizando la sintaxis de llaves
datos = {}
# Inicializamos el diccionario 'datos' con algunas claves y valores
datos = {'nombre': 'esteban', 'edad': 17}
# se Imprime el valor asociado con la clave 'nombre'
print(datos['nombre'])
# se utiliza el metodo get() para obtener el valor asociado con la clave 'nombre1' en el diccionario 'datos'
print(datos.get('nombre1', 'no se encuentra el elemento'))