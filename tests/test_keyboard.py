import pytest

from src.keyboard import KeyBoard


@pytest.fixture()
def keyboard():
    return KeyBoard("Asus", 500, 20)


def test_init_name(keyboard):
    assert keyboard.name == "Asus"
    assert keyboard.price == 500
    assert keyboard.quantity == 20


def test_mixinlang(keyboard):
    assert keyboard.language == "EN"
    keyboard.change_lang()
    assert keyboard.language == "RU"
    keyboard.change_lang().change_lang()
    assert keyboard.language == "RU"

def test__repr__(keyboard):
    assert repr(keyboard) == "Item('Asus', 500, 20)"

def test__str__(keyboard):
    assert str(keyboard) == "Asus"

if __name__ == '__main__':
    pytest.main()