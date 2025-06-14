from . import db

class RestaurantPizza(db.Model):
    __tablename__ = "restaurantpizzas"

    id = db.Column(db.Integer(), primary_key=True)
    price = db.Column(db.Integer())
    restaurant_id = db.Column(db.Integer(), db.ForeignKey('restaurants.id'))
    pizza_id = db.Column(db.Integer(), db.ForeignKey('pizzas.id'))

    pizza = db.relationship('Pizza', back_populates="restaurantpizza")
    restaurant = db.relationship('Restaurant', back_populates="restaurantpizza")

    def __repr__(self):
        return f'<{self.id}, Price:{self.price}, Restaurant:{self.restaurant_id}, Pizza:{self.pizza_id}>'