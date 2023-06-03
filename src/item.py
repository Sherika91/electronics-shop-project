import csv
import os.path


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.name}'

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return int(self.quantity) + int(other.quantity)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, data: str):
        if len(data) <= 10:
            self.__name = data
        else:
            raise Exception(' Длина наименования товара превышает 10 символов.')

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls) -> None:
        try:
            cls.all.clear()
            data_csv = os.path.join('../src/items.csv')
            with open(data_csv, newline='', encoding='UTF-8') as file:
                csvreader = csv.DictReader(file)
                for row in csvreader:
                    Item.all.append(cls(row['name'], row['price'], row['quantity']))

        except FileNotFoundError:
            print("File not found.")

    @staticmethod
    def string_to_number(data):
        num = float(data)
        return int(num)
