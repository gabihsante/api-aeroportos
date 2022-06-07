from app import ma,db
from app.models.aeroportos import Aeroporto

class AeroportoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Aeroporto
        sqla_session = db.session
        load_instance = True

    id_aeroporto = ma.auto_field()
    nome_aeroporto = ma.auto_field()
    codigo_iata = ma.auto_field()
    cidade = ma.auto_field()
    codigo_pais_iso = ma.auto_field()
    latitude = ma.auto_field()
    longitude = ma.auto_field()
    altitude = ma.auto_field()