#  if you have nothing in the class, write pass
class Cell:
    pass

class Cell:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
    def cell_distance(self, other_cell):
        return ((self.x - other_cell.x)**2 + (self.y - other_cell.y)**2)**(1/2)

cell_1 = Cell("Abhay", 1, 2)
cell_2 = Cell("Yes", 3, 4)
print(cell_1.name)

print(cell_1.cell_distance(cell_2))