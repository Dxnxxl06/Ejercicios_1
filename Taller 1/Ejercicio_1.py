texto = "Taller 1/peliculas.txt"

def cartelera():
    with open(texto, mode = 'r') as file:
        cartelera = file.readlines()
    for i in cartelera:
        print(i)

menu= '''
        MENU

        1.MOSTRAR CARTELERA
        2.SALIR
'''


while True:
    
    print(menu)
    opcion = int(input('Ingrese la opcion: '))

    if opcion == 1:
        print( "\n" )
        cartelera()
        input("Continuar...")
        continue

    if opcion == 2:
        break

    else:
        print("[X] Opcion invalida")