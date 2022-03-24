from db import db
# from sqlalchemy import func

class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    price = db.Column(db.Float(precision=2), nullable=False)

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'), nullable=False)
    store = db.relationship('StoreModel')

    @classmethod
    def find_by_name(cls, name:str) -> 'ItemModel':
        return cls.query.filter_by(name=name).first()
    
    @classmethod
    def find_all(cls) -> list['ItemModel']:
        return cls.query.all()
    
    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
    
    # @staticmethod
    # def get_count():
    #     # return db.session.query(func.count(ItemModel.id)).scalar()
    #     return db.session.query(ItemModel.id).count()

    @classmethod
    def get_count(cls):
        # return db.session.query(func.count(ItemModel.id)).scalar()
        return cls.query.count()
