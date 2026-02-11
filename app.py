from flask import Flask
from flask_cors import CORS
from config import Config
from db import db
from api.identity_routes import identity_bp
from api.experience_routes import experience_bp
from api.ledger_routes import ledger_bp

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

db.init_app(app)

# Import models to ensure they are registered with SQLAlchemy
from .domain import identity, experience, block

with app.app_context():
    db.create_all()

# Register blueprints
app.register_blueprint(identity_bp, url_prefix='/api')
app.register_blueprint(experience_bp, url_prefix='/api')
app.register_blueprint(ledger_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
