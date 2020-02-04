# -*- coding:utf-8 -*-
# @Author: quxuanye
# @Time: 2020/1/31 18:38
# 知识图谱

from . import admin
from flask import render_template, redirect, url_for, flash
from .ques_form import subject_form, period_form
from app.models import subject, db, period
from datetime import datetime


# 学科录入
@admin.route("/subject/add", methods = ["GET", "POST"])
def subject_add():
    form = subject_form()
    if form.validate_on_submit():
        data = form.data
        subject_data = subject(
            subject_name = data["chinese_name"],
            subject_english_name = data["english_name"],
            creator = 'qixuanye',
            create_time = datetime.now(),
            last_modify_user = 'qixuanye',
            last_modify_time = datetime.now(),
            is_del = 0
        )
        db.session.add(subject_data)
        db.session.commit()
        flash("录入成功", "ok")
    return render_template("admin/subject_add.html", title = "添加学科", form = form)


# 学科列表
@admin.route("/subject/list/<int:page>", methods = ["GET", "POST"])
def subject_list(page = None):
    # 默认page初始值为None，永远先跳转到第一页
    if page is None:
        page = 1
    page_datas = subject.query.filter_by(is_del=0).paginate(page = page, per_page = 5)
    return render_template("admin/subject_list.html", title = "学科列表", page_data = page_datas)


# 学科删除
@admin.route("/subject/del/<id>", methods = ["GET", "POST"])
def subject_del(id):
    return "删除学科"

# 添加学段
@admin.route("/period/add", methods = ["GET", "POST"])
def period_add():
    form = period_form()
    if form.validate_on_submit():
        data = form.data
        period_data = period(
            period_name=data["name"],
            creator='qixuanye',
            create_time=datetime.now(),
            last_modify_user='qixuanye',
            last_modify_time=datetime.now(),
            is_del=0
        )
        db.session.add(period_data)
        db.session.commit()
        flash("录入成功", "ok")
    return render_template("admin/period_add.html", title="添加学段", form=form)


# 学段列表
@admin.route("/period/list/<int:page>", methods = ["GET", "POST"])
def period_list(page = None):
    # 默认page初始值为None，永远先跳转到第一页
    if page is None:
        page = 1
    page_datas = period.query.filter_by(is_del=0).paginate(page = page, per_page = 5)
    return render_template("admin/period_list.html", title = "学段列表", page_data = page_datas)


# 添加基础知识点
@admin.route("knowledge/add", methods = ["GET", "POST"])
def knowledge_add():
    return "添加基础知识点"


# 知识点列表
@admin.route("/knowledge/list/<id>", methods = ["GET", "POST"])
def knowledge_list(id):
    return "知识点列表"