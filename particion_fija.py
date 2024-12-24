from collections import deque

# Inicializar el tamaño de las particiones
tamanos_particiones = [100, 100, 100, 600, 1200]
particiones = [{'tamano': tamano, 'trabajo': None} for tamano in tamanos_particiones]

# Cola de trabajos pendientes
cola_trabajos_pendientes = deque()

# Solicitar la lista de trabajos
trabajos = []
while True:
    nombre_trabajo = input("Ingrese el nombre del trabajo (o 'fin' para terminar la lista): ")
    if nombre_trabajo.lower() == 'fin':
        break
    tamano_trabajo = int(input(f"Ingrese el tamaño del trabajo '{nombre_trabajo}': "))
    trabajos.append({'nombre': nombre_trabajo, 'tamano': tamano_trabajo})

for trabajo in trabajos:
    # Verificar si el trabajo cabe en alguna partición
    particion_asignada = None
    for i, particion in enumerate(particiones):
        if trabajo['tamano'] <= particion['tamano'] and particion['trabajo'] is None:
            particion_asignada = i
            particiones[i]['trabajo'] = trabajo
            print(f"El trabajo '{trabajo['nombre']}' se ha cargado en la partición {i + 1}.")
            break

    if particion_asignada is None:
        cola_trabajos_pendientes.append(trabajo)
        print(f"El trabajo '{trabajo['nombre']}' ha sido agregado a la cola de trabajos pendientes.")

    # Liberar memoria conforme los trabajos se retiran
    for i, particion in enumerate(particiones):
        if particion['trabajo'] is not None:
            if particion['trabajo']['tamano'] == 0:
                cola_trabajos_pendientes.appendleft(particion['trabajo'])
                particion['trabajo'] = None
            else:
                if cola_trabajos_pendientes and cola_trabajos_pendientes[0]['tamano'] <= particion['tamano']:
                    trabajo_pendiente = cola_trabajos_pendientes.popleft()
                    particiones[i]['trabajo'] = trabajo_pendiente
                    particion['trabajo']['tamano'] -= trabajo_pendiente['tamano']
                    print(f"El trabajo '{trabajo_pendiente['nombre']}' se ha cargado en la partición {i + 1}.")

    # Imprimir el estado de la memoria después de cada trabajo
    print("\nEstado actual de la memoria:")
    for i, particion in enumerate(particiones):
        trabajo = particion['trabajo']['nombre'] if particion['trabajo'] is not None else "Libre"
        print(f"Partición {i + 1}: Tamaño = {particion['tamano']}, Trabajo = {trabajo}")

print("\nEstado final de las particiones:")
for i, particion in enumerate(particiones):
    trabajo = particion['trabajo']['nombre'] if particion['trabajo'] is not None else "Libre"
    print(f"Partición {i + 1}: Tamaño = {particion['tamano']}, Trabajo = {trabajo}")

