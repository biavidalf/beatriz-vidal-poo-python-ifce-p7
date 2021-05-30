from cliente import Cliente
from produto import Produto
from item_nota_fiscal import ItemNotaFiscal
from nota_fiscal import NotaFiscal

# Criando cliente
cli = Cliente(1, "Beatriz Vidal", 1578, "541.197.846-68", 1)

# Criando produtos
p1 = Produto(1, 489, "Biscoito Recheado", 2.0)
it1 = ItemNotaFiscal(1, 1, 3, p1)

p2 = Produto(2, 78, "Salgadinho de queijo", 5.5)
it2 = ItemNotaFiscal(2, 2, 2, p2)

p3 = Produto(3, 8791, "Coca-cola", 7.0)
it3 = ItemNotaFiscal(3, 3, 1, p3)

p4 = Produto(4, 641, "Copo descartável", 1.0)
it4 = ItemNotaFiscal(4, 4, 5, p4)

# Criando nota fiscal
nf = NotaFiscal(1, 100, cli)

# Adicinando itens na nota fiscal
nf.adicionarItem(it1)
nf.adicionarItem(it2)
nf.adicionarItem(it3)
nf.adicionarItem(it4)

# Calculando preço da nota fiscal
nf.calcularNotaFiscal()

# Imprimindo nota fiscal
nf.imprimirNotaFiscal()
