# -*- coding:utf-8 -*-
# @Author: quxuanye
# @Time: 2020/1/21 19:55

from . import admin

# 测试,访问地址为http://127.0.0.1:5000/admin/test1






@admin.route("/test1")
def test1():
    return "hello, world! stu_info_view"