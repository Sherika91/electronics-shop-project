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


if __name__ == "__main__":
    pytest.main()
