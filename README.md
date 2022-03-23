# Example of how to perform a query for counting items with flask-marshmallow

Associated to to perform the query

## app

```py
from resources.item import Item, ItemList, ItemCount

...

api.add_resource(ItemCount, "/items/count")
```

## Resources

```py
from schemas.item import ItemSchema, ItemCountSchema

...

item_count_schema = ItemCountSchema  # ADD

...

class ItemCount(Resource):
    @classmethod
    def get(cls):
        return  {"total_items": item_count_schema.dump(ItemModel.get_count())} 
        # Dump does not work because we have no ItemModel instances returned from the count.
```

## Schemas

```py
...

class ItemCountSchema(ma.Schema):
    class Meta:
        model=ItemModel # Maybe this is not neccesary
        load_instance=False # Not is this
        fields = ("total_items",)

```

## Models

```py
...

@staticmethod
def get_count():
    return db.session.query(func.count(ItemModel.id))
```
