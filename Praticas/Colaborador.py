from MovimentoFolha import MovimentoFolha


class Colaborador:

    def __init__(self, codigo, nome, endereco, telefone, bairro, cep, cpf, salario_atual):
        self.__movimentos = []
        self.__codigo = codigo
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone
        self.__bairro = bairro
        self.__cep = cep
        self.__cpf = cpf
        self.__salario_atual = salario_atual

    def get_codigo(self):
        return self.__codigo

    def get_salario(self):
        return self.__salario_atual

    # 9
    def calcular_salario(self):
        proventos = 0
        descontos = 0
        for x in self.__movimentos:
            if x.get_tip() == "P":
                proventos += x.get_valor()
            else:
                descontos += x.get_valor()

        liquido = float(self.__salario_atual + (proventos - descontos))

        texto = f'|Codigo:   {self.__codigo:<13d}|Nome: {self.__nome}\n' \
                f'|Salário:  {self.__salario_atual:<13.2f}|Liquido: {liquido}\n' \
                f'|Provento: {proventos:<13.2f}|Desconto: {descontos:<10.2f}'

        return texto

    # 5
    def inserir_movimento(self, movimento):
        if isinstance(movimento, MovimentoFolha):
            self.__movimentos.append(movimento)
