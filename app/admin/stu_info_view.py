# -*- coding:utf-8 -*-
# @Author: qixuanye
# @Time: 2020/1/21 19:55
from werkzeug.utils import redirect
from functools import wraps

from app import db
from app.admin.stu_info_form import stu_info_add
from app.admin import admin
from app.models import info_table, score_table
from datetime import datetime
from flask import render_template, session, url_for, request, flash

# 测试,访问地址为http://127.0.0.1:5000/admin/test1


# # 登陆装饰器
# def user_login_req(f):
#     @wraps(f)
#     def login_req(*args, **kwargs):
#         # 判断该用户是否已经存在
#         if "user" not in session:
#             return redirect(url_for("admin.login", next = request.url))
#         return f(*args, **kwargs)
#
#     return login_req
#
#
# # 学生登录
# @admin.route("/login", methods = ['GET', 'POST'])
# def stu_login():
#     form = login_form()
#     if form.validate_on_submit():
#         # 获取form表单所有数据
#         data = form.data
#         # 获取当前登陆的用户名
#         session["user"] = data["name"]
#         # 登录成功，跳转到学生个人信息首页
#         flash("登录成功！", "ok")
#         return redirect("")
#     else:
#         flash("登录失败，请重新登录", "err")
#         return redirect(url_for("admin.login"))
#     return render_template("admin/stu_login.html", title="学生信息", form=form)
#
#
# # # 注册
# # @admin.route("/register", methods = ['GET', 'POST'])
# # def register():
# #     return render_template("admin/register.html")
#
#
# # 退出，直接跳转到登录页面
# @admin.route("/logout", methods = ['GET'])
# @user_login_req
# def logout():
#     session.pop("user", None)
#     return redirect(url_for("admin.login"))


#录入姓名、学校、初始年级，考试成绩，考试所属年级，考试类型，考试单元名称
@admin.route("/stu_info_function/add_info", methods = ['GET', 'POST'])
# @user_login_req
def info_add():
    stu_form = stu_info_add()
    if stu_form.validate_on_submit():
        # 获取学生姓名，学校，初始年级，考试成绩，考试所属年级，考试类型，考试单元名称
        stu_name = request.form.get("stu_name")
        stu_school = request.form.get("stu_school")
        creat_class = request.form.get("creat_class")
        score_offline = request.form.get("score_offline")
        score_exclass = request.form.get("score_exclass")
        score_exsort = request.form.get("score_exsort")
        exam_info = request.form.get("exam_info")
        # 保存info_table数据
        stu_info_list = info_table(
            stu_name = stu_name,
            stu_school = stu_school,
            creat_class = creat_class,
            stu_class = creat_class,
            creator = "待定",
            creat_time = datetime.now(),
            last_modify_user = stu_name,
            last_modify_time = datetime.now(),
            is_del = 0
        )
        # 保存score_table数据
        score_info_list = score_table(
            score_offline = score_offline,
            score_exclass = score_exclass,
            score_exsort =score_exsort,
            exam_info = exam_info,
            creator= stu_name,
            creat_time = datetime.now(),
            last_modify_user = stu_name,
            last_modify_time = datetime.now(),
            is_del=0
        )
        db.session.add(stu_info_list,score_info_list)
        db.session.commit()
        flash("保存成功！", "ok")
    return render_template("/admin/stu_info.html", title = "学生信息", form = stu_form)


# # 编辑信息
# @admin.route("/stu_info_function/edit_info", methods = ["GET", "POST"])
# # @user_login_req
# def info_edit(id):
#     form = stu_info_edit()




# 删除信息




@admin.route("/test1")
def test1():
    return "hello, world! stu_info_view"

