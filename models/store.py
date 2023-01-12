from models.brand import Brand

class Store:
    def __init__(self) -> None:
        self.__id = 0
        self.__name = ''
        self.__link = ''
        self.__login_flag = False
        self.__username = ''
        self.__password = ''
        self.__brands = []
        pass

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def login_flag(self) -> bool:
        return self.__login_flag

    @login_flag.setter
    def login_flag(self, login_flag: bool):
        self.__login_flag = login_flag

    @property
    def link(self) -> str:
        return self.__link

    @link.setter
    def link(self, link: str):
        self.__link = link

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def brands(self) -> list[Brand]:
        return self.__brands

    @brands.setter
    def brands(self, brand: Brand):
        self.__brands.append(brand)