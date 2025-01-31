def mysplit(cadena):
    palabras = []
    palabra = ""
    for i in cadena:
        if i == " ":
            if palabra:
                palabras.append(palabra)
                palabra = ""
        else:
            palabra += i
    if palabra:
        palabras.append(palabra)
    return palabras

print(mysplit("Ser o no ser, esa es la pregunta"))
print(mysplit("Ser o no ser,esa es la pregunta"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
