class Libro:
        
    catalogo = []

    def __init__(selft,titulo,autor,editorial,precio,anyo_publicacion):
        selft.__titulo = titulo
        selft.__autor = autor
        selft.__editorial = editorial
        selft.__precio = precio
        selft.__anyo_publicacion = anyo_publicacion

        selft.catalogo.append(selft.__titulo)

    def aplicar_descuento(self,descuento):

        porcentaje = (self.__precio * descuento)/100
        if (descuento < 100):
            precioDescuento = self.__precio - porcentaje
        else:
            print("No se puede hacer deuento ya que porcentaje tiene que ser menor al 100% del precio")

    def mostrar_informacion(selft):
        print(selft.catalogo)
        

lb1 = Libro("El Hobbit","J.R.R.Tolkien","Minotauro",16,1937)
lb2 = Libro("Un mundo Feliz","Aldous Huxeley","Plaza & Janes",19.90,1932)
lb3 = Libro("Cancion  de hielo y fuego","George R.R Martin","Gigamesh",30,1996)

lb1.mostrar_informacion()

    