# Inicializar el número de particiones y su tamaño prueba 
num_particiones = int(input("Ingrese el número de particiones: "))
particiones = {}

# Solicitar información de cada partición
for i in range(num_particiones):
    tamano_particion = int(input(f"Ingrese el tamaño de la partición {i + 1}: "))
    particiones[i + 1] = {'tamano': tamano_particion, 'trabajo': None}

while True:
    # Solicitar información del trabajo
    nombre_trabajo = input("\nIngrese el nombre del trabajo (o 'salir' para terminar): ")
    if nombre_trabajo.lower() == 'salir':
        break
    tamano_trabajo = int(input("Ingrese el tamaño del trabajo: "))

    # Determinar si el trabajo cabe en alguna partición
    particion_asignada = None
    for num_particion, particion in particiones.items():
        if tamano_trabajo <= particion['tamano'] and particion['trabajo'] is None:
            particion_asignada = num_particion
            particiones[num_particion]['trabajo'] = nombre_trabajo
            break

    if particion_asignada is not None:
        print(f"El trabajo '{nombre_trabajo}' se ha cargado en la partición {particion_asignada}.")
    else:
        print(f"No se pudo cargar el trabajo '{nombre_trabajo}' en ninguna partición.")

print("\nEstado final de las particiones:")
for num_particion, particion in particiones.items():
    trabajo = particion['trabajo'] if particion['trabajo'] is not None else "Libre"
    print(f"Partición {num_particion}: Tamaño = {particion['tamano']}, Trabajo = {trabajo}")

