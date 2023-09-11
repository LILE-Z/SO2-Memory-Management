class TablaPaginas:
    def __init__(self, proceso_id):
        self.proceso_id = proceso_id
        self.paginas = []

    def agregar_pagina(self, num_pagina, num_marco):
        self.paginas.append((num_pagina, num_marco))

    def liberar_paginas(self, marcos):
        for _, num_marco in self.paginas:
            marcos[num_marco] = 0
        self.paginas.clear()

    def mostrar(self):
        print(f"\nProceso ID: {self.proceso_id}")
        for num_pagina, num_marco in self.paginas:
            print(f"Numero de Pagina: {num_pagina}, Numero de Marco: {num_marco}")


def mostrar_estado(marcos, tablas):
    print("\nEstado actual de las Tablas de Páginas:")
    for tabla in tablas:
        tabla.mostrar()

    print("\nVector de Marcos:")
    for i, asignado in enumerate(marcos):
        print(f"Marco {i}: {'Asignado' if asignado else 'No Asignado'}")


def main():
    TAMANO_PAGINA = 32
    memoria_ram = int(input("Ingrese la cantidad de memoria RAM disponible (en bytes): "))
    num_marcos = memoria_ram // TAMANO_PAGINA
    marcos = [0] * num_marcos
    N = int(input("Ingrese la cantidad de procesos: "))
    tablas = []
    cola_procesos = []

    for i in range(N):
        proceso_id = input(f"\nIngrese el identificador del proceso {i + 1}: ")
        tamano_proceso = int(input(f"Ingrese el tamaño del proceso {proceso_id} (en bytes): "))
        tabla = TablaPaginas(proceso_id)
        num_paginas = -(-tamano_proceso // TAMANO_PAGINA)

        for j in range(num_paginas):
            asignado = False
            for k in range(num_marcos):
                if marcos[k] == 0:
                    marcos[k] = 1
                    tabla.agregar_pagina(j, k)
                    asignado = True
                    break

            if not asignado:
                proceso_a_liberar = cola_procesos.pop(0)
                print(f"Liberando proceso {proceso_a_liberar.proceso_id} de la memoria física.")
                proceso_a_liberar.liberar_paginas(marcos)
                k = 0
                while marcos[k] != 0:
                    k += 1
                marcos[k] = 1
                tabla.agregar_pagina(j, k)

        tablas.append(tabla)
        cola_procesos.append(tabla)
        mostrar_estado(marcos, tablas)


if __name__ == "__main__":
    main()
