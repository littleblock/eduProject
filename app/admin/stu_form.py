# -*- coding:utf-8 -*-
# @Author: quxuanye
# @Time: 2020/1/21 19:53
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField, FileField, IntegerField
from wtforms.validators import DataRequired, ValidationError, EqualTo

'''
错题题目提交
'''
class stu_ques_add_form(FlaskForm):
    ques_info = StringField(
        validators = [
            DataRequired("题干不能为空")
        ],
        render_kw = {
            "class": "form-control",
            "placeholder": "题干内容请符合相应规范！"
        }
    )
    submit = SubmitField(
        "提交题干内容",
        render_kw={
            "class": "btn btn-primary"
        }
    )


'''
学科信息录入
1. 学科名（中文)
2. 学科名（英文）
'''
class subject_form(FlaskForm):
    chinese_name = StringField(
        label = "学科中文名",
        validators = [
            DataRequired("不能为空！")
        ],
        description = "学科中文名",
        render_kw = {
            "class": "form-control",
            "placeholder": "请输入学科中文名"
        }
    )
    english_name = StringField(
        label="学科英文名",
        validators=[
            DataRequired("不能为空！")
        ],
        description="学科英文名",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入学科英文名"
        }
    )
    submit = SubmitField(
        "提交",
        render_kw = {
            "class": "btn btn-primary"
        }
    )