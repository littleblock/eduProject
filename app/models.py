# -*- coding:utf-8 -*-
# @Author: quxuanye
# @Time: 2020/1/21 19:53

# 配置好app中的__init.py__ 后，在这里导入db
from app import db
from datetime import datetime

'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 开启debug模式
app.debug = True
# 数据库配置
# qixuanye的本地数据库
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@127.0.0.1:3306/edu"
# whc的本地数据库
# yj的本地数据库

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)
'''

# 错题表模型
class ques_table(db.Model):
    # 定义表名
    __tablename__ = 'wrong_ques_table'
    # 主键
    id = db.Column(db.BigInteger, primary_key = True)
    # 学生编号
    student_id = db.Column(db.Integer, unique = True)
    # 问题编号
    ques_id = db.Column(db.Integer, unique = True)
    # 题干信息
    ques_info = db.Column(db.String(100), nullable = False)
    # 问题答案
    ques_answer = db.Column(db.String(100), nullable = False)
    # 创建人
    creator = db.Column(db.String(128), nullable=False)
    # 创建时间
    create_time = db.Column(db.DateTime, default=datetime.now)
    # 最后修改人
    last_modify_user = db.Column(db.String(128), nullable=False)
    # 最后修改时间
    last_modify_time = db.Column(db.DateTime, default=datetime.now)
    # 该条记录是否可用，默认为0，可用
    is_del = db.Column(db.SmallInteger, default=0, nullable=False)

    def __repr__(self):
        return "<ques_table %r>" % self.name

# 做题记录模型
class ques_review(db.Model):
    # 定义表名
    __tablename__ = 'wrong_ques_review'
    # 主键
    id = db.Column(db.BigInteger, primary_key = True)
    # 问题编号
    ques_id = db.Column(db.Integer, unique = True)
    # 是否做对 1为做对 0为做错
    whether_right = db.Column(db.String(1))
    # 做题时间
    do_time = db.Column(db.DateTime, unique = True)
    # 创建人
    creator = db.Column(db.String(128), nullable=False)
    # 创建时间
    create_time = db.Column(db.DateTime, default=datetime.now)
    # 最后修改人
    last_modify_user = db.Column(db.String(128), nullable=False)
    # 最后修改时间
    last_modify_time = db.Column(db.DateTime, default=datetime.now)
    # 该条记录是否可用，默认为0，可用
    is_del = db.Column(db.SmallInteger, default=0, nullable=False)

    def __repr__(self):
        return "<ques_review %r>" % self.name

if __name__ == "__main__":
    db.drop_all()

