from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required
from models.item import ItemModel
from schemas.item import ItemSchema, ItemCountSchema
# from marshmallow import ValidationError # No se necesita porque se implementa a nivel de aplicación.

NAME_ALREADY_EXISTS = "An item with name '{}' already exists."
ERROR_INSERTING = "An error occurred while inserting the item."
ITEM_NOT_FOUND = "Item not found."
ITEM_DELETED = "Item deleted."


item_schema = ItemSchema()
item_list_schema = ItemSchema(many=True)
item_count_schema = ItemCountSchema  # ADD


class Item(Resource):
    @classmethod
    def get(cls, name: str):
        item = ItemModel.find_by_name(name)
        print(item)
        if not item:
            return {"message": ITEM_NOT_FOUND}, 404
        return item_schema.dump(item), 200

    @classmethod
    @jwt_required(fresh=True)
    def post(cls, name: str):
        if ItemModel.find_by_name(name):
            return {"message": NAME_ALREADY_EXISTS.format(name)}, 400

        item_json = request.get_json()
        item_json['name'] = name

        # Se puede sacar porque se configuró la gestión de errores a nivel de app.py
        # Con @app.errorhandler(ValidationError)
        # try:
        #     item = item_schema.load(item_json)
        # except ValidationError as err:
        #     return err.messages, 400
        item = item_schema.load(item_json)

        try:
            item.save_to_db()
        except:
            return {"message": ERROR_INSERTING}, 500

        return item_schema.dump(item), 201

    @classmethod
    @jwt_required()
    def delete(cls, name: str):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {"message": ITEM_DELETED}, 200
        return {"message": ITEM_DELETED}, 404

    @classmethod
    def put(cls, name: str):
        
        item_json = request.get_json()
        item = ItemModel.find_by_name(name)

        if item:
            item.price = item_json['price']
        else:
            # try:
            #     item_json['name'] = name
            #     item_json = item_schema.load(item_json)
            # except ValidationError as err:
            #     return err.messages, 400
            item_json['name'] = name
            item_json = item_schema.load(item_json)
        
        item = item_json.save_to_db()

        return item_schema.dump(item), 200


class ItemList(Resource):
    @classmethod
    def get(cls):
        # return {"items": [item.json() for item in ItemModel.find_all()]}, 200
        return {"items": item_list_schema.dump(ItemModel.find_all())}, 200

class ItemCount(Resource):
    @classmethod
    def get(cls):
        return  {"total_items": item_count_schema.dump(ItemModel.get_count())}
