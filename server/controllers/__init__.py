from .restaurant_controller import register_restaurant_routes
from .pizza_controller import register_pizza_routes
from .restaurant_pizza_controller import register_restaurant_pizza_routes

def register_all_routes(app):
    register_restaurant_routes(app)
    register_pizza_routes(app)
    register_restaurant_pizza_routes(app)