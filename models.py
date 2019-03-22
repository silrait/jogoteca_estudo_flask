class Jogo:
    def __init__(self, nome, categoria, console, id=None):
        self.__id = id
        self.__nome = nome
        self.__categoria = categoria
        self.__console = console

    @property
    def nome(self):
        return self.__nome

    @property
    def categoria(self):
        return self.__categoria

    @property
    def console(self):
        return self.__console

    @property
    def id(self):
        return self.__id

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @id.setter
    def id(self, id):
        self.__id = id

    @categoria.setter
    def categoria(self, categoria):
        self.__categoria = categoria

    @console.setter
    def console(self, console):
        self.__console = console


class Usuario:
    def __init__(self, id, nome, senha):
        self.__id = id
        self.__nome = nome
        self.__senha = senha

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def senha(self):
        return self.__senha
