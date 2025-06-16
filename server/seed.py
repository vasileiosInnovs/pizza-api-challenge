from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

with app.app_context():

    RestaurantPizza.query.delete()
    Pizza.query.delete()
    Restaurant.query.delete()

    r1 = Restaurant(name="Pizza Palace", address="123 Main St")
    r2 = Restaurant(name="Slice Haven", address="456 Elm Ave")
    r3 = Restaurant(name="Mozza House", address="789 Pine Rd")

    db.session.add_all([r1, r2, r3])
    db.session.commit()

    
    p1 = Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil")
    p2 = Pizza(name="Pepperoni", ingredients="Tomato, Mozzarella, Pepperoni")
    p3 = Pizza(name="Veggie", ingredients="Tomato, Mozzarella, Bell Peppers, Olives, Onion")

    db.session.add_all([p1, p2, p3])
    db.session.commit()

    rp1 = RestaurantPizza(price=10, restaurant_id=r1.id, pizza_id=p1.id)
    rp2 = RestaurantPizza(price=12, restaurant_id=r1.id, pizza_id=p2.id)
    rp3 = RestaurantPizza(price=11, restaurant_id=r2.id, pizza_id=p3.id)
    rp4 = RestaurantPizza(price=9, restaurant_id=r3.id, pizza_id=p1.id)

    db.session.add_all([rp1, rp2, rp3, rp4])
    db.session.commit()

    print("Done seeding!")
