# -*- coding:utf-8 -*-
# @Author: quxuanye
# @Time: 2020/2/2 13:33

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField, FileField, IntegerField
from wtforms.validators import DataRequired, ValidationError, EqualTo


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


'''
学段信息录入
1. 学段名
'''
class period_form(FlaskForm):
    name = StringField(
        label = "学段名",
        validators = [
            DataRequired("不能为空！")
        ],
        description = "学段名",
        render_kw = {
            "class": "form-control",
            "placeholder": "请输入学段名"
        }
    )
    submit = SubmitField(
        "提交",
        render_kw = {
            "class": "btn btn-primary"
        }
    )