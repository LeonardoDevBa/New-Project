from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notasbd.bd'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Diario(db.Model):
    __tablename__ = 'darios'
    data = db.Column(db.DateTime, primary_key=True)
    titulo = db.Column(db.String, nullable=False)
    texto = db.Column(db.String, nullable=False)

db.create_all()

@app.route('/anotacoes', methods=['GET'])
def get_anotacoes():
    anotacoes = Diario.query.all()
    return jsonify([{
        'data': anotacao.data.strftime('%Y-%m-%d'),
        'titulo': anotacao.titulo,
        'texto': anotacao.texto
    } for anotacao in anotacoes])

@app.route('/anotacoes/<string:data>', methods=['GET'])
def get_anotacao(data):
    data_time = datetime.strptime(data, '%Y-%m-%d')
    anotacao = Diario.query.filter_by(data=data_time).first()
    if anotacao:
        return jsonify({
            'data': anotacao.data.strftime('%Y-%m-%d'),
            'titulo': anotacao.titulo,
            'texto': anotacao.texto
        })
    return jsonify({'message': 'Anotação não encontrada'}), 404

@app.route('/anotacoes', methods=['POST'])
def criar_anotacao():
    data = request.json.get('data')
    titulo = request.json.get('titulo')
    texto = request.json.get('texto')
    data_time = datetime.strptime(data, '%Y-%m-%d')

    nova_anotacao = Diario(data=data_time, titulo=titulo, texto=texto)
    db.session.add(nova_anotacao)
    db.session.commit()
    
    return jsonify({'message': 'Anotação criada com sucesso!'}), 201

@app.route('/anotacoes/<string:data>', methods=['DELETE'])
def excluir_anotacao(data):
    data_time = datetime.strptime(data, '%Y-%m-%d')
    anotacao = Diario.query.filter_by(data=data_time).first()
    if anotacao:
        db.session.delete(anotacao)
        db.session.commit()
        return jsonify({'message': 'Anotação excluída com sucesso!'})
    return jsonify({'message': 'Anotação não encontrada'}), 404

if __name__ == '__main__':
    app.run(debug=True)
