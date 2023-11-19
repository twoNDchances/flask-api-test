from config import db

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def json(self):
        return {'name': self.name, 'age': self.age}