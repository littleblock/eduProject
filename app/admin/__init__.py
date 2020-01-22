# -*- coding:utf-8 -*-
# @Author: quxuanye
# @Time: 2020/1/21 19:53

# 定义蓝图
from flask import Blueprint

admin = Blueprint("admin", __name__)

import app.admin.stu_info_view
import app.admin.stu_ques_view