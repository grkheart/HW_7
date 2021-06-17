# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
#
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
#
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу
# декоратора @property.

class Tissue:
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def sqrm_coat(self):
        return self.size * 6.5 + 0.5

    def sqrm_suit(self):
        return self.height * 2 + 0.3

    @property
    def sqrm_total(self):
        return str(f'Общая площадь ткани \n'
                   f' {[(self.size / 6.5 + 0.5) + (self.height * 2 + 0.3)]}')


class Coat(Tissue):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.sq_coat = round(self.size / 6.5 + 0.5)

    def __str__(self):
        return f'Размер отреза для пальто {self.sq_coat}'


class Suit(Tissue):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.sq_suit = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Размер отреза для костюма {self.sq_suit}'


coat = Coat(9, 7)
suit = Suit(6, 9)
print(coat)
print(suit)
print(coat.sqrm_total)
print(suit.sqrm_total)
print('Размер отреза на пальто:', coat.sq_coat, 'Размер отреза на костюм:',
suit.sq_suit)
