import config
from flask import Flask

app = Flask(__name__)
app.config.from_object(config)

from exts import db
db.init_app(app)

from blueprints.index import bp as index_bp
from blueprints.auth import bp as auth_bp
from blueprints.user import bp as user_bp

app.register_blueprint(index_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)

from flask_migrate import Migrate
from models import User

migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)