# -*- coding:utf-8 -*-
# @Author: quxuanye
# @Time: 2020/1/21 19:53

# 配置好app中的__init.py__ 后，在这里导入db
# from app import db

from datetime import datetime

class stu_ques_view_first(db.Model):
    # 定义表名
    __tablename__ = 'wrong_ques_table'
    # 定义字段
    # db.Column 表示是一个字段
    id = db.Column(db.Integer, primary_key = True)
    student_id = db.Column(db.Integer, unique = True)
    ques_id = db.Column(db.Integer, unique = True)
    ques_info = db.Column(db.String(100), nullable = False)
    ques_answer = db.Column(db.String(100), nullable = False)
    creator = db.Column(db.char(50), nullable = False)
    create_time = db.Column(db.DateTime, nullable = False)
    last_modify_user = db.Column(db.Integer, unique = True)
    last_modify_time = db.Column(db.DateTime, nullable = False)
    is_del = db.Column(db.Integer, nullable = True)

class stu_ques_view_second(db.Model):
    # 定义表名
    __tablename__ = 'wrong_ques_review'
    # 定义字段
    # db.Column 表示是一个字段
    ques_id = db.Column(db.Integer, primary_key = True)
    whether_right = db.Column(db.Boolean)
    do_time = db.Column(db.DateTime, unique = True)
    creator = db.Column(db.char(50), nullable = False)
    create_time = db.Column(db.DateTime, nullable = False)
    last_modify_user = db.Column(db.Integer, unique = True)
    last_modify_time = db.Column(db.DateTime, nullable = False)
    is_del = db.Column(db.Integer, nullable = True)

