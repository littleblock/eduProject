# -*- coding:utf-8 -*-
# @Author: quxuanye
# @Time: 2020/1/22 10:52

from . import admin
from app.models import ques_table, ques_review
from datetime import datetime
from flask import render_template



# 测试,访问地址为http://127.0.0.1:5000/admin/test2

@admin.route("/ques_input")
def ques_input():
    # 判断该错题是否在在错题表中
    '''
    if (ques_table_exit("timubianhao")):
        # 错题存在 插入记录
        review_in("timubianhao", "1")
    else:
    # 错题不存在 创建错题及其记录
        create_ques_table("xuesheng1", "timubianhao", "题干", "答案", "whc")
        create_ques_review("timubianhao", "1", )
    '''
    return render_template("/admin/stu_ques_add.html")


# 向已有的错题记录中插入记录
def review_in(question_id, right):
    question = ques_table.query.get(question_id)
    question.whether_right += "," + right
    question.do_time += "," + datetime.now()


# 创建错题
def create_ques_table(student, question_id, question_info, question_answer, creator1):
    student_role = ques_table(student_id=student)
    question_id_role = ques_table(ques_id=question_id)
    question_info_role = ques_table(ques_info=question_info)
    question_answer_role = ques_table(ques_answer=question_answer)
    create_people_role = ques_table(creator=creator1)
    create_time_role = ques_table(create_time_=datetime.now())
    last_modicy_user_role = ques_table(last_modicy_user="whc")
    last_modify_time_role = ques_table(last_modify_time="whc")
    is_del_role = ques_table(is_del=0)


# 将创建第一次做题记录
def create_ques_review(question_id, whether_right1):
    question_id_role = ques_review(ques_id=question_id)
    whether_right_role = ques_review(whether_right=whether_right1)
    do_time_role = ques_review(do_time=datetime.now())


# 判断错题是否在错题表中 1为有 0为无
def ques_table_exit(question_id):
    for table in ques_table.ques_id:
        if table == question_id:
            return 1
    return 0


# 若不同view中出现相同函数名，应加endpoint
@admin.route("/test2")
def test2():
    return "hello, world! stu_ques_view"
