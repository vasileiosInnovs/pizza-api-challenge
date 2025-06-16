from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db
from flask_migrate import Migrate
from controllers import register_all_routes
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config.from_prefixed_env()

db.init_app(app)
migration = Migrate(app, db)

register_all_routes(app)

@app.route('/')
def index():
    return "Index for Restaurant/pizza/restaurant pizza."

if __name__ == '__main__':
    app.run(port=5555, debug=True)