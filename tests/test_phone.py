import pytest
from src.phone import Phone


@pytest.fixture()
def _obj():
    return Phone('Телефон', 10, 5, 2)


def test__repr__(_obj):
    assert repr(_obj) == "Phone('Телефон', 10, 5, 2)"


def test__str__(_obj):
    assert str(_obj) == 'Телефон'


def test_number_of_sims(_obj):
    assert _obj.number_of_sim == 2



if __name__ == "__main__":
    pytest.main()
