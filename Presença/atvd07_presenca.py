"""
    ATIVIDADE 07 - PRESENÇA: POO - P7 DE INFO - BEATRIZ V.

    ENUNCIADO: Codifique classes a partir do modelo de domínio gerado da atividade anterior.
    Crie classes onde seja possível estabelecer os relacionamentos abordados mas aulas.
"""
#Funcoes gerais
def checar_medicos():
    print(f'\nQuantidade de medicos cadastrados: {len(Medico.medicos)}')
    cont = 1
    for x in Medico.medicos:
        print(f'Medico {cont}: {x}')
        cont += 1

def checar_clientes():
    print(f'\nQuantidade de clientes cadastrados: {len(Cliente.clientes)}')
    cont = 1
    for x in Cliente.clientes:
        print(f'Cliente {cont}: {x}')
        cont += 1

def checar_hospitais():
    print(f'\nQuantidade de hospitais: {len(Hospital.hospitais)}')
    cont = 1
    for x in Hospital.hospitais:
        print(f'Hospital {cont}: {x}')
        cont += 1


# Classes
class Hospital:
    contador = 0
    hospitais = []

    def __init__(self, nome, endereco):
        Hospital.contador += 1
        self.id = Hospital.contador
        self.nome = nome
        self.endereco = endereco
        Hospital.hospitais.append(self.nome)

    def fechar_hospital(self):
        Medico.medicos.remove(self.nome)

class Medico:
    medicos = []
    def __init__(self, nome, crm, cpf, email, endereco, especificacao):
        self.nome = nome
        self.crm = crm
        self.cpf = cpf
        self.email = email
        self.endereco = endereco
        self.especificacao = especificacao
        Medico.medicos.append(nome)

    def demitir_medico(self):
        Medico.medicos.remove(self.nome)


class Consulta:
    consultas = []
    cont_consultas = 0

    def __init__(self, medico, cliente, data, preco, hospital):
        Consulta.cont_consultas += 1
        self.medico = medico
        self.cliente = cliente
        self.data = data
        self.preco = preco
        self.hospital = hospital
        self.id = Consulta.cont_consultas
        Consulta.consultas.append(self.id)

    def realizar_consulta(self):
        Consulta.consultas.remove(self.id)

    def cancelar_consulta(self):
        Consulta.consultas.remove(self.id)


class Cliente:
    clientes = []
    def __init__(self, nome, telefone, cpf, email, endereco):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.email = email
        self.endereco = endereco
        Cliente.clientes.append(nome)


# Testando
hospital1 = Hospital('São Carlos', 'Jose Walter')

medico1 = Medico('Augusto', 2315, '04392492', 'augusto@gmail', 'Jovita', 'Cirurgião')

cliente1 = Cliente('Beatriz', 97008596, '8784652', 'beatriz@gmail', 'Amadeu Furtado')

consulta1 = Consulta(medico1, cliente1, '10/12', 150.00, hospital1)

checar_medicos()
checar_hospitais()
checar_clientes()
