import os

def clearFunction():
  os.system("clear")

class Matrix:

    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.matrix = [[" " for _ in range(width)] for _ in range(height)]

    def update(self):
        for row in self.matrix:
            print("".join(row))

    def rectangle(self, length, width, posX, posY):
        if (
            posX < 0
            or posY < 0
            or posX + length > self.width
            or posY + width > self.height
        ):
            return False

        for i in range(posX, posX + length):
            for j in range(posY, posY + width):
                self.matrix[j][i] = " #"

    def clear(self):
        for i in range(self.width):
            for j in range(self.height):
                self.matrix[j][i] = "  "
        clearFunction()
        self.update()
