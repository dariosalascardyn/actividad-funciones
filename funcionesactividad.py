
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

