from MovimentoFolha import MovimentoFolha


class FolhaPagamento:
    def __init__(self, mes, ano):
        self.__movimentos = []
        self.__mes = mes
        self.__ano = ano
        self.__total_proventos = 0
        self.__total_descontos = 0

    # 8
    def calcular_folha(self):
        colabs = [self.__movimentos[0].get_colab()]

        for x in self.__movimentos:
            if x.get_colab().get_codigo() not in [colab.get_codigo() for colab in colabs]:
                colabs.append(x.get_colab())
            if x.get_tip() == "P":
                self.__total_proventos += x.get_valor()
            else:
                self.__total_descontos += x.get_valor()

            # 7
            x.get_colab().inserir_movimento(x)

        salarios = 0
        for i in colabs:
            salarios += i.get_salario()

        liquido = salarios + (self.__total_proventos - self.__total_descontos)
        imprimir = f'|Total de salários:  {salarios:<16.2f}|Total de descontos: {self.__total_descontos:<16.2f}\n' \
                   f'|Total a pagar:      {liquido:<16.2f}' \
                   f'|Total de proventos: {self.__total_proventos:<16.2f}'
        return imprimir

    # 4
    def inserir_movimentos(self, movimento):
        if isinstance(movimento, MovimentoFolha):
            self.__movimentos.append(movimento)

    if __name__ == '__main__':
        pass
