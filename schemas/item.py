from ma import ma
from models.item import ItemModel
from models.store import StoreModel


class ItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=ItemModel
        load_instance=True
        # Esto representa a la relación, lo que resulta redundante con store_id
        load_only = ('store',)
        dump_only = ('id',)
        # Necesario para tener la información para unir las tablas.
        include_fk = True
