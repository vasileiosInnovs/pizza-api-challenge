from sqlalchemy.orm import validates
from sqlalchemy import CheckConstraint
from . import db

class RestaurantPizza(db.Model):
    __tablename__ = "restaurant_pizzas"

    id = db.Column(db.Integer(), primary_key=True)
    price = db.Column(db.Integer())
    restaurant_id = db.Column(db.Integer(), db.ForeignKey('restaurants.id'))
    pizza_id = db.Column(db.Integer(), db.ForeignKey('pizzas.id'))

    pizza = db.relationship('Pizza', back_populates="restaurant_pizza")
    restaurant = db.relationship('Restaurant', back_populates="restaurant_pizza")

    @validates('price')
    def validate_price(self, key, value):
        if not (1 <= value <= 30):
            raise ValueError("Price must be between 1 and 30")
        return value
    
    __table_args__ = (CheckConstraint('price >= 1 AND price <=30', name='check_price_range'))

    def __repr__(self):
        return f'<{self.id}, Price:{self.price}, Restaurant:{self.restaurant_id}, Pizza:{self.pizza_id}>'