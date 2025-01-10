tienda1 = {"manzanas": 10, "naranjas": 15, "plátanos": 5}
tienda2 = {"manzanas": 8, "naranjas": 20, "uvas": 13}

tiendaFusion = {}

for clave, valor in tienda1.items():
    tiendaFusion[clave] = valor

for clave, valor in tienda2.items():

    if clave in tiendaFusion:

        tiendaFusion[clave] += valor

    else:
        tiendaFusion[clave] = valor

print(tiendaFusion)
