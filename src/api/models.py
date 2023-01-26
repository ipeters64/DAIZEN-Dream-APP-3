from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=True, default=True)

    def __repr__(self):
        return f'<User {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Dream(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    meaning = db.Column(db.String(200), unique=True, nullable=False)

    def __repr__(self):
        return '<Dream %r>' % self.meaning

    def serialize(self):
        return {
            "id": self.id,
            "meaning": self.meaning,
            # do not serialize the password, its a security breach
        }     

class Nightmare(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    meaning = db.Column(db.String(200), unique=True, nullable=False)
    
    def __repr__(self):
        return '<Nightmare %r>' % self.meaning

    def serialize(self):
        return {
            "id": self.id,
            "meaning": self.meaning,
            # do not serialize the password, its a security breach
        }     