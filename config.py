import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or \
         'afdaksdjfkasdflansdlfjnasldfknslavaslavaslvalsldfaj2534:::###f'
    SQLALCHEMY_DATABASE_URI = 'postgresql://slavaaivan:5U471VNT2SS&QnMJ@pg3.sweb.ru:5432/slavaaivan'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 3
    LANGUAGES = ['en', 'en-US', 'ru', 'es']
    


