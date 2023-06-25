from flask import Flask
from config import *
import psycopg2

app = Flask(__name__)
app.config.from_object(Config)
conn = psycopg2.connect(dbname=dbname, host=host, port=port, user=user, password=password)
cur = conn.cursor()


from src import routes