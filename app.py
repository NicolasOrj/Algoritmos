from flask import Flask
from config import db, DATABASE_URI
from routes.user_routes import user_bp
from routes.product_routes import product_bp
from routes.store_routes import store_bp

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos
db.init_app(app)

# Registrar los Blueprints de las rutas
app.register_blueprint(user_bp)
app.register_blueprint(product_bp)

#Crear las tablas si no existen
with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
