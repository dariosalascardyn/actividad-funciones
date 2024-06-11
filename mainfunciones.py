import os
os.system("cls")
from funcionesactividad import precio_iva, area_circulo, media_numeros, cuadrado_de_numeros

#IVA
a = int(input("ingrese precio sin iva\n"))
print(precio_iva(a))

#area circulo
radio = int(input("ingrese el radio del circulo\n"))
print(area_circulo(radio))

#media nueros
listanumeros = [1,2,3,4]
print(f"la media de los numeros 1, 2, 3, 4 es {media_numeros(listanumeros)}")
      
# creando logica para preguntar por numeros
    # lista_numeros= []
    # banderanumeros = True
    # while banderanumeros:
    #     numeros = int(input("ingrese numeros"))
    #     lista_numeros.append(numeros)
    #     opcion= input("desea ingresar mas numeros?  si/no ")
    #     if opcion == "si":
    #         numeros = int(input("ingrese numeros"))
    #         lista_numeros.append(numeros)
            
    #     elif ==
    
# cuadrado de numeros
listacuadrados = [1, 2, 3, 4]
print(f"el cuadrado de los numeros 1, 2, 3, 4 es {cuadrado_de_numeros(listacuadrados)}")

#cantidad de palabras
palabras = input("ingrese una frase\n")
cantidad_palabras(palabras)

#cantidad letras
letras = input("ingrese una frase\n")
cantidad_letras(letras)
