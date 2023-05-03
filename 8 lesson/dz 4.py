"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов.
 В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
"""

class NumberCheck(Exception):
    def __int__(self,txt):
        self.txt = txt

class MyCheck(Exception):
    def __int__(self,txt):
        self.txt = txt

class Stock:

    def __init__(self, st_address, st_space):
        self.st_address = st_address
        self.st_space = st_space
        self.st_items = {}
        self.free_space = self.st_space
        if type(self.st_space) != int:
            raise NumberCheck ("Введите целое число")

    def add_item(self, new_item, quantity):
        self.free_space -= quantity
        if self.free_space < 0:
            print("Нет места на складе, товар не добавлен на склад")
        else:
            print("Товар размещен на складе")
            print(f'На складе осталось свободно {self.free_space} мест')
            self.st_items.update({new_item: quantity})

    def move_item(self, new_stock, item_name, need_quantity):
        if type(need_quantity) != int:
            raise NumberCheck ("Не введено количество для перемещения товара")
        if item_name in self.st_items:
            el = self.st_items.get(item_name)
            print(f'Доступное количество для перемещения - {el}шт')
            el_q = el - need_quantity
            if el_q >= 0:
                print(f'{need_quantity}  {item_name} отгружено  {new_stock}  ')
                self.free_space -= need_quantity
                self.st_items.update({item_name: el_q})
            else:
                print("На складе не хватает товара для перемещения.Товар не перемещен")
        else:
            print("На складе нет нужного товара для перемещения")

class OfficeEquipment:
    def __init__(self, type: str, model: str):
        self.type = str(type)
        self.model = str(model)

    def __str__(self):
        return f'{self.type}{self.model}'

class Printer(OfficeEquipment):
    def __init__(self, model):
       super().__init__('Принтер',model)

class Scaner(OfficeEquipment):
    def __init__(self, model: str):
        super().__init__('Сканер', model)

my_stock = Stock('St.Pete', 25)
printer_1 = Printer('HP 2105')
printer_2 = Printer('Samsung 00.05')
scaner_1 = Scaner ('HP 2865')
scaner_2 = Scaner ('Samsung 68.15')

my_stock.add_item(printer_1, 8)
my_stock.move_item('Moscow',printer_1, 1)
my_stock.move_item('Moscow',printer_2, 8)
my_stock.add_item(scaner_1, 5)
my_stock.move_item('Moscow', scaner_1, 1)


