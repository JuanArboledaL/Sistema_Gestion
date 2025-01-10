libros = {
 "Cien años de soledad": ["Realismo mágico", "Drama"],
 "El señor de los anillos": ["Fantasía", "Aventura"],
 "1984": ["Distopía", "Política", "Drama"],
 "Don Quijote": ["Clásico", "Aventura"]
}

realismo_magico = {}
drama = {}
fantasia = {}
aventura = {}
distopia = {}
politica = {}
clasico = {}

genero = input("Ingresa un genero del literario: ")

if genero == "Realismo magico":

    for clave,valor in libros.values:

        if valor == genero:
            realismo_magico[clave]
