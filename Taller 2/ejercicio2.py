texto = 'Taller 2/diario.txt'

def leerDiario():
    with open(texto, mode='r') as file:
        diario = file.readlines()
    for i in diario:
        print (i)

def escribirDiario(mensaje):
    with open(texto, mode='a' ) as file:
        file.writelines(mensaje)

menu='''
      Fokin diario
       1. Leer diario
       2. Escribir una nueva Linea
       3. Salir
'''

while True:
    print(menu)
    
    opcion = int(input("Ingrese la opcion: "))

    if opcion == 1:
        leerDiario()
        input('Continuar...')
        continue
    elif opcion == 2:
        p = input('Ingresar nueva linea: ') 
        escribirDiario(p)
    elif opcion== 3:
        break
    else:
        print('Opcion Invalida')