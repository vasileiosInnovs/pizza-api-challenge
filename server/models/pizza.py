from . import db

class Pizza(db.Model):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    ingredients = db.Column(db.String())

    restaurant_pizza = db.relationship('RestaurantPizza', back_populates="pizza")

    def __repr__(self):
        return f'<{self.id}, {self.name}, {self.ingredients}'
