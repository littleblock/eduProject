# -*- coding:utf-8 -*-
# @Author: wanghaochen
# @Time: 2020/2/6 18:44
import os
import string
import random
import uuid
import xlrd
import sqlalchemy
from . import admin
from app.models import wrong_ques_table, wrong_ques_review, teacher_info,teacher_evaluation,classroom,stu_info_table,db
from datetime import datetime
from werkzeug.utils import secure_filename
from flask import render_template, session, url_for, request, flash, redirect
from .teacher_info_form import teacher_info_form,teacher_evaluate_form
import base64

# 上传文件总目录
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.dirname(__file__)), "uploads")
# 教师头像目录
TEACHER_PHOTO_FOLDER = os.path.join(UPLOAD_FOLDER, "teacher_photo")
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
Basic_photo=r'C:\Users\whc\PycharmProjects\eduProject\app\upload\touxiang.jpg'
grade = ["大一","大二","大三","大四","研一","研二","研三"]
adv_grade = ["一年级", "二年级", "三年级", "四年级", "五年级" , "六年级", "初一", "初二" , "初三" , "高一" , "高二" , "高三"]
model = ["实数与不等式","函数","简单平面几何","圆","相似与全等较难问题","统计概率","全部擅长"]
basedir = os.path.abspath(os.path.dirname(__file__))


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@admin.route("/teacher_evaluate", methods=["Get", "POST"])
def teacher_evaluate():
    form = teacher_evaluate_form()
    if form.validate_on_submit():
        data = form.data
        score = request.args.get("score")
        evaluation = teacher_evaluation(id=1000,  # 写死
                                        teacher_id=1001,  # 写死先
                                        score=score,
                                        evaluation=data["words"],
                                        creator="whc",  # 写死先
                                        create_time=datetime.now(),
                                        last_modify_user="whc",  # 写死先
                                        last_modify_time=datetime.now(),
                                        is_del=0,
                                        )
        db.session.add(evaluation)
        db.session.commit()
        flash("提交成功", "ok")
    return render_template("/admin/Teacher/teacher_evaluation.html", form=form)


@admin.route("/teacher_info_input", methods=["Get", "POST"])
def teacher_info_input():
    form = teacher_info_form()
    if form.validate_on_submit():
        data = form.data
        model_list = form.adv_model.data
        models = ""
        grades = ""
        for v in model_list:
            models += model[v - 1] + ";"
        grade_list = form.adv_grade.data
        for v in grade_list:
            grades += adv_grade[v - 1] + ";"

        # 上传图片
        file_name = secure_filename(form.photo.data.filename)
        photo_name = change_name(file_name)
        save_photo(photo_name, form)

        if data["experience"] == 1:
            ex = "有"
        else:
            ex = "没有"
        info = teacher_info(
                            name=data["name"],
                            head_photo=photo_name,
                            chat=data["chat"],
                            school=data["school"],
                            major=data["major"],
                            introduce=data["introduction"],
                            adv_model=models,
                            adv_grade=grades,
                            grade = grade[data["grade"] - 1],
                            experience=ex,
                            creator="whc",  # 写死先
                            create_time=datetime.now(),
                            last_modify_user="whc",  # 写死先
                            last_modify_time=datetime.now(),
                            is_del=0,
                            )
        db.session.add(info)
        db.session.commit()
        flash("提交成功", "ok")
    return render_template("/admin/Teacher/teacher_info.html", form=form)


# 修改文件名称
def change_name(name):
    info = os.path.splitext(name)
    # 文件名：时间格式字符串+唯一字符串+后缀名
    name = datetime.now().strftime('%Y%m%d%H%M%S') + str(uuid.uuid4().hex) + info[-1]
    return name

# 保存文件
def save_photo(photo, form):
    # 判断是否存在目录
    if not os.path.exists(TEACHER_PHOTO_FOLDER):
        os.makedirs(TEACHER_PHOTO_FOLDER)
    # 保存文件
    form.photo.data.save(TEACHER_PHOTO_FOLDER + "/" + photo)

# 学段列表
@admin.route("/info_list/<int:page>", methods = ["GET", "POST"])
def info_list(page = None):
    # 默认page初始值为None，永远先跳转到第一页
    if page is None:
        page = 1
    page_datas = teacher_info.query.filter_by(is_del=0).paginate(page = page, per_page = 5)

    return render_template("/admin/Teacher/info_list.html", title = "老师信息列表", page_data = page_datas)


