# Esto ya no se necesita porque Flask-Marshamallow lo unifica con 
# El user model

# from marshmallow import Schema, fields


# class UserSchema(Schema):
    # class Meta:
    #     load_only = ('password',)
    #     dump_only = ('id',)
    # id = fields.Int() # SQLAlchemy le va a poner el valor
    # username = fields.Str(required=True)
    # password = fields.Str(required=True)

from ma import ma  
from models.user import UserModel

# Crea los fields de marshamallow basado en las definiciones hechas en los modelos
# Para indicar si un campo es requerido se debe hacer colocando nullable=False en el modelo
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_only = ('password',)
        dump_only = ('id',)
        load_instance = True
