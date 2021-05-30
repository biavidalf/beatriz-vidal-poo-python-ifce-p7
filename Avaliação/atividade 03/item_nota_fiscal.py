class ItemNotaFiscal:
    def __init__(self, id, sequencial, quantidade, produto):
        self.__id = id
        self.__sequencial = sequencial
        self.__quantidade = quantidade
        self.__produto = produto
        self.__descricao = self.__produto.getDescricao()
        self.__valorUnitario = self.__produto.getValorUnitario()
        self.__valorItem = float(self.__quantidade * self.__valorUnitario)

    def get_seq(self):
        if self.__sequencial < 10:
            return f'00{self.__sequencial}'
        elif self.__sequencial < 100:
            return f'0{self.__sequencial}'
        else:
            return self.__sequencial

    def get_qtd(self):
        return self.__quantidade

    def get_valor_unit(self):
        return self.__valorUnitario

    def get_preco_total(self):
        return self.__valorItem

    def get_descricao(self):
        return self.__descricao
