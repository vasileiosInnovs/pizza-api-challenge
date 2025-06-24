from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from server.models import db
from flask_migrate import Migrate
from server.controllers import register_all_routes
from dotenv import load_dotenv
import os
import psycopg2
from server.controllers import (
    get_restaurants,
    restaurant_by_id,
    get_pizzas,
    post_restaurant_pizzas
)

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("FLASK_SQLALCHEMY_DATABASE_URI")

db.init_app(app)
migration = Migrate(app, db)

@app.route('/restaurants', methods=['GET'])
def handle_get_restaurants():
    return get_restaurants()

@app.route('/restaurants/<int:id>', methods=['GET'])
def handle_get_restaurant(id):
    return restaurant_by_id(id)

@app.route('/restaurants/<int:id>', methods=['DELETE'])
def handle_delete_restaurant(id):
    return restaurant_by_id(id)

@app.route('/pizzas', methods=['GET'])
def handle_get_pizzas():
    return get_pizzas()

@app.route('/restaurant_pizzas', methods=['POST'])
def handle_create_restaurant_pizza():
    return post_restaurant_pizzas()


conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)



if __name__ == '__main__':
    app.run(port=5555, debug=True)