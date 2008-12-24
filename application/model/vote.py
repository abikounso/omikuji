from google.appengine.ext import db
from gaeo.model import BaseModel

class Vote(BaseModel):
    name = db.StringProperty(required=True)
    type = db.IntegerProperty(required=True)