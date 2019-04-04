from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_pyfile('app.cfg')
app.config['SECRET_KEY'] = 'spooky'
login = LoginManager(app)
login.login_view = 'login'
import views
