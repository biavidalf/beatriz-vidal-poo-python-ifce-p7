class MovimentoFolha:
    def __init__(self, colab, descricao, valor, tipo):
        self.__descricao = descricao
        self.__valor = valor
        self.__colab = colab        # colaborador
        self.__tipo = tipo      # tipo do movimento - provento(P) ou desconto (D)

    def get_colab(self):
        return self.__colab

    def get_tip(self):
        return self.__tipo

    def get_valor(self):
        return self.__valor
