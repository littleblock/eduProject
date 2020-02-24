# -*- coding:utf-8 -*-
# @Author: quxuanye
# @Time: 2020/1/31 18:38
# 知识图谱

from . import admin
from flask import render_template, redirect, url_for, flash
from .knowledge_map_form import subject_form, period_form, knowledge_level1_form, knowledge_level2_form
from app.models import subject, db, period, knowledge_basic, knowledge_level
from datetime import datetime


# 学科录入
@admin.route("/subject/add", methods=["GET", "POST"])
def subject_add():
    form = subject_form()
    if form.validate_on_submit():
        data = form.data
        subject_data = subject(
            subject_name=data["chinese_name"],
            subject_english_name=data["english_name"],
            creator='qixuanye',
            create_time=datetime.now(),
            last_modify_user='qixuanye',
            last_modify_time=datetime.now(),
            is_del=0
        )
        db.session.add(subject_data)
        db.session.commit()
        flash("录入成功", "ok")
    return render_template("admin/knowledge_map/subject_add.html", title="添加学科", form=form)


# 学科列表
@admin.route("/subject/list/<int:page>", methods=["GET", "POST"])
def subject_list(page=None):
    # 默认page初始值为None，永远先跳转到第一页
    if page is None:
        page = 1
    page_datas = subject.query.filter_by(is_del=0).paginate(page=page, per_page=5)
    return render_template("admin/knowledge_map/subject_list.html", title="学科列表", page_data=page_datas)


# 添加学段
@admin.route("/period/add", methods=["GET", "POST"])
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
    return render_template("admin/knowledge_map/period_add.html", title="添加学段", form=form)


# 学段列表
@admin.route("/period/list/<int:page>", methods=["GET", "POST"])
def period_list(page=None):
    # 默认page初始值为None，永远先跳转到第一页
    if page is None:
        page = 1
    page_datas = period.query.filter_by(is_del=0).paginate(page=page, per_page=5)
    return render_template("admin/knowledge_map/period_list.html", title="学段列表", page_data=page_datas)


# 添加一级知识点
@admin.route("knowledge_level1/add", methods=["GET", "POST"])
def knowledge_level1_add():
    form = knowledge_level1_form()
    if form.validate_on_submit():
        data = form.data

        # 判断知识点是小、初、高中，获取period_id
        if data["period_name"] == 1:
            period_data = period.query.filter_by(period_name='小学', is_del=0).first()
        elif data["period_name"] == 2:
            period_data = period.query.filter_by(period_name='初中', is_del=0).first()
        else:
            period_data = period.query.filter_by(period_name='高中', is_del=0).first()

        subject_data = subject.query.filter_by(subject_name='数学', is_del=0).first()
        # 存基础知识点表
        knowledge_level1_basic = knowledge_basic(
            knowledge_name=data["knowledge_level1_name"],
            subject_id=subject_data.subject_id,
            period_id=period_data.period_id,
            creator='qixuanye',
            create_time=datetime.now(),
            last_modify_user='qixuanye',
            last_modify_time=datetime.now(),
            is_del=0
        )
        db.session.add(knowledge_level1_basic)
        # 获取刚刚插入的id
        db.session.flush()
        knowledge_id = knowledge_level1_basic.knowledge_id
        # 存知识点等级表
        knowledge_level1_level = knowledge_level(
            knowledge_id=knowledge_id,
            subject_id=subject_data.subject_id,
            period_id=period_data.period_id,
            level_1_id=knowledge_id,
            level_1_name=data["knowledge_level1_name"],
            level_2_id=0,
            level_2_name='无',
            level_3_id=0,
            level_3_name='无',
            creator='qixuanye',
            create_time=datetime.now(),
            last_modify_user='qixuanye',
            last_modify_time=datetime.now(),
            is_del=0
        )
        db.session.add(knowledge_level1_level)
        db.session.commit()
        flash("录入成功", "ok")
    return render_template("admin/knowledge_map/knowledge_level1_add.html", title="添加一级知识点", form=form)


# 一级知识点列表
@admin.route("/knowledge_level1/list/<int:page>", methods=["GET"])
def knowledge_level1_list(page=None):
    if page is None:
        page = 1
    page_datas = knowledge_level.query.filter(knowledge_level.level_1_id != 0).filter(
        knowledge_level.level_2_id == 0).filter(knowledge_level.level_3_id == 0).paginate(page=page, per_page=2)
    return render_template("admin/knowledge_map/knowledge_level1_list.html", title="一级知识点列表", page_data=page_datas)


# 删除一级知识点
@admin.route("/knowledge_level1/del/<id>", methods=["GET", "POST"])
def knowledge_level1_del(id):
    return "删除知识点"


# 添加二级知识点
@admin.route("knowledge_level2/add", methods=["GET", "POST"])
def knowledge_level2_add():
    form = knowledge_level2_form()
    return render_template("admin/knowledge_map/knowledge_level2_add.html", title="添加一级知识点", form=form)


# 二级知识点列表
@admin.route("/knowledge_level2/list/<id>", methods=["GET"])
def knowledge_level2_list(id):
    return "知识点列表"


# 删除一级知识点
@admin.route("/knowledge_level2/del/<id>", methods=["GET", "POST"])
def knowledge_level2_del(id):
    return "删除知识点"


# 添加三级知识点
@admin.route("knowledge_level3/add", methods=["GET", "POST"])
def knowledge_level3_add():
    return "添加基础知识点"


# 三级知识点列表
@admin.route("/knowledge_level3/list/<id>", methods=["GET"])
def knowledge_level3_list(id):
    return "知识点列表"
