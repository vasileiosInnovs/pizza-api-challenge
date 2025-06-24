from flask import jsonify, make_response
from server.models import Pizza

def register_pizza_routes(app):

    @app.route('/pizzas')
    def get_pizza():

        pizzas = Pizza.query.all()

        pizza_list = [pizza.to_dict() for pizza in pizzas]

        response = make_response(
            jsonify(pizza_list),
            200
        )

        return response