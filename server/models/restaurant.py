from . import db
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    address = db.Column(db.String())

    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates="restaurant", cascade='all, delete-orphan')

    pizzas = association_proxy('restaurant_pizza', 'pizza')

    serialize_rules = ('-restaurant_pizza.restaurant',)

    def __repr__(self):
        return f'<{self.id}, {self.name}, {self.address}>'
