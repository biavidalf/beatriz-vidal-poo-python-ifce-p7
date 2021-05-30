class Cliente:
    def __init__(self, id, nome, codigo, cnpjcpf, tipo):
        self.__id = id
        self.__nome = nome
        self.__codigo = codigo
        self.__cnpjcpf = cnpjcpf
        self.__tipo = tipo

    def str(self):
        string = "\nId={4} Codigo={2} Nome={3} CNPJ/CPF={1} Tipo={0}".format(self.__tipo, self.__cnpjcpf, self.__codigo,
                                                                             self.__nome, self.__id)
        return string

    def get_nome(self):
        return self.__nome

    def get_codigo(self):
        return self.__codigo

    def get_cpfcnpj(self):
        return self.__cnpjcpf
