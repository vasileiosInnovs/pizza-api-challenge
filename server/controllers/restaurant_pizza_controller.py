from flask import make_response, request, jsonify
from server.models import RestaurantPizza, db, Pizza, Restaurant

def register_restaurant_pizza_routes(app):

    @app.route('/restaurant-pizzas', methods=['POST'])
    def post_restaurant_pizzas():
        data = request.get_json()

        try:
            price = int(data.get("price"))
        except (TypeError, ValueError):
            return jsonify({"error": "Price must be an integer"}), 400

        pizza_id = data.get("pizza_id")
        restaurant_id = data.get("restaurant_id")

        if not (1 <= price <= 30):
            return jsonify(
                {"error": "Price must be between 1 and 30"},
                400
            )

        pizza = Pizza.query.get(pizza_id)
        restaurant = Restaurant.query.get(restaurant_id)

        if not pizza or not restaurant:
            return jsonify(
                {"error": "Invalid pizza or restaurant ID"},
                404            
            )

        new_rp = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)

        db.session.add(new_rp)
        db.session.commit()

        return make_response(
            jsonify(new_rp.to_dict()), 
            201
        )