from flask import Flask, request, jsonify

app = Flask(__name__)

# -------------------
# CALCULADORA
# -------------------

@app.route('/dividir', methods=['POST'])
def dividir():

    dados = request.json

    numero1 = dados.get('numero1')
    numero2 = dados.get('numero2')

    if numero2 == 0:
        return jsonify({
            "erro": "Não é possível dividir por zero"
        }), 400

    resultado = numero1 / numero2

    return jsonify({
        "resultado": resultado
    }), 200


@app.route('/multiplicar', methods=['POST'])
def multiplicar():

    dados = request.json

    numero1 = dados.get('numero1')
    numero2 = dados.get('numero2')

    resultado = numero1 * numero2

    return jsonify({
        "resultado": resultado
    }), 200


# -------------------
# USUÁRIOS
# -------------------

@app.route('/usuarios', methods=['POST'])
def usuarios():

    dados = request.json

    if not dados:
        return jsonify({
            "erro": "JSON inválido"
        }), 400

    return jsonify({
        "mensagem": "Usuário recebido com sucesso"
    }), 200


# -------------------
# PRODUTOS
# -------------------

produtos = [
    {"id": 1, "nome": "Camiseta", "categoria": "vestuario"},
    {"id": 2, "nome": "Notebook", "categoria": "tecnologia"},
    {"id": 3, "nome": "Calça", "categoria": "vestuario"}
]

@app.route('/produtos', methods=['GET'])
def listar_produtos():

    categoria = request.args.get('categoria')

    if categoria:
        filtrados = [
            produto for produto in produtos
            if produto['categoria'] == categoria
        ]

        return jsonify(filtrados)

    return jsonify(produtos)


# -------------------
# STATUS
# -------------------

@app.route('/status', methods=['GET'])
def status():

    return jsonify({
        "status": "API funcionando"
    })


# -------------------

if __name__ == '__main__':
    app.run(debug=True)