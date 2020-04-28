from flask import Flask
from app import api_bp
from flask_cors import CORS

app = Flask(__name__)

def create_app(config_filename):
    app.config.from_object(config_filename)
    
    app.register_blueprint(api_bp, url_prefix='/')

    return app


if __name__ == "__main__":
    app = create_app("config")
    cors = CORS(app, resources={r"/*": {"origins": "*"}})
    app.run(debug=True)