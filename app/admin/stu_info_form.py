# !/Git/eduProject/app/admin
# -*- ecoding: utf-8 -*-
# Author: Yujian
# Time: 2020/1/29 19:36

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField, FileField, IntegerField
from wtforms.validators import DataRequired, ValidationError, EqualTo, Length, NumberRange
from app.models import stu_info_table, stu_score_table
from flask_sqlalchemy import SQLAlchemy

'''
登录表单
1. 账号
2. 密码
3. 登录按钮
'''

# class login_form(FlaskForm):
#     account = StringField(
#         # 标签
#         label = "账号",
#         # 验证规则列表
#         validators = [
#             DataRequired("请输入账号哦！")
#         ],
#         description = "账号",
#         # 自定义html属性,且附加选项,会自动在前端判别
#         render_kw = {
#             "class": "form-control textClear",
#             "placeholder": "请输入账号哦!",
#             # 表示输入框不能为空，并有提示信息
#             "required": 'required'
#         }
#     )
#     pwd = PasswordField(
#         # 标签
#         label = "密码",
#         # 验证器
#         validators = [
#             DataRequired("请输入密码哦！")
#         ],
#         description = "密码",
#         render_kw = {
#             "class": "form-control textClear",
#             "placeholder": "请输入密码哦!",
#             # 表示输入框不能为空
#             "required": 'required'
#         }
#     )
#     submit = SubmitField(
#         label= "登录",
#         render_kw = {
#             "class": "btn btn-primary"
#         }
#     )
#
#     # 自定义字段验证规则：validate_字段名
#     def validate_name(self, field):
#         name = field.data
#         user1 = stu_info_table.query.filter_by(stu_name = name).count()
#         if user1 <= 0:
#             raise ValidationError("姓名不存在！")
#         else:
#             user2 = stu_info_table.query.filter_by(stu_name = name).first()
#             pwd = self.pwd.data
#             if not user2.check_pwd(pwd):
#                 raise ValidationError("密码不正确")
#

'''
信息录入表单 分为基础信息和成绩信息两个表单
1. 基础信息：姓名、学校、初创年级
2. 成绩信息：考试成绩、考试所属年级、考试类型、单元名
3. 保存按钮
'''

class stu_basic_info_add(FlaskForm):
    photo = FileField(
        label = '头像',
        description = '封面',
        render_kw = {
            "class": "form-control-file"
        }
    )
    stu_name = StringField(
        # 标签
        label = 'stu_name',
        # 验证器
        validators = [
            DataRequired("姓名不能为空哦！"),
            Length(1, 20, message = "必须是1-20个字哦！")
        ],
        description = "姓名",
        render_kw = {
            "class": "form-control",
            "id": "stu_name",
            "placeholder": "请输入姓名哦!"
        }
    )
    stu_school = StringField(
        # 标签
        label = 'stu_school',
        # 验证器
        description = "学校",
        render_kw = {
            "class": "form-control",
            'id': "stu_school",
            "placeholder": "请输入学校哦!"
        }
    )
    create_class = SelectField(
        # 标签
        label = 'create_class',
        # 验证器
        validators = [
            DataRequired("年级不能为空哦！"),
        ],
        description = "年级",
        render_kw = {
            "class": "form-control",
            'id': "create_class",
            "placeholder": "请输入年级哦!"
        },
        choices = [
            (1, '一年级'),
            (2, '二年级'),
            (3, '三年级'),
            (4, '四年级'),
            (5, '五年级'),
            (6, '六年级'),
            (7, '初一'),
            (8, '初二'),
            (9, '初三'),
            (10, '高一'),
            (11, '高二'),
            (12, '高三'),
                  ],
        default = 1,
        coerce = int
    )
    basic_submit = SubmitField(
        # 标签
        label = '保存个人信息',
        render_kw = {
            "class": "btn btn-primary",
            "id": "basic_submit"
        }
    )

class stu_score_info_add(FlaskForm):
    score_offline = IntegerField(
        # 标签
        label = 'score_offline',
        # 验证器
        validators = [
            DataRequired("成绩不能为空哦！"),
            NumberRange(0, 150, message="必须是0-150分哦！")
        ],
        description = "成绩",
        render_kw = {
            "class": "form-control",
            "id": "score_offline",
            "placeholder": "请输入成绩哦!"
        }
    )
    # 考试类型下拉框
    score_exsort = SelectField(
        # 标签
        label = 'score_exsort',
        # 验证器
        validators = [
            DataRequired("考试类型不能不选哦！")
        ],
        description = "考试类型",
        render_kw = {
            "class": "form-control",
            "id": "score_exsort",
            "placeholder": "请输入考试类型哦!",
            "onchange": "showinput(this);"
        },
        choices = [
            (1, '月考'),
            (2, '期中考试'),
            (3, '期末考试'),
            (4, '联考'),
            (5, '单元考试')
                   ],
        default = 1,
        coerce = int
    )
    score_exclass = SelectField(
        # 标签
        label='score_exclass',
        # 验证器
        validators=[
            DataRequired("本次考试所属年级不能为空哦！"),
        ],
        description="考试所属年级",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入考试所属年级哦!"
        },
        choices=[
            (1, '一年级'),
            (2, '二年级'),
            (3, '三年级'),
            (4, '四年级'),
            (5, '五年级'),
            (6, '六年级'),
            (7, '初一'),
            (8, '初二'),
            (9, '初三'),
            (10, '高一'),
            (11, '高二'),
            (12, '高三'),
        ],
        default=1,
        coerce=int
    )
    exam_info = StringField(
        # 标签
        label = 'exam_info',
        # 验证器
        validators = [
            Length(0, 30, message="单元名称长度应为0-30个字哦！")
        ],
        description = "单元名称",
        render_kw = {
            "class": "form-control",
            "id": "exam_info",
            "placeholder": "请输入单元名称哦!"
        }
    )
    score_submit = SubmitField(
        # 标签
        label='保存成绩信息',
        render_kw={
            "class": "btn btn-primary",
            "id": "score_submit"
        }
    )


# '''
# 信息修改表单
# 1.修改基本信息
# 2.修改成绩信息
# '''
# def stu_basic_info_edit(FlaskForm):
#
#
#
# def stu_score_info_edit(FlaskForm):
