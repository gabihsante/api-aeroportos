from flask import Blueprint, make_response, jsonify, request

from app import db
from app.models.aeroportos import Aeroporto
from app.models.aeroportos_schema import AeroportoSchema

class AeroportoController:

    aeroporto_controller = Blueprint(name='aeroporto_cotroller', import_name=__name__)

    @aeroporto_controller.route('/api/v1/aeroportos', methods=['GET'])
    def index():
        lista_de_aeroportos = Aeroporto.query.all()
        aeroportos_schema = AeroportoSchema(many=True)
        aeroportos = aeroportos_schema.dump(lista_de_aeroportos)

        return make_response(jsonify({
            "aeroportos": aeroportos
        }))
    @aeroporto_controller.route('/api/v1/aeroportos/<iata>', methods=['GET'])
    def get_aeroporto(iata):

        aeroporto = Aeroporto.query.filter_by(iata).first()
        aeroporto_schema = AeroportoSchema()
        aeroportos = aeroporto_schema.dump(aeroporto)

        return make_response(jsonify({
            "aeroportos": aeroportos
        }))
    @aeroporto_controller.route('/api/v1/aeroportos', methods=['POST'])
    def create():
        dados = request.get_json()
        aeroporto_schema = AeroportoSchema()
        aeroporto = aeroporto_schema.load(dados)

        print(aeroporto)

        resultado = aeroporto_schema.dump(aeroporto.create())

        return make_response(jsonify({
            "produtos": resultado
        }), 201)

    @aeroporto_controller.route('/api/v1/aeroportos/<iata>', methods=['DELETE'])
    def delete(iata):
        aeroporto = Aeroporto.query.filter_by(iata).first()
        db.session.delete(aeroporto)
        db.session.commit()
        return make_response(jsonify({}), 204)

    @aeroporto_controller.route('/api/v1/aeroportos/<iata>', methods=['PUT'])
    def update(iata):

        aeroporto = Aeroporto.query.filter_by(iata).first()
        dados = request.get_json()
        aeroporto_schema = AeroportoSchema()

        if dados.get('nome_aeroporto'):
            aeroporto.nome_aeroporto = dados['nome_aeroporto']

        if dados.get('codigo_iata'):
            aeroporto.codigo_iata = dados['codigo_iata']

        if dados.get('cidade'):
            aeroporto.cidade = dados['cidade']

        if dados.get('codigo_pais_iso'):
            aeroporto.codigo_pais_iso = dados['codigo_pais_iso']

        if dados.get('latitude'):
            aeroporto.latitude = dados['latitude']

        if dados.get('longitude'):
            aeroporto.longitude = dados['longitude']

        if dados.get('altitude'):
            aeroporto.altitude = dados['altitude']

        db.session.add(aeroporto)
        db.session.commit()

        aeroporto_atualizado = aeroporto_schema.dump(aeroporto)

        return make_response(jsonify({
            "aeroportos": aeroporto_atualizado
        }), 200)