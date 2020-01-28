# -*- coding:utf-8 -*-
# @Author: quxuanye
# @Time: 2020/1/21 19:53

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 开启debug模式
app.debug = True
# 数据库配置
'''
app.config["SQLALCHEMY_DATABASE_URI"] = 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = 
db = SQLAlchemy(app)
'''

app.config["SQLALCHEMY_DATABASE_URI"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)

# 创建蓝图对象
from app.admin import admin as admin_blueprint

# 注册蓝图
app.register_blueprint(admin_blueprint, url_prefix = "/admin")

