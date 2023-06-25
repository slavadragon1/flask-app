import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or \
         'afdaksdjfkasdflansdlfjnasldfknslavaslavaslvalsldfaj2534:::###f'
    SQLALCHEMY_DATABASE_URI = 'postgresql://slavaaivan:5U471VNT2SS&QnMJ@pg3.sweb.ru:5432/slavaaivan'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


dbname='slavaaivan'
host='pg3.sweb.ru'
port='5432'
user='slavaaivan'
password='5U471VNT2SS&QnMJ'