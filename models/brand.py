from models.product import Product


class Brand:
    def __init__(self) -> None:
        self.__id = 0
        self.__store_id = 0
        self.__name = ''
        self.__code = ''
        self.__products = []
        pass

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def store_id(self) -> int:
        return self.__store_id

    @store_id.setter
    def store_id(self, store_id: int):
        self.__store_id = store_id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: int):
        self.__code = code

    @property
    def products(self) -> list[Product]:
        return self.__products

    @products.setter
    def products(self, product: Product):
        self.__products.append(product)

    def empty_products(self):
        self.__products = []