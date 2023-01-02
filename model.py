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
    namn = ["Ull Garn","Syntet Garn", "Bomulls Garn", "Lin Garn", "Bland Garn"]
    color = ["Beige", "Grå", "Svart", "Brun", "Amber"]
    antal =  Produkter.query.count()
    while antal < 500:
        produkt = Produkter()
        produkt.Name = random.choice(namn)
        produkt.Pris = round(random.uniform(10.50,99.50),2)
        produkt.Colour = random.choice(color)
        db.session.add(produkt)
        db.session.commit()






# import random
# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# class Customer(db.Model):
#     __tablename__= "Customer"
#     Id = db.Column(db.Integer, primary_key=True)
#     Name = db.Column(db.String(50), unique=False, nullable=False)
#     City = db.Column(db.String(40), unique=False, nullable=False)
#     TelephoneCountryCode = db.Column(db.Integer, unique=False, nullable=False)
#     Telephone = db.Column(db.String(20), unique=False, nullable=False)


# def seedData(db):
#     cites = ["Stockholm","Västerås", "Södertälje"]
#     countrycodes = [46,47,44]
#     antal =  Customer.query.count()
#     while antal < 500:
#         customer = Customer()
#         customer.Name = "Customer" + str(antal)
#         customer.TelephoneCountryCode = random.choice(countrycodes)
#         customer.Telephone = random.randint(10000000,999999999)
#         customer.City = random.choice(cites)
#         db.session.add(customer)
#         db.session.commit()
#         antal = antal + 1