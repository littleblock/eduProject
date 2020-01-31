# -*- coding:utf-8 -*-
# @Author: quxuanye
# @Time: 2020/1/31 0:12
# 权限控制相关

from . import admin
from flask import redirect, url_for

# 登陆
@admin.route("/login", methods = ["GET", "POST"])
def login():
    return "这是登陆界面"

# 注册
@admin.route("/register", methods = ["GET", "POST"])
def register():
    return "这是注册界面"

# 退出登陆
@admin.route("/logout", methods = ["GET"])
def logout():
    return redirect(url_for("admin.login"))