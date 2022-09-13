from flask import Flask
from flask_cors import CORS


if __name__ == "__main__":
    app = Flask(__name__)
    CORS(app, supports_credentials=True)

    from app.index import index as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/')

    app.run(host="0.0.0.0", port=5000, debug=True)

