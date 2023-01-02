# Övning - egen sajt

# Skapa ett nytt projekt

# du ska ha en databas med Products
# varje produkt ska ha id, namn, pris, color
# Skapa en SEEDNINGs-funktion (ska se till att det finns minst 500 st produkter i databasen) som körs vid uppstart efter migrering
# Slumpa fram unika namn, priser, färger på nåt fiffigt sätt?


# skriv ett admin console UI som - listar alla, samt man kan skapa ny
# copy and paste från Stefans genomgång = bygg en enkel webb ui


# (ps nästa vecka = vi bygger vidare på denna -> komplett webapplikation )






from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, upgrade

from model import db, seedData, Produkter

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:stefan@localhost/players0101'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:my-secret-pw@localhost/Products' 
db.app = app
db.init_app(app)
migrate = Migrate(app,db)

@app.route("/")
def startpage():
	    return "<h1>test</h1>"
        # <html><head></head><</html>

@app.route("/kontakt")
def contactpage():
    s = "<html><head><title>Get lost</title></head><body>"
    for c in Produkter.query.all():
        s = s + c.Name + "<br />"
    s = s + "</body></html>"
    return s

if __name__  == "__main__":
    with app.app_context():
        upgrade()
    
        seedData(db)
        #app.run()
