def texto_a_binario(texto):
    binario = "".join(format(ord(i), 'b') for i in texto)
    return binario

texto = input("ingresa el texto a convertir :  ")

binario = texto_a_binario(texto)

print ("el texto binario es:", binario)

