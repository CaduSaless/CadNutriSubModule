from flask import Flask, render_template
from routes.auth import auth_bp
from routes.cadastro import cadastro_bp
from routes.bd_cad import bd_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'projetofacom'

app.register_blueprint(auth_bp)
app.register_blueprint(cadastro_bp)
app.register_blueprint(bd_bp, url_prefix='/bd')


@app.route('/')
def homepage():
    return render_template('index.html')


if '__main__' == __name__:
    app.run(debug=True, port=80)
