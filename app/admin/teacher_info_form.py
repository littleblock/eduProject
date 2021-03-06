# -*- coding:utf-8 -*-
# @Author: wanghaochen
# @Time: 2020/2/6 19:00

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField, FileField, IntegerField
from wtforms import SelectMultipleField, core, widgets
from wtforms.validators import DataRequired, ValidationError, EqualTo,NumberRange
from wtforms.fields import SelectMultipleField
from wtforms.widgets import ListWidget, CheckboxInput
'''
老师信息注册：
基本信息：姓名 年龄 学校 专业
擅长信息：擅长年纪 擅长模块
自我介绍
'''


class teacher_info_form(FlaskForm):
    # 头像
    photo = FileField(
        label = '头像',
        description = '封面',
        render_kw = {
            "class": "form-control-file"
        }
    )
    # 姓名
    name = StringField(
        # 标签
        label = 'name',
        # 验证器
        validators=[
            DataRequired("姓名不能为空"),
        ],
        description="姓名",
        render_kw={
        "class": "form-control",
        'id': "name",
        "placeholder": "请输入姓名"
        }
    )
    # 微信号
    chat = StringField(
        # 标签
        label='chat',
        # 验证器
        validators=[
            DataRequired("微信号不能为空"),
        ],
        description="微信号",
        render_kw={
            "class": "form-control",
            'id': "chat",
            "placeholder": "请输入微信号"
        }
    )
    # 专业
    major = StringField(
        # 标签
        label='major',
        # 验证器
        validators=[
            DataRequired("专业不能为空"),
        ],
        description="专业",
        render_kw={
            "class": "form-control",
            'id': "major",
            "placeholder": "请输入所学专业"
        }
    )
    # 学校
    school = StringField(
        # 标签
        label='school',
        # 验证器
        validators=[
            DataRequired("毕业学校不能为空"),
        ],
        description="毕业学校",
        render_kw={
            "class": "form-control",
            'id': "school",
            "placeholder": "请输入毕业学校"
        }
    )
    # 年级
    grade = core.SelectField(
        # 标签
        label='adv_grade',
        # 验证器
        validators=[
            DataRequired("至少选择一项")
        ],
        description="年级",
        render_kw={
            "id": "adv_grade",
            "placeholder": "请至少选择一项"
        },
        choices=[
            (1, '大一'),
            (2, '大二'),
            (3, '大三'),
            (4, '大四'),
            (5, '研一'),
            (6, '研二'),
            (7, '研三'),
        ],
        default=7,
        coerce=int
    )
    #擅长教学年纪
    adv_grade = core.SelectMultipleField(
        # 标签
        label='adv_grade',
        # 验证器
        validators=[
            DataRequired("至少选择一项")
        ],
        description="年级",
        render_kw={
            "id": "adv_grade",
            "placeholder": "请至少选择一项"
        },
        choices=[
            (1, '一年级'),
            (2, '二年级'),
            (3, '三年级'),
            (4, '四年级'),
            (5, '五年级'),
            (6, '六年纪'),
            (7, '初一'),
            (8, '初二'),
            (9, '初三'),
            (10, '高一'),
            (11, '高二'),
            (12, '高三'),
        ],
        widget=widgets.ListWidget(prefix_label=False),
        option_widget=widgets.CheckboxInput(),
        default=12,
        coerce=int
    )
    # 擅长教学模块
    adv_model = core.SelectMultipleField(
        # 标签
        label='adv_model',
        # 验证器
        validators=[
            DataRequired("至少选择一项")
        ],
        description="擅长教学的模块",
        render_kw={
            "id": "adv_model",
            "placeholder": "请至少选择一项"
        },
        choices=[
            (1, '实数与不等式'),
            (2, '函数'),
            (3, '简单平面几何'),
            (4, '圆'),
            (5, '相似与全等较难问题'),
            (6, '统计概率'),
            (7, '全部擅长'),
        ],
        widget=widgets.ListWidget(prefix_label=False),
        option_widget=widgets.CheckboxInput(),
        default=7,
        coerce=int
    )
    #有无家教经验
    experience = SelectField(
        #标签
        label='experience',
        #验证器
        validators=[
            DataRequired("至少选择一项")
        ],
        description="有无家教经验",
        render_kw = {
                     "id": "experience",
                     "placeholder": "请至少选择一项"
        },
        choices=[
            (1,'有家教经验'),
            (2,'无家教经验'),
        ],

        default=1,
        coerce=int
    )
    # 自我介绍
    introduction = TextAreaField(
        # 标签
        label='introduction',
        description="自我介绍",
        render_kw={
            "class": "form-control",
            'id': "introduction",
            "placeholder": "自我介绍内容"
        }
    )
    #教师分类
    # 有无家教经验
    classify = SelectField(
        # 标签
        label='classify',
        # 验证器
        validators=[
            DataRequired("至少选择一项")
        ],
        description="教师分类",
        render_kw={
            "id": "experience",
            "placeholder": "请至少选择一项"
            
        },
        choices=[
            (0, '未决定'),
            (1, '计划制定教师'),
            (2, '辅导教师'),
            (3, '错题诊断教师'),
        ],
        default=3,
        coerce=int
    )
    #提交注册信息
    info_submit = SubmitField(
        # 标签
        label='提交注册信息',
        render_kw={
            "class": "btn btn-primary div2",
            # "id": "info_submit"
        }
    )

    '''
    老师评价：
    评价分数
    评价语
    '''

class teacher_evaluate_form(FlaskForm):
    # 评价分数
    score = IntegerField(
        # 标签
        label='score',
        # 验证器
        validators=[
            DataRequired("姓名不能为空"),
            NumberRange(0, 100, "分数在0-100之间"),
        ],
        description="评价分数",
        render_kw={
            "class": "form-control",
            'id': "score",
            "placeholder": "分数在0-100之间"
        }
    )
    # 评语
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
        label='提交',
        render_kw={
            "class": "btn btn-primary div2",
            # "id": "submit"
        }
    )