from flask import Flask, render_template
from database import inicializar_banco
from controllers.produto_controller import produto_bp

app = Flask(__name__)

inicializar_banco()
app.register_blueprint(produto_bp)

@app.route("/", methods=["GET"])
def inicio():
    return render_template("produtos.html")

if __name__ == '__main__':
    app.run(debug=True)
