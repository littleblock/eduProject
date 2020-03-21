import xlrd
from . import home
from app.models import plantable,plan_relation,wrong_ques_table, wrong_ques_review, teacher_info,teacher_evaluation,classroom,stu_info_table,db
from flask import render_template, session, url_for, request, flash, redirect
from datetime import datetime
import sqlalchemy
import os
import string
import uuid
import random

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.dirname(__file__)), "uploads")
EXCEL_FILE = os.path.join(UPLOAD_FOLDER,"plan_excel")


#学生列表
@home.route("/stu_list", methods = ["GET", "POST"])
def stu_list():
    id = 1
    students_id = classroom.query.filter_by(teacher_id=id)
    q_1 = []

    for a in students_id:
        q_2 = stu_info_table.query.filter_by(id=a.student_id)
        for b in q_2:
            a = b
            q_1.append(b)
            break
    return render_template("/PlanTeacher/stu_list.html", title = "学生列表", student_list = q_1, teacher = id)

# 修改文件名称
def change_name(name):
    info = os.path.splitext(name)
    # 文件名：时间格式字符串+唯一字符串+后缀名
    name = datetime.now().strftime('%Y%m%d%H%M%S') + str(uuid.uuid4().hex) + info[-1]
    return name


#excel计划导入
@home.route("/excel_plan", methods = ["GET", "POST"])
def excel_plan():
    teacher = request.args.get('teacher_id')
    student = request.args.get('student_id')
    id = {'stu_id' : student,'teach_id' : teacher}
    if request.method == 'POST':
        f = request.files.get('file')
        stuid = request.form.get('stu')
        teachid = request.form.get('teach')
        file_name = change_name(f.filename)
        if not os.path.exists(EXCEL_FILE):
            os.makedirs(EXCEL_FILE)
        # 保存文件
        f.save(EXCEL_FILE + "\\" + file_name)
        wb = xlrd.open_workbook(filename=EXCEL_FILE + "\\" + file_name)  # 打开文件
        sheet_names = wb.sheet_names()
        for sheet_name in sheet_names:
            sheet = wb.sheet_by_name(sheet_name)
            p = sheet_name.split('.')
            year = p[0]
            month = p[1]
            day = p[2]
            d = datetime(int(year),int(month),int(day))
            finish_time = sheet.col_values(1)
            t = ""
            for time in finish_time[1:]:
                t += str(time) + " "
            content = ""
            contents = sheet.col_values(2)
            for con in contents[1:]:
                content += str(con) + " "
            plan = plantable(
                student_id = stuid,
                teacher_id = teachid,
                daytime = d,
                plan_time = t,
                plan_content = content,
                performance = "",
                reason = "",
                creator="whc",  # 写死先
                create_time=datetime.now(),
                last_modify_user="whc",  # 写死先
                last_modify_time=datetime.now(),
                is_del= 0,
            )
            db.session.add(plan)
            db.session.flush()
            pl_id = plan.id
            db.session.commit()
            pl_relation = plan_relation(
                student_id=stuid,
                plan_id=pl_id,
                creator="whc",  # 写死先
                create_time=datetime.now(),
                last_modify_user="whc",  # 写死先
                last_modify_time=datetime.now(),
                is_del=0,
            )
            db.session.add(pl_relation)
            db.session.commit()
    return render_template("/PlanTeacher/excel_save.html", title="计划表导入",ids = id)


#今日计划表
@home.route("/show_plan/<id>", methods = ["GET", "POST"])
def show_plan(id):
    plans = plan_relation.query.filter_by(student_id=int(id))
    answer = {}
    for plan in plans:
        p = plantable.query.filter_by(id=plan.plan_id).first()
        if p.daytime.month == datetime.now().month and p.daytime.day == datetime.now().day:
            answer = p
            break
    times = answer.plan_time.split(' ')[:-1]
    contents = answer.plan_content.split(' ')[:-1]
    numb = range(1,len(times) - 1)
    info = []
    for i in numb:
        info.append({'time':times[i],
                   'content':contents[i],
                   'number' : i})
    return render_template("/PlanTeacher/show_plan.html",title="计划表展示",info = info,id = answer.id)

#今日计划完成度
@home.route("/plan_complish/", methods = ["GET", "POST"])
def plan_complish():
    if request.method == 'POST':
        wetherdo = request.form.get('whetherDo')
        reason = request.form.get('reason')
        planid = request.form.get('plan_id')
        plan = plantable.query.filter_by(id = planid).first()
        plan.performance = wetherdo
        plan.reason = reason
        db.session.commit()
