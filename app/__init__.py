# -*- coding:utf-8 -*-
# @Author: quxuanye
# @Time: 2020/1/21 19:53

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 开启debug模式
app.debug = True
# 数据库配置
# qixuanye的本地数据库
#app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@127.0.0.1:3306/edu"
# whc的本地数据库
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:newpassword@127.0.0.1:3306/edu"
# yj的本地数据库
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:yujian@127.0.0.1:3306/edu"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)

# 创建蓝图对象
from app.admin import admin as admin_blueprint

# 注册蓝图
app.register_blueprint(admin_blueprint, url_prefix = "/admin")

