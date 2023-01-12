class Metafields:
    def __init__(self) -> None:
        self.__id = 0
        self.__product_id = 0
        self.__for_who = ''
        self.__product_size = ''
        self.__activity = ''
        self.__lens_material = ''
        self.__graduabile = ''
        self.__interest = ''
        self.__lens_technology = ''
        self.__frame_material = ''
        self.__frame_shape = ''
        self.__gtin1 = ''
        self.__img_url = ''
        self.__img_360_urls = []
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
    def for_who(self) -> str:
        return self.__for_who

    @for_who.setter
    def for_who(self, for_who: str):
        self.__for_who = for_who
    
    @property
    def product_size(self) -> str:
        return self.__product_size

    @product_size.setter
    def product_size(self, product_size: str):
        self.__product_size = product_size

    @property
    def activity(self) -> str:
        return self.__activity

    @activity.setter
    def activity(self, activity: str):
        self.__activity = activity
    
    @property
    def lens_material(self) -> str:
        return self.__lens_material

    @lens_material.setter
    def lens_material(self, lens_material: str):
        self.__lens_material = lens_material

    @property
    def graduabile(self) -> str:
        return self.__graduabile

    @graduabile.setter
    def graduabile(self, graduabile: str):
        self.__graduabile = graduabile

    @property
    def interest(self) -> str:
        return self.__interest

    @interest.setter
    def interest(self, interest: str):
        self.__interest = interest

    @property
    def lens_technology(self) -> str:
        return self.__lens_technology

    @lens_technology.setter
    def lens_technology(self, lens_technology: str):
        self.__lens_technology = lens_technology

    @property
    def frame_material(self) -> str:
        return self.__frame_material

    @frame_material.setter
    def frame_material(self, frame_material: str):
        self.__frame_material = frame_material

    @property
    def frame_shape(self) -> str:
        return self.__frame_shape

    @frame_shape.setter
    def frame_shape(self, frame_shape: str):
        self.__frame_shape = frame_shape

    @property
    def gtin1(self) -> str:
        return self.__gtin1

    @gtin1.setter
    def gtin1(self, gtin1: str):
        self.__gtin1 = gtin1

    @property
    def img_url(self) -> str:
        return self.__img_url

    @img_url.setter
    def img_url(self, img_url: str):
        self.__img_url = img_url

    @property
    def img_360_urls(self) -> list[str]:
        return self.__img_360_urls

    @img_360_urls.setter
    def img_360_urls(self, img_360_url: str):
        self.__img_360_urls.append(img_360_url)



