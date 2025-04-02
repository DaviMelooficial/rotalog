from flask import request, jsonify  
from ..extensions import db  
from ..models import cliente
from validate_docbr import CNPJ, CEP  
from app import app

@app.route('/clientes', methods=['POST'])  #FUNÇÃO DE CADASTRO.
def cadastrar_cliente():  
    try:  
        dados = request.get_json()  

        # Validações iniciais  
        if not dados.get('cnpj') or not dados.get('email'):  
            return jsonify({"erro": "CNPJ e e-mail são obrigatórios"}), 400  

        if not CNPJ().validate(dados['cnpj']):  
            return jsonify({"erro": "CNPJ inválido"}), 400  

        if not CEP().validate(dados['cep']):  
            return jsonify({"erro": "CEP inválido"}), 400  
        
        # Verifica se CNPJ já existe
        cliente_existente = cliente.query.filter_by(cnpj=dados['cnpj']).first()
        if cliente_existente:
            return jsonify({
                "erro": "CNPJ já cadastrado",
                "id_existente": cliente_existente.id,
                "razao_social_existente": cliente_existente.razao_social
            }), 409  # HTTP 409 Conflict

        # Cria o cliente  
        novo_cliente = cliente(  
            cnpj=dados['cnpj'],  
            razao_social=dados['razao_social'],  
            nome_fantasia=dados.get('nome_fantasia'),  
            email=dados['email'],  
            telefone=dados['telefone'],  
            logradouro=dados['logradouro'],  
            bairro=dados['bairro'],  
            cidade=dados['cidade'],  
            estado=dados['estado'],  
            cep=dados['cep'],  
            inscricao_estadual=dados.get('inscricao_estadual'),  
            status=True  
        )  

        db.session.add(novo_cliente)  
        db.session.commit()  

        return jsonify({  
            "mensagem": "Cliente cadastrado com sucesso!",  
            "id": novo_cliente.id  
        }), 201  

    except Exception as e:  
        db.session.rollback()  
        return jsonify({"erro": str(e)}), 500  
    
#______________________________________________________________________________________

@app.route('/clientes', methods=['GET'])  #FUNÇÃO DE CONSULTA
@app.route('/clientes/<int:id>', methods=['GET'])  
def consultar_clientes(id=None):  
    try:  
        if id:  # Consulta específica  
            cliente = cliente.query.get(id)  
            if not cliente:  
                return jsonify({"erro": "Cliente não encontrado"}), 404  

            return jsonify({  
                "id": cliente.id,  
                "razao_social": cliente.razao_social,  
                "cnpj": cliente.cnpj,  
                "email": cliente.email,  
                "status": cliente.status  
            }), 200  

        else:  # Lista todos (com paginação opcional)  
            clientes = cliente.query.filter_by(status=True).all()  
            return jsonify([{  
                "id": c.id,  
                "razao_social": c.razao_social,  
                "cnpj": c.cnpj  
            } for c in clientes]), 200  

    except Exception as e:  
        return jsonify({"erro": str(e)}), 500  