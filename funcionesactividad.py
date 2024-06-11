
#funcion iva
def precio_iva(a):
    preciototal = a * 1.19
    return preciototal


#funcion area circulo 3.14 por radio al cuadrado = 3.14 * radio ** 2
def area_circulo(radio):
    area = (radio ** 2) * 3.14
    return area

#funcion media de numeros
def media_numeros(listanumeros):
    for i in listanumeros:
        numerosumados = sum(listanumeros)
        media = numerosumados / len(listanumeros) 
        return media
    
#funcion cuadrado de numeros
def cuadrado_de_numeros(listacuadrados):
    for i in listacuadrados:
        numerocuadrado = listacuadrados[0] ** 2, listacuadrados[1] ** 2
        return numerocuadrado
    
# funcion cantidad de  palabraas
def cantidad_palabras (palabras):
    numeropalabras = len(palabras.split())
    print(f"el numero de palabras es: {numeropalabras}")
    return(numeropalabras)

#funcion cantidad de letras
def cantidad_letras (letras):
    letras_sin_espacio = letras.split()
    letras_sin_espacio= "".join(letras_sin_espacio)
    numeroletras = len(letras_sin_espacio)
    print(f"el numero de letras es: {numeroletras}")
    return(numeroletras)
