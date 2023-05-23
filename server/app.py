#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():
    bakeries = [bakery.to_dict() for bakery in Bakery.query.all()]

    return make_response(bakeries, 200)

@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    bakery = Bakery.query.filter(Bakery.id == id).first().to_dict()

    return make_response(bakery, 200)

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    goods = [good.to_dict() for good in BakedGood.query.order_by(BakedGood.price.desc()).all()]

    return make_response(goods, 200)

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    most_expensive_good = BakedGood.query.order_by(BakedGood.price.desc()).first().to_dict()

    return make_response(most_expensive_good, 200)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
