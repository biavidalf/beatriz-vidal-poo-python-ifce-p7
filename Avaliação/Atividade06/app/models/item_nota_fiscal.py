from Avaliação.Atividade06.app.models.produto import Produto


class ItemNotaFiscal:
    # CONSTRUTOR
    def __init__(self, id, sequencial, quantidade, produto):
        self.__id = id
        self.__sequencial = sequencial
        self.__quantidade = quantidade
        self.__produto = produto
        self.__descricao = self.__produto.get_descricao()
        self.__valorUnitario = self.__produto.get_valor_unitario()
        self.__valorItem = float(self.__quantidade * self.__valorUnitario)

    # GETS
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

    def get_id(self):
        return self.__id

    # SETS
    def set_sequencial(self, sequencial):
        self.__sequencial = sequencial

    def set_quantidade(self, quantidade):
        self.__quantidade = quantidade
        self.__valorItem = float(quantidade * self.__valorUnitario)

    # DICT PRO JSON
    def dicionario(self):
        return {'id': self.__id,
                'sequencial': self.__sequencial,
                'quantidade': self.__quantidade,
                'produto': self.__produto.dicionario(),
                'valor-item': self.__valorItem
                }
