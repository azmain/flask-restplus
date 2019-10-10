from flask import Flask
from flask_pymongo import PyMongo

from apis import api

app = Flask(__name__)

# app.config["MONGO_URI"] = "mongodb://localhost:27017/nishan"

# mongo = PyMongo(app)

api.init_app(app)




if __name__ == "__main__":
    app.run(debug=True)
