from flask import request
from Avaliação.Atividade06.app import app
from Avaliação.Atividade06.app.controller import obj_json, resposta, selecionar
from Avaliação.Atividade06.app.models import usuarios
from Avaliação.Atividade06.app.models.user import User
from Avaliação.Atividade06.app.models import produtos
from Avaliação.Atividade06.app.models.produto import Produto
from Avaliação.Atividade06.app.models import notas
from Avaliação.Atividade06.app.models.nota_fiscal import NotaFiscal
from Avaliação.Atividade06.app.models import itens
from Avaliação.Atividade06.app.models.item_nota_fiscal import ItemNotaFiscal


# ROTAS CLIENTE
@app.route("/users", methods=["GET"])
def users():
    print(usuarios)
    json_usuarios = obj_json(usuarios)
    print(json_usuarios)
    return resposta(200, 'usuarios', json_usuarios, 'Todos os usuarios')


@app.route('/user/<int:id_user>', methods=["GET"])
def ler_cliente(id_user):
    try:
        usuario = selecionar(usuarios, id_user)
        usuario_json = obj_json(usuario)

        return resposta(200, 'usuario', usuario_json, 'Cliente selecionado')
    except Exception as e:
        print(e)
        return resposta(400, 'usuario', {}, 'ID inválido')


@app.route('/user', methods=["POST"])
def criar_cliente():
    try:
        body = request.json

        usuario = User(usuarios[-1].get_id() + 1, body['nome'], body['codigo'], body['cpf'], 'pessoa fisica')
        usuarios.append(usuario)
        usuario_json = obj_json(usuario)

        return resposta(201, 'cliente', usuario_json, 'Cliente criado')
    except Exception as e:
        print(e)
        return resposta(400, 'usuario', {}, 'Usuario não criado')


@app.route('/user/<int:id_user>', methods=["PUT"])
def atualizar_cliente(id_user):
    try:
        body = request.json
        usuario = selecionar(usuarios, id_user)

        usuario.set_nome(body['nome'])
        usuario.set_codigo(body['codigo'])
        usuario.set_cnpjcpf(body['cpf'])

        usuario_json = obj_json(usuario)
        return resposta(200, 'usuario', usuario_json, 'Usuario atualizado')
    except Exception as e:
        print(e)
        return resposta(400, 'usuario', {}, 'Usuario não atualizado')


@app.route('/user/<int:id_user>', methods=["DELETE"])
def deletar_cliente(id_user):
    try:
        usuario = selecionar(usuarios, id_user)
        usuarios.remove(usuario)

        usuario_json = obj_json(usuario)
        return resposta(200, 'usuario', usuario_json, 'Usuario deletado')
    except Exception as e:
        print(e)
        return resposta(400, 'usuario', {}, 'Usuario não deletado')


# ROTAS PRODUTO
@app.route('/produtos', methods=["GET"])
def todos_produtos():
    protudos_json = obj_json(produtos)

    return resposta(200, 'produtos', protudos_json, 'Todos os produtos')


@app.route('/produto/<int:id_produto>', methods=["GET"])
def ver_produto(id_produto):
    try:
        produto = selecionar(produtos, id_produto)
        produto_json = obj_json(produto)

        return resposta(200, 'produto', produto_json, 'Produto selecionado')
    except Exception as e:
        print(e)
        return resposta(400, 'produto', {}, 'ID inválido')


@app.route('/produto', methods=["POST"])
def criar_produto():
    try:
        body = request.json

        produto = Produto(produtos[-1].get_id() + 1, body['codigo'], body['descricao'], body['valor-unitario'])
        produtos.append(produto)
        produto_json = obj_json(produto)

        return resposta(201, 'produto', produto_json, 'Produto criado')
    except Exception as e:
        print(e)
        return resposta(400, 'produto', {}, 'Produto não criado')


@app.route('/produto/<int:id_produto>', methods=["PUT"])
def atualizar_produto(id_produto):
    try:
        body = request.json
        produto = selecionar(produtos, id_produto)

        produto.set_codigo(body['codigo'])
        produto.set_descricao(body['descricao'])
        produto.set_valor_unitario(body['valor-unitario'])

        produto_json = obj_json(produto)
        return resposta(200, 'produto', produto_json, 'Produto atualizado')
    except Exception as e:
        print(e)
        return resposta(400, 'produto', {}, 'Produto não atualizado')


@app.route('/produto/<int:id_produto>', methods=["DELETE"])
def deletar_produto(id_produto):
    try:
        produto = selecionar(produtos, id_produto)
        produtos.remove(produto)

        produto_json = obj_json(produto)
        return resposta(200, 'produto', produto_json, 'Produto deletado')
    except Exception as e:
        print(e)
        return resposta(400, 'produto', {}, 'Produto não deletado')


