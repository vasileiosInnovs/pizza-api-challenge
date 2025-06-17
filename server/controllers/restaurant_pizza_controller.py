from flask import make_response, request, jsonify
from models import RestaurantPizza, db, Pizza, Restaurant

def register_restaurant_pizza_routes(app):

    @app.route('/restaurant-pizzas', methods=['POST'])
    def post_restaurant_pizzas():
        data = request.get_json()

        price = data.get("price")
        pizza_id = data.get("pizza_id")
        restaurant_id = data.get("restaurant_id")

        if not (1 <= int(price) <= 30):
            return jsonify({"error": "Price must be between 1 and 30"}), 400

        if not Pizza.query.get(pizza_id) or not Restaurant.query.get(restaurant_id):
            return jsonify({"error": "Invalid pizza or restaurant ID"}), 404

        new_rp = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)

        db.session.add(new_rp)
        db.session.commit()

        return jsonify(new_rp.to_dict()), 201