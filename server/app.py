from flask import Flask
from models import db
from flask_migrate import Migrate
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config.from_prefixed_env()

db.init_app(app)
migration = Migrate(app, db)

if __name__ == '__main__':
    app.run(port=5555, debug=True)