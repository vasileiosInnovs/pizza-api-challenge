from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    address = db.Column(db.String())

    restaurantpizzas = db.relationship('RestaurantPizza', back_populates="restaurant", cascade='all, delete-orphan')

    def __repr__(self):
        return f'<{self.id}, {self.name}, {self.address}>'