@admin.route("teacher_type_edit/<id>", methods = ["GET", "POST"])
def teacher_type_edit(id):
    form = teacher_info_form()
    clas = teacher_info.query.filter(teacher_info.teacher_id == id).first()
    if request.method == 'POST':
        data = form.data
        classify = data["classify"]
        clas.classify = classify
        db.session.commit()
        return redirect(url_for("admin.info_list" , page = 1))
    return render_template("/admin/Teacher/teacher_classify_edit.html", title = "修改老师类别", form = form)


#班级管理
@admin.route("/class_stu_list/<int:page>", methods = ["GET", "POST"])
def class_stu_list(page = None):
    # 默认page初始值为None，永远先跳转到第一页
    if page is None:
        page = 1
    page_datas = stu_info_table.query.filter_by(is_del=0).paginate(page = page, per_page = 5)

    return render_template("/admin/Teacher/class_manage.html", title = "班级管理", page_data = page_datas)

@admin.route("/class_edit/<id>", methods = ["GET", "POST"])
def class_edit(id):
    teach = teacher_info.query.filter_by(is_del=0)
    return render_template("/admin/Teacher/class_edit.html", title="选择教课老师",teacher = teach, stu_id = id)

@admin.route("/class_sure", methods = ["GET", "POST"])
def class_sure():
    id_stu = request.args.get("student_id")
    id_teacher = request.args.get("teacher_id")
    clas = classroom(
        student_id=id_stu,
        teacher_id=id_teacher,
        creator="whc",  # 写死先
        create_time=datetime.now(),
        last_modify_user="whc",  # 写死先
        last_modify_time=datetime.now(),
        is_del=0,
    )
    db.session.add(clas)
    db.session.commit()
    page = 1
    page_datas = stu_info_table.query.filter_by(is_del=0).paginate(page = page, per_page = 5)
    return render_template("/admin/Teacher/class_manage.html", title = "班级管理", page_data = page_datas)

@admin.route("/read_teachinfo_excel/", methods = ["GET", "POST"])
def read_teachinfo_excel():
    wb = xlrd.open_workbook(filename=r"C:\Users\whc\Desktop\线上家教个人信息.xls")  # 打开文件
    sheet = wb.sheet_by_name("Sheet1")
    sheet_name = sheet.col_values(0)
    sheet_grade = sheet.col_values(4)
    sheet_major = sheet.col_values(3)
    sheet_school = sheet.col_values(2)
    sheet_chat = sheet.col_values(1)
    sheet_adv_grade = sheet.col_values(5)
    sheet_adv_model = sheet.col_values(6)
    sheet_experience = sheet.col_values(7)
    sheet_introduce = sheet.col_values(8)

    for col in range(1,sheet.nrows):
        info = teacher_info(
            name=sheet_name[col],
            head_photo=r'C:\Users\whc\PycharmProjects\eduProject\app\upload\touxiang.jpg',
            chat=sheet_chat[col],
            school=sheet_school[col],
            major=sheet_major[col],
            introduce=sheet_introduce[col],
            adv_model=sheet_adv_model[col],
            adv_grade=sheet_adv_grade[col],
            classify = 0,
            grade=sheet_grade[col],
            experience=sheet_experience[col],
            creator="whc",  # 写死先
            create_time=datetime.now(),
            last_modify_user="whc",  # 写死先
            last_modify_time=datetime.now(),
            is_del=0,
        )
        db.session.add(info)
        db.session.commit()
    return "ye"

@admin.route("/demo", methods = ["GET", "POST"])
def demo():
 return render_template("/admin/demo.html", title = "班级管理")

@admin.route("/class_list/<int:page>", methods = ["GET", "POST"])
def class_list(page = None):
    if page is None:
        page = 1
    page_datas = classroom.query.filter_by(is_del=0).paginate(page = page, per_page = 5)

    return render_template("/admin/Teacher/class_manage.html", title = "班级", page_data = page_datas)

@admin.route("/teacher_class_list/<id>", methods = ["GET", "POST"])
def teacher_class_list(id):
    students_id = classroom.query.filter_by(teacher_id=id)
    q_1 = []

    for a in students_id:
        q_2 = stu_info_table.query.filter_by(id=a.student_id)
        for b in q_2:
            a = b
            q_1.append(b)
            break
    return render_template("/admin/Teacher/teacher_class.html", title = "老师班级", student_list = q_1)

@admin.route("/delete_student/<id>", methods = ["GET", "POST"])
def delete_student(id):
    class1 = classroom.query.filter_by(student_id=id).first()
    db.session.delete(class1)
    db.session.commit()
    page = 1
    page_datas = teacher_info.query.filter_by(is_del=0).paginate(page = page, per_page = 5)
    return render_template("/admin/Teacher/info_list.html", title="班级", page_data=page_datas)
