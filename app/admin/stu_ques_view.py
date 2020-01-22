# -*- coding:utf-8 -*-
# @Author: quxuanye
# @Time: 2020/1/22 10:52

from . import admin

# 测试,访问地址为http://127.0.0.1:5000/admin/test2
# 若不同view中出现相同函数名，应加endpoint
@admin.route("/test2")
def test2():
    return "hello, world! stu_ques_view"