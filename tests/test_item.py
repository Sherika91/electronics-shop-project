""""Здесь надо написать тесты с использованием pytest для модуля item."""
import csv
import os.path

import pytest
from src.item import Item
from src.phone import Phone
from src.item import InstantiateCSVError


@pytest.fixture()
def _obj():
    return Item('Телефон', 10, 5)


def test_calculate_total_price(_obj):
    """Проверяем, что общая цена рассчитывается правильно"""
    item = _obj
    assert item.calculate_total_price() == 50


def test_apply_discount(_obj):
    """
     Устанавливаем скидку
     Применяем скидку
     Проверяем, что цена после скидки установлена правильно
    """
    item = _obj
    item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 8


def test_all_items(_obj):
    """Проверяем, что все элементы добавляются в список all"""
    _obj.all.clear()
    item1 = Item("Test Item 1", 10, 5)
    item2 = Item("Test Item 2", 20, 3)
    assert len(Item.all) == 0

    # Homework #2


def test_name_too_long(_obj):
    """ Длина наименования товара меньше 10 символов """
    _obj.name = 'Смартфон'
    assert _obj.name == 'Смартфон'
    """  на  длина наименования товара больше 10 символов
    Exception: ' Длина именования товара превышает 10 символов.'"""
    with pytest.raises(Exception):
        _obj.name = 'СуперСмартфон'


def test_instantiate_from_csv(_obj):
    assert _obj.name == "Телефон"
    assert _obj.price == 10
    assert _obj.quantity == 5


def test_instantiate_no_file():

    with pytest.raises(FileNotFoundError):
        os.rename('../src/temp_invalid.csv', '../src/items.csv')
        Item.instantiate_from_csv()


def test_instantiate_2():
    data_csv = os.path.join('../src/items.csv')
    with open(data_csv, newline='', encoding='windows-1251') as file:
        csvreader = csv.DictReader(file)
        for row in csvreader:
            Item(row['name'], row['price'], row['quantity'])


def test_instantiate_from_csv_missing_fields():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv()


def test_string_to_number(_obj):
    """ Метод, который возвращает число из числа-строки """
    assert _obj.string_to_number('5') == 5
    assert _obj.string_to_number('5.0') == 5
    assert _obj.string_to_number('5.5') == 5


def test__repr__(_obj):
    assert repr(_obj) == "Item('Телефон', 10, 5)"


def test__str__(_obj):
    assert str(_obj) == 'Телефон'


def test__add__():
    item1 = Item("Смартфон", 10000, 20)
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
    assert phone1 + 100 == 120_100


if __name__ == "__main__":
    pytest.main()
