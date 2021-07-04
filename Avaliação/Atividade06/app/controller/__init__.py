import json
from flask import Response


def obj_json(objeto):
    if isinstance(objeto, list):
        atual = []
        for objeto in objeto:
            atual.append(objeto.dicionario())
        return atual
    else:
        return objeto.dicionario()


def resposta(status, nome, conteudo, msg='', nome_secundario='', conteudo_secundario=None):
    corpo = {nome: conteudo}

    if conteudo_secundario:
        corpo[nome_secundario] = conteudo_secundario
    if msg:
        corpo['msg'] = msg

    return Response(json.dumps(corpo), status=status, mimetype="api/json")


def selecionar(lista, obj_id):
    return [x for x in lista if x.get_id() == obj_id][0]
