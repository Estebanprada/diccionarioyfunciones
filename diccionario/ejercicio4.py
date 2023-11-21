# Se crea un diccionario llamado 'informacion' con claves 'nombre' y 'notafinal', y sus respectivos valores
informacion = {
    'nombre': 'breiner',
    'notafinal': 3.9
}
# Crear otro diccionario llamado 'informacion1' con claves de nombres y sus respectivas notas finales.
informacion1 = {
    'Paulo': 4.0,
    'Laura': 4.5,
    'Tovar': 2.5,
    'Fierro': 2.0
}
# Iterar a traves de las claves y valores del diccionario 'informacion' utilizando un bucle 'for'.
for clave, valor in informacion.items():
    print(clave, valor)