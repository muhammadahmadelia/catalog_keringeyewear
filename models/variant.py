class Variant:
    def __init__(self) -> None:
        self.__id = 0
        self.__product_id = 0
        self.__position = 0
        self.__title = ''
        self.__sku = ''
        self.__inventory_quantity = 0
        self.__found_status = 1
        self.__wholesale_price = ''
        self.__listing_price = ''
        self.__barcode_or_gtin = ''
        self.__size = ''
        self.__weight = '0.5'
        self.__shopify_id = 0
        self.__inventory_item_id = ''
        pass

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def product_id(self) -> int:
        return self.__product_id

    @product_id.setter
    def product_id(self, product_id: int):
        self.__product_id = product_id

    @property
    def position(self) -> int:
        return self.__position

    @position.setter
    def position(self, position: int):
        self.__position = position

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def sku(self) -> str:
        return self.__sku

    @sku.setter
    def sku(self, sku: str):
        self.__sku = sku

    @property
    def inventory_quantity(self) -> int:
        return self.__inventory_quantity

    @inventory_quantity.setter
    def inventory_quantity(self, inventory_quantity: int):
        self.__inventory_quantity = inventory_quantity

    @property
    def found_status(self) -> int:
        return self.__found_status

    @found_status.setter
    def found_status(self, found_status: int):
        self.__found_status = found_status

    @property
    def wholesale_price(self) -> str:
        return self.__wholesale_price

    @wholesale_price.setter
    def wholesale_price(self, wholesale_price: str):
        self.__wholesale_price = wholesale_price

    @property
    def listing_price(self) -> str:
        return self.__listing_price

    @listing_price.setter
    def listing_price(self, listing_price: str):
        self.__listing_price = listing_price

    @property
    def barcode_or_gtin(self) -> str:
        return self.__barcode_or_gtin

    @barcode_or_gtin.setter
    def barcode_or_gtin(self, barcode_or_gtin: str):
        self.__barcode_or_gtin = barcode_or_gtin

    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

    @property
    def weight(self) -> str:
        return self.__weight

    @weight.setter
    def weight(self, weight: str):
        self.__weight = weight

    @property
    def shopify_id(self) -> str:
        return self.__shopify_id

    @shopify_id.setter
    def shopify_id(self, shopify_id: str):
        self.__shopify_id = shopify_id

    @property
    def inventory_item_id(self) -> str:
        return self.__inventory_item_id

    @inventory_item_id.setter
    def inventory_item_id(self, inventory_item_id: str):
        self.__inventory_item_id = inventory_item_id
