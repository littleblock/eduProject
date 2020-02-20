# -*- coding:utf-8 -*-
# @Author: qixuanye
# @Time: 2020/1/21 19:55
import os
import uuid

import pymysql
from werkzeug.utils import redirect, secure_filename
from functools import wraps

from app import db, app
from app.admin.stu_info_form import stu_basic_info_add, stu_score_info_add
from app.admin import admin
from app.models import stu_info_table, stu_score_table
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
#         return redirect(url_for("admin.stu_info_view.stu_info_display"))
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
## 上传文件总目录
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.dirname(__file__)), "uploads")

# 学生头像目录
STU_PROFILE_FOLDER = os.path.join(UPLOAD_FOLDER, "stu_profile")
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
Basic_photo = r'C:\Users\一条余健\Pictures\芙芙\口吐芬芳.jpg'
basedir = os.path.abspath(os.path.dirname(__file__))


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# 定义可以上传的头像文件类型
#    跳转页面失败
@admin.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            file.save(os.path.join(UPLOAD_FOLDER, file.filename))
            return '<p>success</p>'
        else:
            return '<p> 你上传了不允许的文件类型 </p>'
    return render_template("/admin/Teacher/upload.html")


'''
录入功能
'''

#录入姓名、学校、初始年级
@admin.route("/stu_info_function/add_basic_info", methods = ['GET', 'POST'])
# @user_login_req
def basic_info_add():
    basic_form = stu_basic_info_add()
    if basic_form.validate_on_submit():
        data =basic_form.data
        # 获取学生姓名，学校，初始年级
        stu_name = data["stu_name"]
        stu_school = data["stu_school"]
        create_class = data["create_class"]

        # 上传图片
        # 获取文件名称（无法获取中文文件名）
        file_name = secure_filename(basic_form.photo.data.filename)
        stu_profile_name = change_name(file_name)
        save_photo(stu_profile_name, basic_form)

        # 保存stu_info_table数据
        # 暂时没有学校id，写死
        stu_info_list = stu_info_table(
            stu_name = stu_name,
            stu_school = stu_school,
            create_class = create_class,
            stu_class = create_class,
            stu_profile = stu_profile_name,
            creator = "待定",
            create_time = datetime.now(),
            # school_id = 1,
            last_modify_user = stu_name,
            last_modify_time = datetime.now(),
            is_del = 0
        )
        db.session.add(stu_info_list)
        db.session.commit()
        flash("保存成功！", "ok")
        redirect(url_for('admin.stu_info_display'))
    return render_template("/admin/stu_info/stu_add_basic_info.html", title = "蜻蜓教育💯学生个人信息", basic_form = basic_form)


# 修改文件名称
def change_name(name):
    info = os.path.splitext(name)
    # 文件名：时间格式字符串+唯一字符串+后缀名
    name = datetime.now().strftime('%Y%m%d%H%M%S') + str(uuid.uuid4().hex) + info[-1]
    return name

# 保存文件
def save_photo(photo, form):
    # 判断是否存在目录
    if not os.path.exists(STU_PROFILE_FOLDER):
        os.makedirs(STU_PROFILE_FOLDER)
    # 保存文件
    form.photo.data.save(STU_PROFILE_FOLDER + "/" + photo)



# 录入考试成绩，考试所属年级，考试类型，考试单元名称
@admin.route("/stu_info_function/add_score_info", methods = ['GET', 'POST'])
# uer_login_req
def score_info_add():
    score_form = stu_score_info_add()
    print(score_form.validate_on_submit())
    if score_form.validate_on_submit():
        data = score_form.data
        # 获取考试成绩，考试所属年级，考试类型，考试单元名称
        score_offline = data["score_offline"]
        score_exclass = data["score_exclass"]
        score_exsort = data["score_exsort"]
        exam_info = data["exam_info"]
        # 保存stu_score_table数据
        score_info_list = stu_score_table(
            score_offline=score_offline,
            score_exclass=score_exclass,
            score_exsort=score_exsort,
            exam_info=exam_info,
            creator=stu_info_table.stu_name,
            create_time=datetime.now(),
            last_modify_user=stu_info_table.stu_name,
            last_modify_time=datetime.now(),
            is_del=0
        )
        db.session.add(score_info_list)
        db.session.commit()
        flash("保存成功！", "ok")
        redirect(url_for('admin.stu_info_display'))
    return render_template("/admin/stu_info/stu_add_score_info.html", title = "蜻蜓教育💯学生个人信息", score_form = score_form)


'''
编辑功能
'''
'''
# 连接数据库
# 建立连接、拿到游标对象
connect = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='yujian',
    port=3306,
    db='edu',
    # charset='utf8'
)
# 拿到游标对象
cursor = connect.cursor()
'''

