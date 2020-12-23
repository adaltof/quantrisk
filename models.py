from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db' : 'quantriskdb',
    'host': 'localhost',
    'port': 27017,
    'username': 'quser',
    'password': 'test123123'
}
db = MongoEngine()
db.init_app(app)

class User(db.Document):
    name = db.StringField(required=True)
    email = db.StringField()


if __name__ == 'main':
    app.run(debug=True)