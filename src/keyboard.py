from src.item import Item


class MixinLang:

    def __init__(self, language="EN"):
        self.__language = language

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
            return self
        else:
            self.__language = "EN"
            return self


class KeyBoard(Item, MixinLang):

    def __init__(self, name: str, price: int, quantity: int, language="EN") -> None:
        super().__init__(name, price, quantity)

    def __repr__(self) -> str:
        return f"{Item.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        return self.name
