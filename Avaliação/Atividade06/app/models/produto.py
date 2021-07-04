class Produto:
    # CONSTRUTOR
    def __init__(self, id, codigo, descricao, valorUnitario):
        self.__id = id
        self.__codigo = codigo
        self.__descricao = descricao
        self.__valorUnitario = valorUnitario

    # GETS
    def get_descricao(self):
        return self.__descricao

    def get_valor_unitario(self):
        return self.__valorUnitario

    def str(self):
        string = "\nId={3} Codigo={2} Descricao={1} Valor Unitario={0}".format(self.__valorUnitario, self.__descricao,
                                                                               self.__codigo, self.__id)
        return string

    def get_id(self):
        return self.__id

    def get_codigo(self):
        return self.__codigo

    # SETS
    def set_codigo(self, codigo):
        self.__codigo = codigo

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def set_valor_unitario(self, valor_unitario):
        self.__valorUnitario = valor_unitario

    # DICT PRO JSON
    def dicionario(self):
        return {'id': self.get_id(),
                'codigo': self.get_codigo(),
                'descricao': self.get_descricao(),
                'valor-unitario': self.get_valor_unitario()
                }
