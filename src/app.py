from flask import Flask, render_template
from routes.to_do import to_do
from dotenv import load_dotenv
import os

# Carga de Dotenv
load_dotenv()

# Instancia de Flask
app = Flask(__name__)

app.config[MONGO_URI] = os.getenv("MONGO_URI")


# Ruta principal de la aplicacion
@app.route("/")
def index():
    return render_template("index.html")


# Registro de Bluprints - (Routes)
app.register_blueprint(to_do, url_prefix="/to-do")

# Condicional Principal de Aplicacion + DEBUG
if __name__ == "__main__":
    app.run(debug=True)
