from ma import ma
from models.store import StoreModel
from models.item import ItemModel
from schemas.item import ItemSchema

class StoreSchema(ma.SQLAlchemyAutoSchema):
    # Necesario para una relación donde hay muchos items por store
    # Implicitamente indica que es algo que se va a dumpear en lugar de hacer un load
    items = ma.Nested(ItemSchema, many=True)
    
    class Meta:
        model=StoreModel
        load_instance=True
        dump_only = ('id',)
        # Necesario para tener la información para unir las tablas.
        include_fk = True
