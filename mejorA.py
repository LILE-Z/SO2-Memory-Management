from collections import deque

particiones = [['Libre', 100, None], ['Libre', 100, None], ['Libre', 100, None], ['Libre', 600, None], ['Libre', 1200, None]]

# Crear una cola para mantener un seguimiento de los elementos que no se pudieron agregar
cola_trabajos_pendientes = deque()  # Declarar como cola
trabajos = []  # Lista de trabajos
fragmentacion_interna = [0] * 5  # Seguir la fragmentación_interna

# Lista de trabajos
while True:
    nombre_trabajo = input("Ingresa el nombre del proyecto (Si deseas dejar de introducir elementos escribe fin o N): ")
    if nombre_trabajo == "fin" or nombre_trabajo=="N":
        break
    tamano_trabajo = int(input("Ingresa el tamaño del trabajo: "))
    trabajos.append({"nombre": nombre_trabajo, "tamano": tamano_trabajo})

for trabajo in trabajos:
    particion_asignada = None  # Sirve para ver si pudo agregar
    for i, particion in enumerate(particiones):
        if not particion[2] and trabajo["tamano"] <= particion[1]:  # Verificar que no esté ocupado y que quepa
            particion_asignada = i
            particiones[i][0] = trabajo["nombre"]
            particiones[i][2] = trabajo['tamano']
            fragmentacion_interna[i] = particion[1] - trabajo['tamano']
            print("                 Asignación Exitosa")
            print(f"El trabajo '{trabajo['nombre']}' se ha cargado en la partición {i + 1}.")
            break
    if particion_asignada is None:
        cola_trabajos_pendientes.append(trabajo)
        print(f"El trabajo '{trabajo['nombre']}' ha sido agregado a la cola de trabajos pendientes.")


    # Estado de la memoria después de que se agregara o no un trabajo
    print("Estado en memoria")
    fragmentacion_externa = 0
    for i, particion in enumerate(particiones):
        trabajo = particion[0] if particion[2] is not None else "Libre"
        fragmentacion = particion[1] - (particion[2] if particion[2] is not None else 0)  # fragmentación_interna
        print(f"Partición {i + 1}: Tamaño = {particion[1]}, Trabajo = {trabajo}, Fragmentación = {fragmentacion}")
        if particion[0] == "Libre":
            fragmentacion_externa += particion[1]

print(f"Fragmentación Externa Total = {fragmentacion_externa}")

# Liberar espacios
for i, particion in enumerate(particiones):
    if cola_trabajos_pendientes and cola_trabajos_pendientes[0]['tamano'] <= particion[1]:
        trabajo_pendiente = cola_trabajos_pendientes.popleft()
        particiones[i][0] = trabajo_pendiente['nombre']
        particiones[i][2] = trabajo_pendiente['tamano']
        fragmentacion_interna[i] = particion[1] - trabajo_pendiente['tamano']
        print(f"El trabajo '{trabajo_pendiente['nombre']}' se ha cargado en la partición {i + 1}.")

# Calcular la fragmentación interna total
fragmentacion_interna_total = sum(fragmentacion_interna)

# Imprimir el estado final de las particiones después de liberar la memoria
print("\nEstado final de las particiones:")
for i, particion in enumerate(particiones):
    trabajo = particion[0] if particion[2] is not None else "Libre"
    fragmentacion = particion[1] - (particion[2] if particion[2] is not None else 0)
    print(f"Partición {i + 1}: Tamaño = {particion[1]}, Trabajo = {trabajo}, Fragmentación = {fragmentacion}")

# Imprimir la fragmentación interna total
print(f"Fragmentación Interna Total = {fragmentacion_interna_total}")

