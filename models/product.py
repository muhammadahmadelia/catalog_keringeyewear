from models.metafields import Metafields
from models.variant import Variant

class Product:
    def __init__(self) -> None:
        self.__id = 0
        self.__url = ''
        self.__brand = ''
        self.__number = ''
        self.__name = ''
        self.__frame_code = ''
        self.__frame_color = ''
        self.__lens_code = ''
        self.__lens_color = ''
        self.__status = 'active'
        self.__type = ''
        self.__metafields = None
        self.__variants = []
        self.__shopify_id = ''
        pass
    
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def brand(self) -> str:
        return self.__brand

    @brand.setter
    def brand(self, brand: str):
        self.__brand = brand

    @property
    def number(self) -> str:
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def frame_code(self) -> str:
        return self.__frame_code

    @frame_code.setter
    def frame_code(self, frame_code: str):
        self.__frame_code = frame_code

    @property
    def frame_color(self) -> str:
        return self.__frame_color

    @frame_color.setter
    def frame_color(self, frame_color: str):
        self.__frame_color = frame_color

    @property
    def lens_code(self) -> str:
        return self.__lens_code

    @lens_code.setter
    def lens_code(self, lens_code: str):
        self.__lens_code = lens_code

    @property
    def lens_color(self) -> str:
        return self.__lens_color

    @lens_color.setter
    def lens_color(self, lens_color: str):
        self.__lens_color = lens_color

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type
    
    @property
    def metafields(self) -> Metafields:
        return self.__metafields

    @metafields.setter
    def metafields(self, metafields: Metafields):
        self.__metafields = metafields

    @property
    def variants(self) -> list[Variant]:
        return self.__variants

    @variants.setter
    def variants(self, variant: Variant):
        self.__variants.append(variant)
    
    @property
    def shopify_id(self) -> str:
        return self.__shopify_id

    @shopify_id.setter
    def shopify_id(self, shopify_id: str):
        self.__shopify_id = shopify_id
