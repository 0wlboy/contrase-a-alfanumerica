import string 
import random 

listBase=['']
listExtension=['']
esta= True
salir= False


def randomCaracteres(base):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    largo = 32-len(base)
    lista = ''.join(random.choice(caracteres) for i in range(largo))
    return lista

while salir == False:
    respuesta = input('Introduzca un string entre 6 y 12 caracteres >')
    largo = False
    contador = 0

    while largo == False:
        x = len(respuesta)
        if x > 12 or x < 6:
            print(f'Su base es de {x} y no entra en los parametros')
            respuesta = input('Introduzca un string >')
        else:
            largo = True

    for i in listBase:
        if i == respuesta:
            newPassword = respuesta + listExtension[contador]
            break 
        if i != respuesta:
            contador = contador + 1
            esta = False

    if esta == False: 
        listBase.append(respuesta)
        listExtension.append(randomCaracteres(respuesta))
        newPassword = listBase[contador] + listExtension[contador]

    print(f'su nueva contraseña es: {newPassword}')

    print('desea salir?')
    respuesta = input('escriba salir, sino, escriba cualquier caracter')

    if respuesta == 'salir':
        salir=True 

