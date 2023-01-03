import random
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Produkter(db.Model):
    __tablename__= "Produkt"
    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(50), unique=False, nullable=False)
    Pris = db.Column(db.Float, unique=False, nullable=False)
    Colour= db.Column(db.String(20), unique=False, nullable=False)


def seedData(db):
    namn = ["Ullgarn","Syntetgarn", "Bomullsgarn", "Lingarn", "Blandgarn", "Mohairgarn", "Cashmeregarn"]
    color = ["Beige", "Grå", "Svart", "Brun", "Amber", "Ljusgrå", "Congac", "Smaragdgrön", "Senapsgul", "Rost", "Vit", "Natur" ]
    antal =  Produkter.query.count()
    while antal < 500:
        produkt = Produkter()
        produkt.Name = random.choice(namn)
        produkt.Pris = round(random.uniform(10.50,99.50),2)
        produkt.Colour = random.choice(color)
        db.session.add(produkt)
        db.session.commit()


