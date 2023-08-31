tamanoMemoria=int(input("Ingresa el tamano de la memoria "))
memoria=["Libre"]*tamanoMemoria
procesos=[]

#Solo agregarlo a la lista de procesos
while True :
    nombre_proceso= input("Ingresa el nombre_proceso")
    if(nombre_proceso=="fin"):
     break
    tamano_proceso= int(input("Ingresa el tamano_proceso"))
    procesos.append([nombre_proceso,tamano_proceso])


#Agregarlos a la memoria 
for proceso in procesos:
    nombre_proceso,tamano_proceso= proceso
    for i in range (tamanoMemoria):
        #Encontrar espacios
        if memoria [i: i+tamano_proceso]== "Libre" * tamano_proceso:
            memoria[i:i + tamano_proceso] = [nombre_proceso] * tamano_proceso
            break
        else:
            print("No se pudo agregar el proceso por falta de espacio en memoria")
            #Liberar procesos
            for i, bloque in enumerate(memoria):
                if bloque !="Libre":



