class Produto:
    def __init__(self, id, codigo, descricao, valorUnitario):
        self.__id = id
        self.__codigo = codigo
        self.__descricao = descricao
        self.__valorUnitario = valorUnitario

    def getDescricao(self):
        return self.__descricao

    def getValorUnitario(self):
        return self.__valorUnitario

    def str(self):
        string = "\nId={3} Codigo={2} Descricao={1} Valor Unitario={0}".format(self.__valorUnitario, self.__descricao,
                                                                               self.__codigo, self.__id)
        return string
