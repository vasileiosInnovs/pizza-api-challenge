from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from server.models import db
from flask_migrate import Migrate
from server.controllers import register_all_routes
from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("FLASK_SQLALCHEMY_DATABASE_URI")

db.init_app(app)
migration = Migrate(app, db)

register_all_routes(app)

@app.route('/')
def index():
    return "Index for Restaurant/pizza/restaurant pizza."


conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)



if __name__ == '__main__':
    app.run(port=5555, debug=True)