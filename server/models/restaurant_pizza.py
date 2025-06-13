from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s"
})

db = SQLAlchemy(metadata=metadata)

class RestaurantPizza(db.Model):
    __tablename__ = "restaurantpizzas"

    id = db.Column(db.Integer(), primary_key=True)
    price = db.Column(db.Integer())
    restaurant_id = db.Column(db.Integer(), db.ForeignKey('restaurants.id'))
    pizza_id = db.Column(db.Integer(), db.ForeignKey('pizzas.id'))

    pizza = db.relationship('Pizza', back_populates="restaurantpizza", cascade='all, delete-orphan')
    restaurant = db.relationship('Restaurant', back_populates="restaurantpizza", cascade='all, delete-orphan')

    def __repr__(self):
        return f'<{self.id}, Price:{self.price}, Restaurant:{self.restaurant_id}, Pizza:{self.pizza_id}>'