# ROTAS NOTA FISCAL
@app.route('/notas', methods=["GET"])
def todas_notas():
    notas_json = obj_json(notas)

    return resposta(200, 'notas', notas_json, 'Todos as notas')


@app.route('/nota/<int:id_nota>', methods=["GET"])
def ver_nota(id_nota):
    try:
        nota = selecionar(notas, id_nota)
        nota_json = obj_json(nota)

        return resposta(200, 'nota', nota_json, 'Nota selecionada')
    except Exception as e:
        print(e)
        return resposta(400, 'nota', {}, 'ID inválido')


@app.route('/notafiscal', methods=["POST"])
def criar_nota():
    try:
        body = request.json

        cliente = selecionar(usuarios, body['cliente'])
        nota = NotaFiscal(notas[-1].get_id() + 1, body['codigo'], cliente)
        notas.append(nota)

        nota_json = obj_json(nota)
        return resposta(201, 'nota', nota_json, 'Nota criada')
    except Exception as e:
        print(e)
        return resposta(400, 'nota', {}, 'Nota não criada')


@app.route('/nota/<int:id_nota>', methods=["PUT"])
def atualizar_nota(id_nota):
    try:
        body = request.json
        nota = selecionar(notas, id_nota)
        cliente = selecionar(usuarios, body['cliente'])
        nota.set_codigo(body['codigo'])
        nota.setCliente(cliente)

        nota_json = obj_json(nota)
        return resposta(200, 'nota', nota_json, 'Nota atualizada')
    except Exception as e:
        print(e)
        return resposta(400, 'nota', {}, 'Nota não atualizada')


@app.route('/nota/<int:id_nota>', methods=["DELETE"])
def deletar_nota(id_nota):
    try:
        nota = selecionar(notas, id_nota)
        notas.remove(nota)

        nota_json = obj_json(nota)
        return resposta(200, 'nota', nota_json, 'Nota deletada')
    except Exception as e:
        print(e)
        return resposta(400, 'nota', {}, 'Nota não deletada')


@app.route('/calcularnota/<int:id_nota>', methods=["GET"])
def calcular_nota(id_nota):
    try:
        nota = selecionar(notas, id_nota)
        nota.calcularNotaFiscal()

        nota_json = obj_json(nota)
        return resposta(200, 'nota', nota_json, 'Nota calculada')

    except Exception as e:
        print(e)
        return resposta(400, 'nota', {}, 'Nota não calculada')


@app.route('/imprimirnota/<int:id_nota>', methods=["GET"])
def imprimir_nota(id_nota):
    try:
        nota = selecionar(notas, id_nota)
        impresso = nota.imprimirNotaFiscal()

        return resposta(200, 'nota', impresso, 'Nota impressa')

    except Exception as e:
        print(e)
        return resposta(400, 'nota', {}, 'Nota não impressa')


# ROTAS ITEM NOTA FISCAL
@app.route('/itens/<int:id_nota>', methods=["GET"])
def todos_itens(id_nota):
    try:
        itens_nota = selecionar(notas, id_nota).get_itens()
        itens_json = obj_json(itens_nota)

        return resposta(200, 'itens', itens_json, 'Todos os itens da nota')
    except Exception as e:
        print(e)
        return resposta(400, 'itens', {}, 'ID inválido')


@app.route('/item/<int:id_item>', methods=["GET"])
def ver_item(id_item):
    try:
        item = selecionar(itens, id_item)
        item_json = obj_json(item)

        return resposta(200, 'itens', item_json, 'Itens da nota')
    except Exception as e:
        print(e)
        return resposta(400, 'itens', {}, 'ID inválido')


@app.route('/item', methods=["POST"])
def criar_item():
    try:
        body = request.json
        produto = selecionar(produtos, body['produto'])
        item = ItemNotaFiscal(itens[-1].get_id() + 1, body['sequencial'], body['quantidade'], produto)
        itens.append(item)
        item_json = obj_json(item)

        return resposta(201, 'item', item_json, 'Item criado')
    except Exception as e:
        print(e)
        return resposta(400, 'item', {}, 'Item não criado')


@app.route('/item/<int:id_item>', methods=["PUT"])
def atualizar_item(id_item):
    try:
        body = request.json
        item = selecionar(itens, id_item)

        item.set_sequencial(body['sequencial'])
        item.set_quantidade(body['quantidade'])

        item_json = obj_json(item)
        return resposta(200, 'item', item_json, 'Item atualizado')
    except Exception as e:
        print(e)
        return resposta(400, 'item', {}, 'Item não atualizado')


@app.route('/item/<int:id_item>', methods=["DELETE"])
def deletar_item(id_item):
    try:
        item = selecionar(itens, id_item)
        itens.remove(item)

        item_json = obj_json(item)
        return resposta(200, 'item', item_json, 'Item deletado')
    except Exception as e:
        print(e)
        return resposta(400, 'item', {}, 'Item não deletado')
