# -*- coding:utf-8 -*-
# @Author: wanghaochen
# @Time: 2020/2/6 18:44
import os
import string
import random

from . import admin
from app.models import wrong_ques_table, wrong_ques_review, teacher_info, teacher_evaluation, db
from datetime import datetime
from flask import render_template, session, url_for, request, flash, redirect
from .teacher_info_form import teacher_info_form
from .teacher_evaluate_form import teacher_evaluate_form
import base64


UPLOAD_FOLDER = r'C:\Users\whc\PycharmProjects\eduProject\app\upload'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
Basic_photo=r'C:\Users\whc\PycharmProjects\eduProject\app\upload\touxiang.jpg'
grade = ["一年级","二年级","三年级","四年级","五年级","六年级","初一","初二","初三","高一","高二","高三"]
model = ["代数运算","方程组求解","函数","平面几何","立体几何","解析几何","向量运算","排列组合","概率与统计"]
basedir = os.path.abspath(os.path.dirname(__file__))

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


'''   跳转页面失败
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
@admin.route("/teacher_evaluate", methods=["Get", "POST"])
def teacher_evaluate():
    form = teacher_evaluate_form()
    if form.validate_on_submit():
        data = form.data
        evaluation = teacher_evaluation(id = 1000, #写死
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
''' 上传图片失败
def editorData(name):
    #生成随机字符串，防止图片名字重复
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 16))
    #获取图片文件 name = upload
    img = name.read()
    #定义一个图片存放的位置 存放在static下面
    path = basedir+"\\static\\upload\\"
    #图片名称 给图片重命名 为了图片名称的唯一性
    imgName = ran_str+img.filename
    #图片path和名称组成图片的保存路径
    file_path = path+imgName
    #保存图片
    img.save(file_path)
    #这个是图片的访问路径，需返回前端（可有可无）
    url = '/static/upload/'+imgName
    return url
'''

@admin.route("/teacher_info_input", methods=["Get", "POST"])
def teacher_info_input():
    form = teacher_info_form()
    if form.validate_on_submit():
        if form.info_submit:
            data = form.data
            model_list = form.adv_model.data
            models = ""
            grades = ""
            for v in model_list:
                models += model[v-1] + ";"
            grade_list = form.adv_grade.data
            for v in grade_list:
                grades += grade[v-1] + ";"
            if data["photo"] == '':
                photo = Basic_photo
            else:
                photo = data["photo"]       # 此处加保存图片程序
            info = teacher_info(teacher_id=1001,  # 写死先
                                name=data["name"],
                                head_photo=photo,
                                age=data["age"],
                                school=data["school"],
                                major=data["major"],
                                introduce=data["introduction"],
                                adv_model=models,
                                adv_grade=grades,
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


