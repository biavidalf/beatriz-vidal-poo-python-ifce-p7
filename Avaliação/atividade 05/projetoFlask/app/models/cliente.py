matricula = 0


class Cliente:

    def __init__(self, nome, senha, email, cnpjcpf):
        global matricula
        matricula += 1
        self.__matricula = matricula
        self.__nome = nome
        self.__senha = senha
        self.__email = email
        self.__cnpjcpf = cnpjcpf

    def get_matricula(self):
        return self.__matricula

    def get_nome(self):
        return self.__nome

    def get_senha(self):
        return self.__senha

    def get_cnpjcpf(self):
        return self.__cnpjcpf

    def set_matricula(self, matric):
        self.__matricula = matric

    def set_nome(self, nome):
        self.__nome = nome

    def set_senha(self, sen):
        self.__senha = sen

    def set_cnpjcpf(self, cpf):
        self.__cnpjcpf = cpf

    def __repr__(self):
        return f'User {self.__matricula}'

