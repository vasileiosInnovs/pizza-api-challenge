from . import db
from sqlalchemy_serializer import SerializerMixin

class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    ingredients = db.Column(db.String())

    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates="pizza", cascade="all, delete-orphan")
    
    serialize_rules = ('-restaurant_pizzas.pizza',)

    def __repr__(self):
        return f'<{self.id}, {self.name}, {self.ingredients}>'
