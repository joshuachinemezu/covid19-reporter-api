from flask import Flask
from app import api_bp
from flask_cors import CORS

app = Flask(__name__)

app.config.from_object("config")
app.register_blueprint(api_bp, url_prefix='/')
cors = CORS(app, resources={r"/*": {"origins": "*"}})



if __name__ == "__main__":
    app.run(debug=True)