# Se crea un diccionario vacio llamado 'informacion'
informacion = {}
# Inicializamos el diccionario con una clave 'nombre' y un valor 'esteban', y una clave 'edad' y un valor 17.
informacion = {'nombre': 'esteban', 'edad': 17}
# Eliminar la clave 'nombre' del diccionario 'informacion'.
del(informacion['nombre'])
# Se agrega nuevas claves y valores al diccionario 'informacion'.
informacion.update({'ciudad': 'ibague', 'tel': 3014459707})
# Iterar a traves de las claves y valores del diccionario 'informacion' utilizando un bucle 'for'.
for i, j in informacion.items():
    print(i, j)