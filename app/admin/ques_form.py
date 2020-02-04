# -*- coding:utf-8 -*-
# @Author: quxuanye
# @Time: 2020/2/2 13:33

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField, FileField, IntegerField
from wtforms.validators import DataRequired, ValidationError, EqualTo
from app.models import period


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

'''
一级知识点录入
1. 选择学段，默认初中
2. 录入知识点名
'''
class knowledge_level1_form(FlaskForm):
    period_name = SelectField(
        label = "学段分类",
        description = "学段分类",
        validators = [
            DataRequired("分类不能为空！")
        ],
        # 从学段表中取出学段信息
        choices = [],
        default = 2,
        coerce = int,
        render_kw = {
            "class": "form-control"
        }
    )
    knowledge_level1_name = StringField(
        label = "一级知识点名",
        validators = [
            DataRequired("不能为空！")
        ],
        description = "一级知识点名",
        render_kw = {
            "class": "form-control",
            "placeholder": "请输入知识点名称"
        }
    )
    submit = SubmitField(
        "提交",
        render_kw={
            "class": "btn btn-primary"
        }
    )

    # 每次实例化都会从数据库取一次，做到数据库和展示页面数据实时更新
    def __init__(self, *args, **kwargs):
        super(knowledge_level1_form, self).__init__(*args, **kwargs)
        self.period_name.choices = [(v.period_id, v.period_name) for v in period.query.filter_by(is_del=0)]