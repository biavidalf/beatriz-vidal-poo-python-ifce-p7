from cliente import Cliente
from item_nota_fiscal import ItemNotaFiscal
import datetime


class NotaFiscal:
    def __init__(self, Id, codigo, cliente):
        self.__Id = Id
        self.__codigo = codigo
        self.__cliente = cliente
        self.__data = datetime.datetime.now()
        self.__itens = []
        self.__valorNota = 0.0

    def setCliente(self, cliente):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente

    def adicionarItem(self, item):
        if isinstance(item, ItemNotaFiscal):
            self.__itens.append(item)

    def calcularNotaFiscal(self):
        valor = 0.0
        for item in self.__itens:
            valor = valor + item.get_preco_total()
        self.__valorNota = valor

    def imprimirNotaFiscal(self):
        linha = '--------------------------------------------------------------------------------'
        temp = 'NOTA FISCAL'
        texto = f'' \
                f'{linha}\n' \
                f'{temp:<64s}{self.__data.year}/{self.__data.month}/{self.__data.day}  {self.__data.hour}:' \
                f'{self.__data.minute}\n' \
                f'CLIENTE: {self.__cliente.get_codigo()}      NOME: {self.__cliente.get_nome()}\n' \
                f'CPF/CNPJ: {self.__cliente.get_cpfcnpj()}\n' \
                f'{linha}\n' \
                f'ITENS\n' \
                f'{linha}\n' \
                f'  SEQ      DESCRIÇÃO                  QTD        VALOR UNIT        PREÇO        \n' \
                f' ------   ------------------------   ------     --------------    --------------'

        print(texto)

        for x in self.__itens:
            print(f'  {x.get_seq():<9s}{x.get_descricao():<28s}{x.get_qtd():<11d}{x.get_valor_unit():<18.2f}'
                  f'{x.get_preco_total():<13.2f}\n')

        print(linha)
        print(f'Valor total: {self.__valorNota}')
