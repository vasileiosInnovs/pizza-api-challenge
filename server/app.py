from flask import Flask, jsonify, make_response, request
from flask_sqlalchemy import SQLAlchemy
from models import db, Restaurant, Pizza, RestaurantPizza
from flask_migrate import Migrate
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config.from_prefixed_env()

db.init_app(app)
migration = Migrate(app, db)

@app.route('/')
def index():
    return "Index for Restaurant/pizza/restaurant pizza."

@app.route('/restaurants')
def restaurants():

    restaurants = Restaurant.query.all()

    restaurants_list = [restaurant.to_dict() for restaurant in restaurants]

    response = make_response(
        restaurants_list,
        200,
        {"Content-Type": "application/json"}
    )

    return response

@app.route('/restaurants/<int:id>', method=['GET', 'DELETE'])
def restaurant_by_id(id):
    restaurant = Restaurant.query.filter(Restaurant.id == id).first()

    if request.method == 'GET':
        if restaurant:
            response = make_response(
                jsonify(restaurant.to_dict()),
                200
            )
        else:
            response = make_response(
                jsonify({"error": "Restaurant not found"}),
                404
            )

        return response
    
    elif request.method == 'DELETE':
        db.session.delete(restaurant)
        db.session.commit()

        response_body = {
            "delete_successful": True,
            "message": "Review deleted."
        }

        response = make_response(
            response_body,
            200
        )

        return response

@app.route('/pizzas')
def get_pizza():

    pizzas = Pizza.query.all()

    pizza_list = [pizza.to_dict() for pizza in pizzas]

    response = make_response(
        jsonify(pizza_list),
        200
    )

if __name__ == '__main__':
    app.run(port=5555, debug=True)