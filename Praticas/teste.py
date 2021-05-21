# ITEM A
from Colaborador import Colaborador
from FolhaPagamento import FolhaPagamento
from MovimentoFolha import MovimentoFolha

# ITEM B
if __name__ == '__main__':
    # 1
    FP = FolhaPagamento(9, 2019)

    # 2
    CL01 = Colaborador(100, 'Manoel Claudino', 'Av 13 de maio 2081', '88671020', 'Benfica',
                       '60020-060', '124543556-89', 4500.00)
    CL02 = Colaborador(200, 'Carmelina da Silva', 'Av dos expedicionarios 1200', '3035-1280', 'Aeroporto',
                       '60530-020', '301789435-54', 2500.00)
    CL03 = Colaborador(300, 'Gurmelina Castro Saraiva', 'Av João Pessoa 1020', '3235-1089', 'Damas',
                       '60330-090', '350245632-76', 3000.00)

    # 3
    MF01 = MovimentoFolha(CL01, 'Gratificação', 4500.00, 'P')
    MF02 = MovimentoFolha(CL01, 'Plano Saúde', 1000.00, 'P')
    MF03 = MovimentoFolha(CL01, 'Pensão', 600.00, 'D')

    MF04 = MovimentoFolha(CL02, 'Gratificação', 2500.00, 'P')
    MF05 = MovimentoFolha(CL02, 'Plano Saúde', 1000.00, 'P')
    MF06 = MovimentoFolha(CL02, 'Faltas', 600.00, 'D')

    MF07 = MovimentoFolha(CL03, 'Gratificação', 4500.00, 'P')
    MF08 = MovimentoFolha(CL03, 'Plano Saúde', 1000.00, 'P')
    MF09 = MovimentoFolha(CL03, 'Pensão', 600.00, 'D')

    # 6
    FP.inserir_movimentos(MF01)
    FP.inserir_movimentos(MF02)
    FP.inserir_movimentos(MF03)
    FP.inserir_movimentos(MF04)
    FP.inserir_movimentos(MF05)
    FP.inserir_movimentos(MF06)
    FP.inserir_movimentos(MF07)
    FP.inserir_movimentos(MF08)
    FP.inserir_movimentos(MF09)

    # 7 automatico na classe FolhaPagamento

    # Imprimindo os métodos calcular folha e salário
    print()
    print(f'Folha total da empresa:=================================\n{FP.calcular_folha()}')
    print()

    print('Folhas individuais:=====================================')
    print(CL01.calcular_salario())
    print()
    print()
    print(CL02.calcular_salario())
    print()
    print()
    print(CL03.calcular_salario())
