from flask import request, jsonify, make_response
from server.models import Restaurant, db

def register_restaurant_routes(app):

    @app.route('/restaurants')
    def get_restaurants():

        restaurants = Restaurant.query.all()

        restaurants_list = [restaurant.to_dict() for restaurant in restaurants]

        response = make_response(
            jsonify(restaurants_list),
            200,
        )

        return response

    @app.route('/restaurants/<int:id>', methods=['GET', 'DELETE'])
    def restaurant_by_id(id):
        restaurant = Restaurant.query.get(id)

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
                "message": "Restaurant deleted."
            }

            response = make_response(
                jsonify(response_body),
                200
            )

            return response