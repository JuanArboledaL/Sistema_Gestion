class Queue:
    def __init__(self):
        self.__cola =[]

    def put(self, elem):
        self.__cola.append(elem)

    def get(self):
        eliminado = self.__cola[0]
        del self.__cola[0]
        return eliminado
    

clase = Queue()

clase.put(1)
clase.put("juanito")
clase.put(False)

try:
    for i in range(4):
        print(clase.get())
except:
    print("Error de Cola")


