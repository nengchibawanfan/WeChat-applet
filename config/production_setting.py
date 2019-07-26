# -*- coding: utf-8 -*-
DEBUG = True
SQLALCHEMY_ECHO = True
SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@localhost/food_db?charset=utf8mb4'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ENCODING = "utf8mb4"

APP = {
    'domain': 'http://0.0.0.0:8999'
}

RELEASE_VERSION = "20180729001"
