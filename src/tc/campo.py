import random as rd

class Campo:
    def __init__(self, filas: int, columnas: int):
        self.filas = filas
        self.columnas = columnas
        self.matriz = []
        self.nave = ["_", "🚤", "🛥️"]

    def generar_campo(self) -> list[list[str]]:
        for i in range(self.filas):
            fila = []
            for j in range(self.columnas):
                fila.append(rd.choice(self.nave))
            self.matriz.append(fila)
        return self.matriz
                                                      
    