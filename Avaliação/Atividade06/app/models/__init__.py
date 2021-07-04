from Avaliação.Atividade06.app.models.user import User
from Avaliação.Atividade06.app.models.produto import Produto
from Avaliação.Atividade06.app.models.item_nota_fiscal import ItemNotaFiscal
from Avaliação.Atividade06.app.models.nota_fiscal import NotaFiscal

u1 = User(1, 'Beatriz', 100, '123.412.342-14', 'fisica')
u2 = User(2, 'Joana', 200, '233.253.875-48', 'fisica')
u3 = User(3, 'Carlos', 300, '424.758.732-93', 'fisica')
usuarios = [u1, u2, u3]

p1 = Produto(1, 123, 'Banana', 0.5)
p2 = Produto(2, 421, 'Biscoito', 1.5)
p3 = Produto(3, 723, 'Coca-cola 1L', 5.5)
produtos = [p1, p2, p3]

n1 = NotaFiscal(1, 100, u1)
n2 = NotaFiscal(2, 200, u2)
n3 = NotaFiscal(3, 300, u3)
notas = [n1, n2, n3]

# Itens cliente 1
i1 = ItemNotaFiscal(1, 100, 2, p1)
i2 = ItemNotaFiscal(2, 200, 2, p2)
i3 = ItemNotaFiscal(3, 300, 1, p3)

# Itens Cliente 2
i4 = ItemNotaFiscal(4, 200, 1, p2)
i5 = ItemNotaFiscal(5, 300, 1, p3)

# Itens Cliente 3
i6 = ItemNotaFiscal(6, 200, 1, p1)

itens = [i1, i2, i3, i4, i5, i6]

# Adicionar itens nas notas
n1.adicionarItem(i1)
n1.adicionarItem(i2)
n1.adicionarItem(i3)

n2.adicionarItem(i4)
n2.adicionarItem(i5)

n3.adicionarItem(i6)

n1.calcularNotaFiscal()
n2.calcularNotaFiscal()
n3.calcularNotaFiscal()

