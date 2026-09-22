import random


def crearEntrenador(tupla):
    print("Ingrese el nombre del entrenador:")
    entrenador = input()

    print("Ingrese el nombre del Pokemon:")
    pokemon = input()

    ataque = random.randint(150, 250)
    vida = random.randint(500, 900)

    nuevo = (entrenador, pokemon, ataque, vida)
    tupla.append(nuevo)

    print("Entrenador y Pokemon creados.")
    print(f"Ataque: {ataque}")
    print(f"Vida: {vida}")


def ordenBurbuja(lis):
    for i in range(1, len(lis)):
        for j in range(len(lis)-1):
            if lis[j][2] > lis[j+1][2]:
                lis[j], lis[j+1] = lis[j+1], lis[j]

    return lis


def listaEntrenador(tupla):
    ordenBurbuja(tupla)

    print("===== LISTA DE ENTRENADORES =====")

    correlativo = 1

    for item in tupla:
        print(f"{correlativo}. Entrenador: {item[0]} - Pokemon: {item[1]} - Ataque: {item[2]} - Vida: {item[3]}")
        correlativo += 1


def ordenSeleccion(lista):
    n = len(lista)

    for manoIzq in range(n):
        ind_min_val = manoIzq

        for vista in range(manoIzq + 1, n):
            if lista[vista][3] < lista[ind_min_val][3]:
                ind_min_val = vista

        lista[manoIzq], lista[ind_min_val] = lista[ind_min_val], lista[manoIzq]

    return lista


def busqueda_binaria(array, vida):
    menor = 0
    mayor = len(array) - 1

    for data in range(len(array)):
        medio = (menor + mayor) // 2

        if array[medio][3] == vida:
            return medio

        elif array[medio][3] < vida:
            menor = medio

        else:
            mayor = medio

        if mayor - menor <= 1:
            break

    if array[menor][3] == vida:
        return menor

    elif array[mayor][3] == vida:
        return mayor

    return -1


def borraPorPokemon(tupla):
    ordenSeleccion(tupla)

    print("Ingrese la vida del Pokemon a buscar:")
    vida = int(input())

    busqueda = busqueda_binaria(tupla, vida)

    if busqueda == -1:
        print(f"No existe un Pokemon con vida {vida}.")

    else:
        eliminado = tupla[busqueda]

        tupla.remove(eliminado)

        print(f"Se elimino al entrenador {eliminado[0]} y su Pokemon {eliminado[1]}.")


def peleaPokemon(lista):
    listaEntrenador(lista)

    print("Ingrese el numero del primer Pokemon:")
    numero1 = int(input())

    print("Ingrese el numero del segundo Pokemon:")
    numero2 = int(input())

    indice1 = numero1 - 1
    indice2 = numero2 - 1

    pokemon1 = lista[indice1]
    pokemon2 = lista[indice2]

    aleatorio1 = random.randint(0, 5)
    aleatorio2 = random.randint(0, 5)

    ataque1 = pokemon1[2] * aleatorio1
    ataque2 = pokemon2[2] * aleatorio2

    vida1 = pokemon1[3] - ataque2
    vida2 = pokemon2[3] - ataque1

    print(f"{pokemon1[1]} realiza un ataque de {ataque1}")
    print(f"{pokemon2[1]} realiza un ataque de {ataque2}")

    print(f"Vida de {pokemon1[1]}: {vida1}")
    print(f"Vida de {pokemon2[1]}: {vida2}")

    if vida1 <= 0 and vida2 <= 0:
        lista.remove(pokemon1)
        lista.remove(pokemon2)

        print("Ambos Pokemon quedaron sin vida. Ambos perdieron.")

    elif vida1 == vida2:
        lista.remove(pokemon1)
        lista.remove(pokemon2)

        print("Ambos Pokemon empataron. Ambos perdieron.")

    elif vida1 > vida2:
        lista[indice1] = (pokemon1[0], pokemon1[1], pokemon1[2], vida1)

        lista.remove(pokemon2)

        print(f"Ganador: {pokemon1[0]} con su Pokemon {pokemon1[1]}")

    else:
        lista[indice2] = (pokemon2[0], pokemon2[1], pokemon2[2], vida2)

        lista.remove(pokemon1)

        print(f"Ganador: {pokemon2[0]} con su Pokemon {pokemon2[1]}")


lista = []

opcion = ""

while opcion != "5":

    print("================================")
    print("============ POKEMON ===========")
    print("================================")
    print("1. Crear Entrenador")
    print("2. Listar Entrenadores")
    print("3. Borrar por Pokemon")
    print("4. Pelea Pokemon")
    print("5. Fin")

    opcion = input("Seleccione una opcion: ")

    match opcion:

        case "1":
            crearEntrenador(lista)

        case "2":
            listaEntrenador(lista)

        case "3":
            borraPorPokemon(lista)

        case "4":
            peleaPokemon(lista)

        case "5":
            print("Saliendo del programa")
            break

        case _:
            print("Opcion invalida")