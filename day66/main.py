from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, func
import random

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/random', methods=['GET'])
def get_random_cafe():
    all_cafes=db.session.execute(db.select(Cafe)).scalars().all()
    random_cafe=random.choice(all_cafes)
    cafe_dict={
        'id': random_cafe.id,
        'name':random_cafe.name,
        'location': random_cafe.location,
        'map_url': random_cafe.map_url,
        'img_url': random_cafe.img_url,
        'seats':random_cafe.seats,
        'coffe_price':random_cafe.coffee_price,
        'amenities':{
            'has_toilet':random_cafe.has_toilet,
            'has_wifi':random_cafe.has_wifi,
            'has_sockets':random_cafe.has_sockets,
            'can_take_calls':random_cafe.can_take_calls
        }
    }
    return jsonify(cafe=cafe_dict)

@app.route('/all', methods=['GET'])
def cafes_list():
    all_cafes=db.session.execute(db.select(Cafe)).scalars().all()
    cafes_list=[]
    for cafe in all_cafes:
        cafe_dict={
        'id': cafe.id,
        'name':cafe.name,
        'location': cafe.location,
        'map_url': cafe.map_url,
        'img_url': cafe.img_url,
        'seats':cafe.seats,
        'coffe_price':cafe.coffee_price,
        'amenities':{
            'has_toilet':cafe.has_toilet,
            'has_wifi':cafe.has_wifi,
            'has_sockets':cafe.has_sockets,
            'can_take_calls':cafe.can_take_calls
            }
        }
        cafes_list.append(cafe_dict)
    return jsonify(cafe=cafes_list)

@app.route('/search', methods=['GET'])
def search_movie():
    loc=request.args.get('loc')
    compare_cafes = db.session.execute(db.select(Cafe).where(Cafe.location == loc)).scalars().all()
    cafes_list=[]
    if not compare_cafes:
        return jsonify(error="No cafes found at this location")
    else:
        for cafe in compare_cafes:
            cafe_dict={
            'id': cafe.id,
            'name':cafe.name,
            'location': cafe.location,
            'map_url': cafe.map_url,
            'img_url': cafe.img_url,
            'seats':cafe.seats,
            'coffe_price':cafe.coffee_price,
            'amenities':{
                'has_toilet':cafe.has_toilet,
                'has_wifi':cafe.has_wifi,
                'has_sockets':cafe.has_sockets,
                'can_take_calls':cafe.can_take_calls
                }
            }
            cafes_list.append(cafe_dict)
    return jsonify(cafes=cafes_list)

@app.route('/add', methods=['POST'])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get('name'),
        map_url=request.form.get('map_url'),
        img_url=request.form.get('img_url'),
        location=request.form.get('location'),
        seats=request.form.get('seats'),
        has_toilet=bool(request.form.get('has_toilet')),
        has_wifi=bool(request.form.get('has_wifi')),
        has_sockets=bool(request.form.get('has_sockets')),
        can_take_calls=bool(request.form.get('can_take_calls')),
        coffee_price=request.form.get('coffee_price')
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

@app.route('/update-price/<int:cafe_id>', methods=['PATCH'])
def change_price(cafe_id):
    price=request.args.get('new_price')
    try:
        cafe = db.session.get(Cafe, cafe_id)
        cafe.coffee_price = price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200
    except AttributeError:
        return jsonify(error="Cafe not found"), 404

@app.route('/report-closed/<int:cafe_id>', methods=['DELETE'])
def delete_cafe(cafe_id):
    api_key = request.args.get('api-key')
    if api_key != "TopSecretApiKey":
        return jsonify(error="Not authorized"), 403
    else:
        cafe = db.session.get(Cafe, cafe_id)
        db.session.delete(cafe)
        db.session.commit()
        return jsonify(response={"success": "Successfully deleted the cafe."}), 200

if __name__ == '__main__':
    app.run(debug=True)
