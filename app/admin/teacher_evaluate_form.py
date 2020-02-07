# -*- coding:utf-8 -*-
# @Author: wanghaochen
# @Time: 2020/2/6 19:00

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField, FileField, IntegerField
from wtforms import SelectMultipleField, core, widgets
from wtforms.validators import DataRequired, ValidationError, EqualTo, NumberRange
from wtforms.fields import SelectMultipleField
from wtforms.widgets import ListWidget, CheckboxInput
'''
老师评价：
评价分数
评价语
'''


class teacher_evaluate_form(FlaskForm):
    #评价分数
    score = IntegerField(
        # 标签
        label = 'score',
        # 验证器
        validators=[
            DataRequired("姓名不能为空"),
            NumberRange(0,100,"分数在0-100之间"),
        ],
        description="评价分数",
        render_kw={
            "class": "form-control",
            'id': "score",
            "placeholder": "分数在0-100之间"
        }
    )
    #评语
    words = TextAreaField(
        # 标签
        label='words',
        description="本次课的评价",
        render_kw={
            "class": "form-control",
            'id': "words",
            "placeholder": "对老师的评价（选填）"
        }
    )
    # 提交注册信息
    submit = SubmitField(
        # 标签
        label='提交注册信息',
        render_kw={
            "class": "btn btn-primary div2",
            # "id": "submit"
        }
    )