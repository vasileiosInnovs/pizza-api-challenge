from . import db

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    address = db.Column(db.String())

    restaurant_pizza = db.relationship('RestaurantPizza', back_populates="restaurant", cascade='all, delete-orphan')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address
        }

    def __repr__(self):
        return f'<{self.id}, {self.name}, {self.address}>'
