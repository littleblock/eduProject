# -*- coding:utf-8 -*-
# @Author: quxuanye
# @Time: 2020/1/21 19:53

# 配置好app中的__init__.py 后，在这里导入db
from app import db

from datetime import datetime

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

# 学生基础信息表模型
class info_table(db.Model):
    # 定义表名
    __tablename__ = 'stu_basic_info'
    # 主键
    id = db.Column(db.BigInteger, primary_key = True, unique = True, autoincrement=True)
    # 学生姓名
    stu_name = db.Column(db.String(128), nullable = False)
    # 学生学校
    stu_school = db.Column(db.String(100), nullable = False)
    # 创建账户时录入的年级
    creat_class = db.Column(db.Integer, nullable = False)
    # 学生当前年级
    stu_class = db.Column(db.Integer, nullable = False)
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

# 学生成绩信息表模型
class score_table(db.Model):
    # 定义表名
    __tablename__ = 'stu_socre_info'
    # 主键
    id = db.Column(db.BigInteger, primary_key = True, unique = True, autoincrement=True)
    # 学生编号，与上表的id对应，作为上表外键
    stu_id = db.Column(db.Integer, db.ForeignKey('stu_basic_info.id'), nullable=False)
    # 学生录入的考试成绩
    score_offline = db.Column(db.Integer, nullable=False)
    # 考试所属年级
    score_exclass = db.Column(db.Integer, nullable=False)
    # 考试类型（月考、期中、期末、模拟考）
    score_exsort = db.Column(db.String(20))
    # 如果考试不属于上述考试类型就为单元名，反之为空
    exam_info = db.Column(db.String(30), nullable = True)
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