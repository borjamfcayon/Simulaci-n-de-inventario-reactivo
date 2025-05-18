import graphene
from graphene import ObjectType, Int, Float, String, Boolean, List, Field
from db import products_db

class ProductType(ObjectType):
    id = Int()
    name = String()
    price = Float()
    stock = Int()
    available = Boolean()

class Query(ObjectType):
    products = List(ProductType)

    def resolve_products(self, info):
        return products_db

class ModifyStock(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
        stock = Int(required=True)

    product = Field(lambda: ProductType)

    def mutate(self, info, id, stock):
        for product in products_db:
            if product["id"] == id:
                product["stock"] += stock

                if product["stock"] <= 0:
                    product["stock"] = 0
                    product["available"] = False
                else:
                    product["available"] = True

                return ModifyStock(product=product)

        raise Exception("Producto no encontrado")

class Mutation(ObjectType):
    modify_stock = ModifyStock.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)