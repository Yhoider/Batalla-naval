import random as rd


class Campo:

    """
    Representa el campo de juego en forma de una matriz bidimensional.
    Cada celda puede contener agua ("_") o barcos ("🚤", "🛥️").
    """

    def __init__(self, filas: int, columnas: int):
        """
        Inicializa el campo con el tamaño dado.

        :param filas: Número de filas del campo.
        :param columnas: Número de columnas del campo.
        """
        self.filas = filas
        self.columnas = columnas
        self.matriz = []
        self.nave = ["_", "🚤", "🛥️"]

    def generar_campo(self) -> list[list[str]]:
        """
        Llena la matriz con símbolos aleatorios representando el mar y barcos.

        :return: La matriz generada.
        """
        for i in range(self.filas):
            fila = []
            for j in range(self.columnas):
                fila.append(rd.choice(self.nave))
            self.matriz.append(fila)
        return self.matriz
                                                      
    