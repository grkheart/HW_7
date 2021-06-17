# Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
# вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).Данные методы должны применяться
# только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток,
# соответственно. В методе деления должно осуществляться округление значения до целого числа.

class Cell:
    def __init__(self, amount):
        self.amount = int(amount)

    def __str__(self):
        return f'Result: {self.amount * "*"}'

    def __add__(self, other):
        return Cell(self.amount + other.amount)

    def __sub__(self, other):
        return self.amount - other.amount if (self.amount - other.amount) > 0 else print('Negative')

    def __mul__(self, other):
        return Cell(int(self.amount * other.amount))

    def __truediv__(self, other):
        return Cell(round(self.amount // other.amount))

    def make_order(self, cell_row):
        row = ' '
        for i in range(int(self.amount / cell_row)):
            row += f'{"*" * cell_row} \\n'
        row += f'{"*" * (self.amount % cell_row)}'
        return row


cells_a = Cell(20)
cells_b = Cell(40)
print(cells_a)
print(cells_a + cells_b)
print(cells_a - cells_b)
print(cells_a * cells_b)
print(cells_a / cells_b)
print(cells_b.make_order(5))
print(cells_a.make_order(12))
