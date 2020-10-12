from enum import unique
from app.main import db

# Models for the database tables

class CategoryModel(db.Model):
    __tablename__ = "Categories"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    category_sequence = db.Column(db.Integer)

class SaladModel(db.Model):
    __tablename__ = "Salad"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    item_sequence = db.Column(db.Integer)
    price = db.Column(db.Integer)
    available = db.Column(db.String(50))
    veg = db.Column(db.String(50))
    description = db.Column(db.String(255))

class StartersModel(db.Model):
    __tablename__ = "starters"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    item_sequence = db.Column(db.Integer)
    price = db.Column(db.Integer)
    available = db.Column(db.String(50))
    veg = db.Column(db.String(50))
    description = db.Column(db.String(255))

class BurgersModel(db.Model):
    __tablename__ = "burgers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    item_sequence = db.Column(db.Integer)
    price = db.Column(db.Integer)
    available = db.Column(db.String(50))
    veg = db.Column(db.String(50))
    description = db.Column(db.String(255))

class HotDogsModel(db.Model):
    __tablename__ = "hotdogs"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    item_sequence = db.Column(db.Integer)
    price = db.Column(db.Integer)
    available = db.Column(db.String(50))
    veg = db.Column(db.String(50))
    description = db.Column(db.String(255))

class Desserts(db.Model):
    __tablename__ = "desserts"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    item_sequence = db.Column(db.Integer)
    price = db.Column(db.Integer)
    available = db.Column(db.String(50))
    veg = db.Column(db.String(50))
    description = db.Column(db.String(255))

class Beverages(db.Model):
    __tablename__ = "beverages"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    item_sequence = db.Column(db.Integer)
    price = db.Column(db.Integer)
    available = db.Column(db.String(50))
    veg = db.Column(db.String(50))
    description = db.Column(db.String(255))

