class User:

    # CONSTRUTOR
    def __init__(self, id, nome, codigo, cnpjcpf, tipo):
        self.__id = id
        self.__nome = nome
        self.__codigo = codigo
        self.__cnpjcpf = cnpjcpf
        self.__tipo = tipo

    # GETS
    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_codigo(self):
        return self.__codigo

    def get_cnpjcpf(self):
        return self.__cnpjcpf

    # SETS
    def set_id(self, new):
        self.__id = new

    def set_nome(self, nome):
        self.__nome = nome

    def set_codigo(self, cod):
        self.__codigo = cod

    def set_cnpjcpf(self, cpf):
        self.__cnpjcpf = cpf

    # DICT PRO JSON
    def dicionario(self):
        return {'id': self.get_id(),
                'codigo': self.get_codigo(),
                'cpf': self.get_cnpjcpf(),
                'nome': self.get_nome()
                }