# 编辑/更新基本信息
@admin.route("/stu_info_function/edit_basic_info", methods = ["GET", "POST"])
# @user_login_req
def basic_info_edit(id):
    edit_form = stu_basic_info_add()

    if edit_form.validate_on_submit():
        # 获取学生姓名，学生学校，学生初始年级
        stu_name = request.form.get("stu_name")
        stu_school = request.form.get("stu_school")
        create_class = request.form.get("create_class")
        last_modify_user = stu_name,
        last_modify_time = datetime.now()

        # 获取特定id对应的数据库数据
        filter_by_id = stu_info_table.query.filter_by(id=id, is_del=0).first()
        # 修改数据库中特定数据
        filter_by_id.stu_name = stu_name
        filter_by_id.stu_school = stu_school
        filter_by_id.create_class = create_class
        filter_by_id.last_modify_user = last_modify_user
        filter_by_id.last_modify_time = last_modify_time

        try:
            # 提交到数据库执行
            db.session.commit()
        except:
            flash("修改失败，请重试！", "ok")
            redirect(url_for(admin.stu_info_view.score_info_edit))
        flash("保存成功！", "ok")
        redirect(url_for('admin.stu_info_view.stu_info_display'))
    return render_template("/admin/stu_info/stu_add_basic_info.html", title="蜻蜓教育💯学生个人信息", basic_form=edit_form)


# 编辑/更新成绩信息
@admin.route("/stu_info_function/edit_score_info", methods = ["GET", "POST"])
# @user_login_req
def score_info_edit(id):
    edit_form = stu_score_info_add()
    if edit_form.validate_on_submit():
        # 获取考试成绩，考试所属年级，考试类型，考试单元名称
        score_offline = request.form.get("score_offline")
        score_exclass = request.form.get("score_exclass")
        score_exsort = request.form.get("score_exsort")
        exam_info = request.form.get("exam_info")
        last_modify_user=stu_info_table.stu_name,
        last_modify_time=datetime.now(),

        # 获取特定id对应的数据库数据
        filter_by_id = stu_score_table.query.filter_by(id=id, is_del=0).first()
        # 修改数据库中特定数据
        filter_by_id.score_offline = score_offline
        filter_by_id.score_exclass = score_exclass
        filter_by_id.score_exsort = score_exsort
        filter_by_id.exam_info = exam_info
        filter_by_id.last_modify_user = last_modify_user
        filter_by_id.last_modify_time = last_modify_time

        try:
            # 提交到数据库执行
            db.session.commit()
        except:
            flash("修改失败，请重试！", "ok")
            redirect(url_for(admin.stu_info_view.score_info_edit))
        flash("保存成功！", "ok")
        redirect(url_for('admin.stu_info_view.stu_info_display'))
    return render_template("/admin/stu_info/stu_add_score_info.html", title = "蜻蜓教育💯学生个人信息", score_form = edit_form)



'''
展示功能
'''
# 年级更新策略暂时没有，先写死
updatetodo = 0

# 显示基本信息
@admin.route("/stu_info_function/basic_display", methods = ['GET', 'POST'])
# uer_login_req
def stu_info_display(id):

    # 获取特定id对应的数据库数据
    filter_by_id = stu_info_table.query.filter_by(id=id, is_del=0).first()
    # 建立字典用于存储取出的信息
    stu_basic_info_dict = {}

    try:
        # 获取数据库特定数据
        stu_name = filter_by_id.stu_name
        stu_school = filter_by_id.stu_school
        create_class = filter_by_id.create_class
        # 数据存入字典
        stu_basic_info_dict['stu_name'] = stu_name
        stu_basic_info_dict['stu_school'] = stu_school
        stu_basic_info_dict['create_class'] = create_class
        stu_basic_info_add['stu_class'] = create_class + updatetodo

    except:
        flash("没有相关信息，请录入！", "ok")
        redirect(url_for('admin.basic_info_add'))

    return render_template("/admin/stu_info/stu_info_display.html", title = "蜻蜓教育💯学生个人信息", dict1 = stu_basic_info_dict)


# 显示成绩信息
@admin.route("/stu_info_function/score_display/<int:page>", methods = ['GET', 'POST'])
# uer_login_req
def stu_score_display(page = None):
    # 默认page初始值为None，永远先跳转到第一页
    if page is None:
        page = 1
    # 每页一个考试信息，留出空间放考试的知识图谱、不足等相关信息
    page_datas = stu_score_table.query.filter_by(is_del=0).paginate(page=page, per_page=1)
    # 获取特定id对应的数据库数据
    filter_by_id = stu_score_table.query.filter_by(id=id, is_del=0).first()
    # 建立字典用于存储取出的信息
    stu_score_info_dict = {}

    try:
        # 获取数据库特定数据
        score_offline = filter_by_id.score_offline
        score_exclass = filter_by_id.score_exclass
        score_exsort = filter_by_id.score_exsort
        exam_info = filter_by_id.exam_info
        # 数据存入字典
        stu_score_info_dict['score_offline'] = score_offline
        stu_score_info_dict['score_exclass'] = score_exclass
        stu_score_info_dict['score_exsort'] = score_exsort
        stu_score_info_dict['exam_info'] = exam_info

    except:
        flash("没有相关信息，请录入！", "ok")
        redirect(url_for('admin.score_info_add'))

    return render_template("/admin/stu_info/stu_score_display.html", title = "蜻蜓教育💯学生个人信息", dict2 = stu_score_info_dict, page_data =page_datas)


# 学生列表
@admin.route("/stu_info_function/info_list/<int:page>", methods = ["GET", "POST"])
def stu_info_list(page = None):
    # 默认page初始值为None，永远先跳转到第一页
    if page is None:
        page = 1
    page_datas = stu_info_table.query.filter_by(is_del=0).paginate(page = page, per_page = 5)

    return render_template("/admin/stu_info/stu_info_list.html", title = "学生信息列表", page_data = page_datas)

# @admin.route("/test1")
# def test1():
#     return "hello, world! stu_info_view"

