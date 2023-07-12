from flask import Flask, request, g
from config import *
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_babel import Babel, get_locale
from flask_socketio import SocketIO

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
login.login_message = 'please login😔😔😔'
socketio = SocketIO(app)



from src import routes, models, errors
# Time
moment = Moment(app)
# CSS
bootstrap = Bootstrap(app)


# Lang localization
# def get_locale():
#     # if a user is logged in, use the locale from the user settings
#     user = getattr(g, 'user', None)
#     if user is not None:
#         return user.locale
#     # otherwise try to guess the language from the user accept
#     # header the browser transmits.  We support de/fr/en in this
#     # example.  The best match wins.
#     return request.accept_languages.best_match(Config.LANGUAGES)
# babel = Babel(app, locale_selector=get_locale)

