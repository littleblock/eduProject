# -*- coding:utf-8 -*-
# @Author: quxuanye
# @Time: 2020/1/21 19:53

from app import app

#已有review，向其中记录
def review_in(question_id, right):
    question = ques_table.query.get(question_id)
    question.whether_right += ","+ right
    question.do_time += "," + Datetime.now()

#创建错题表
def create_ques_table(student, question_id, question_info, question_answer, creator1, ):
    student_role = ques_table(student_id = student)
    question_id_role = ques_table(ques_id = question_id)
    question_info_role = ques_table(ques_info = question_info)
    question_answer_role = ques_table(ques_answer = question_answer)
    create_people_role = ques_table(creator = creator1)
    create_time_role = ques_table(creator = Datetime.now())
    last_modicy_user_role =
    last_modify_time_role =
    is_del_role = ques_table(is_del = 0)

#创建错题做题记录表
def create_ques_review(question_id, whetherright1, time):
    question_id_role = ques_review(ques_id = question_id)
    whether_right_role = ques_review(whether_right = whether_right1)
    do_time_role = ques_review(do_time = time)
#判断错题表是否存在
def ques_table_exit(question_id):
    for table in ques_table.ques_id:
        if table == question_id:
            return 1
    else :
        return 0
if __name__ == "__main__":
        app.run()
