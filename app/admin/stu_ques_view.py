# -*- coding:utf-8 -*-
# @Author: quxuanye
# @Time: 2020/1/22 10:52

from . import admin
from app.models import wrong_ques_table, wrong_ques_review, db
from datetime import datetime
from flask import render_template
from .stu_form import stu_ques_add_form


# 测试,访问地址为http://127.0.0.1:5000/admin/test2

@admin.route("/ques_input",methods = ["Get", "POST"])
def ques_input():
    form = stu_ques_add_form()
    if form.validate_on_submit():
        data = form.data
        # 获取用户名
        #user = session["user"]
        # 判断该错题是否在在错题表中
        if (ques_table_exit(1001)):
            # 错题存在 插入记录
            review_in(1001, "1")
        else:
            # 错题不存在 创建错题及其记录
            create_ques_table(123, 1001, data["ques_info"], "答案", "whc")
            create_ques_review(1001, "1")
    return render_template("/admin/stu_ques_add.html", form = form)


# 向已有的错题记录中插入记录
def review_in(question_id, right):
    reviews = wrong_ques_review.query.filter_by(ques_id=question_id).count()
    review = wrong_ques_review.query.filter_by(ques_id=question_id).first()
    if reviews <= 0:
        create_ques_review(question_id, right)
    else:
        review.whether_right += "," + right
        review.do_time += "," + datetime.now()


# 创建错题
def create_ques_table(student, question_id, question_info, question_answer, creator1):
    question = wrong_ques_table(student_id = student,
                          ques_id=question_id,
                          ques_info=question_info,
                          ques_answer=question_answer,
                          creator="whc",
                          create_time = datetime.now(),
                          last_modify_user="whc",
                          last_modify_time="2020.2.1",
                          is_del=0
                          )
    db.session.add(question)
    db.session.commit()


# 将创建第一次做题记录
def create_ques_review(question_id, whether_right1):
    review = wrong_ques_review(ques_id=question_id,
                         whether_right=whether_right1,
                         do_time=datetime.now(),
                         creator = "whc",
                         create_time = datetime.now(),
                         last_modify_user = "whc",
                         last_modify_time = "2020.2.1",
                         is_del = 0
    )
    db.session.add(review)
    db.session.commit()


# 判断错题是否在错题表中 1为有 0为无
def ques_table_exit(question_id):
    ids = wrong_ques_table.query.filter_by(ques_id=question_id).count()
    if ids <= 0:
        return 0
    return 1


# 若不同view中出现相同函数名，应加endpoint
@admin.route("/test2")
def test2():
    return "hello, world! stu_ques_view"
