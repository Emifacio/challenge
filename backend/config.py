import os

class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://myuser:mypassword@db:5432/mydatabase'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'myjwtsecret'
    SECRET_KEY = 'mysecret'
