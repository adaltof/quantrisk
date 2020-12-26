from flask import Flask
from flask_mongoengine import MongoEngine
import datetime

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

class ThreatCommunity(db.Document):
    name = db.StringField(required=True)
    description = db.StringField(required=False)
    tcapmax = db.IntField(min_value=0, max_value=100)
    tcapmin = db.IntField(min_value=0, max_value=100)
    tcapavg = db.IntField(min_value=0, max_value=100)

class AssetTarget(db.Document):
    name = db.StringField(required=True)
    description = db.StringField(required=False)
    rsmax = db.IntField(min_value=0, max_value=100)
    rsmin = db.IntField(min_value=0, max_value=100)
    rsavg = db.IntField(min_value=0, max_value=100)

class Analysis(db.Document):
    name = db.StringField(required=True)
    description = db.StringField(required=False)
    datecreated = db.DateTimeField(default=datetime.datetime.utcnow)
    lefmax = db.DecimalField(min_value=0, precision=2)
    lefmin = db.DecimalField(min_value=0, precision=2)
    lefavg = db.DecimalField(min_value=0, precision=2)
    tefmax = db.DecimalField(min_value=0, precision=2)
    tefmin = db.DecimalField(min_value=0, precision=2)
    tefavg = db.DecimalField(min_value=0, precision=2)
    cfmax = db.DecimalField(min_value=0, precision=2)
    cfavg = db.DecimalField(min_value=0, precision=2)
    cfmin = db.DecimalField(min_value=0, precision=2)
    vulnmin = db.IntField(min_value=0, max_value=100)
    vulnavg = db.IntField(min_value=0, max_value=100)
    vulnmax = db.IntField(min_value=0, max_value=100)
    tcapmax = db.IntField(min_value=0, max_value=100)
    tcapmin = db.IntField(min_value=0, max_value=100)
    tcapavg = db.IntField(min_value=0, max_value=100)
    rsmax = db.IntField(min_value=0, max_value=100)
    rsmin = db.IntField(min_value=0, max_value=100)
    rsavg = db.IntField(min_value=0, max_value=100)

class TypeofLoss(db.Document):
    name = db.StringField(required=True)
    description = db.StringField(required=False)
    datecreated = db.DateTimeField()


if __name__ == 'main':
    app.run(debug=True)