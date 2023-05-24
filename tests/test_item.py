"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


def test_calculate_total_price():
    """Проверяем, что общая цена рассчитывается правильно"""
    item = Item("Test Item", 10, 5)
    assert item.calculate_total_price() == 50


def test_apply_discount():
    """
     Устанавливаем скидку
     Применяем скидку
     Проверяем, что цена после скидки установлена правильно
    """
    item = Item("Test Item", 10, 5)
    item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 8


def test_all_items():
    """Проверяем, что все элементы добавляются в список all"""
    Item.all.clear()
    item1 = Item("Test Item 1", 10, 5)
    item2 = Item("Test Item 2", 20, 3)
    assert len(Item.all) == 2

    # Homework #2

def test_all_second():
    # Создаем класс для проверки новых методов
    item1 = Item('Телефон', 10000, 5)

    # проверяем сеттер отправляя товар, у которого наименование более 10 символов
    item1.name = 'СуперСмартфон'
    # Exception: Длина наименования товара превышает 10 символов.
    assert item1.name == 'Телефон'

    # проверяем сеттер товар, у которого наименование менее 10 символов
    item1.name = 'Смартфон'
    assert item1.name == 'Смартфон'

    # Запускаем метод вызывающий класс из файла
    Item.instantiate_from_csv()

    # Проверяем корректность работы метода, подсчетом записей
    assert len(Item.all) == 5  # в файле 5 записей с данными по товарам

    item6 = Item.all[0]
    assert item6.name == 'Смартфон'
    # проверка стаческого метода, который возвращает число из числа-строки
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


if __name__ == "__main__":
    pytest.main()
