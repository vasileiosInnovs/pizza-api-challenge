from flask import make_response, request
from models import RestaurantPizza, db

def register_restaurant_pizza_routes(app):

    @app.route('/restaurant-pizzas', methods=['POST'])
    def post_restaurant_pizzas():
        new_restaurant_pizza = RestaurantPizza(
            score=request.form.get("price"),
            pizza_id=request.form.get("pizza_id"),
            restaurant_id=request.form.get("restaurant_id"),
        )

        db.session.add(new_restaurant_pizza)
        db.session.commit()

        review_dict = new_restaurant_pizza.to_dict()

        response = make_response(
            review_dict,
            201
        )

        return response