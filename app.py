from flask import Flask
from views import views


app = Flask(__name__)
#Lien avec les blueprints créés
app.register_blueprint(views, url_prefix="/views")


if __name__ == '__main__':
    app.run(debug=True, port=8000) #le port de base est 5000, peut être changé