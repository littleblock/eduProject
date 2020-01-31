# -*- coding:utf-8 -*-
# @Author: quxuanye
# @Time: 2020/1/30 23:50
# 基础题库

from . import admin


# 学科录入
@admin.route("/subject/add", methods = ["GET", "POST"])
def subject_add():
    return "录入学科"

# 学科删除
@admin.route("/subject/del/<id>", methods = ["GET", "POST"])
def subject_del(id):
    return "删除学科"