# -*- coding:utf-8 -*-
# @Author: wanghaochen
# @Time: 2020/2/6 18:44
import os
import string
import random
import uuid

from . import admin
from app.models import wrong_ques_table, wrong_ques_review, teacher_info, teacher_evaluation, db
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
        evaluation = teacher_evaluation(id=1000,  # 写死
                                        teacher_id=1001,  # 写死先
                                        score=data["score"],
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
            grades += grade[v - 1] + ";"

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
