from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
            {'nome':'Giu',
             'habilidade':['Python', 'Flask']
            },
            {'nome':'Cabral',
            'hanilidade':['Python', 'Django']}
]

#devolve um desenvolvedor pelo ID, também altera e deleta um desenvolvedor.
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id] 
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status':'erro', 'mensgaem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status':'erro', 'mensgaem':mensagem}    
        return jsonify(response)
            #return jsonify({'nome':'Giu'})
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method =='DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'sucesso', 'mensagem':'Registro excluido'})
    
#lista todos os desenvolvedores e permite resitrar um novo desenvolvedor
@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method =='POST':
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        return jsonify({'status':'sucesso', 'mensagem':'Registro inserido'})
    elif request.method == 'GET':
        return jsonify(desenvolvedores)

if __name__ == '__main__':
    app.run(debug=True)
