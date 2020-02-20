# -*- coding:utf-8 -*-
# @Author: quxuanye
# @Time: 2020/1/21 19:53

# 配置好app中的__init.py__ 后，在这里导入db
from app import db
from datetime import datetime

# 若要生成数据表，将上面的from app import db注释掉，将下面的注释和最后的if __name__ == '__main__'部分注释去掉
# 生成数据表后，记得再重新注释上


'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 开启debug模式
app.debug = True
# 数据库配置
# qixuanye的本地数据库
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@127.0.0.1:3306/edu"

# whc的本地数据库
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:newpassword@127.0.0.1:3306/edu"
# yj的本地数据库
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:yujian@127.0.0.1:3306/edu"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)
'''


# 班级表
class classroom(db.Model):
    __tablename__ = 'classroom'
    # id
    id = db.Column(db.Integer, primary_key=True)
    # 学生id
    student_id = db.Column(db.BigInteger, nullable=False)
    # 老师id
    teacher_id = db.Column(db.Integer, db.ForeignKey("teacher_info.teacher_id"))
    # 创建人
    creator = db.Column(db.String(128), nullable=False)
    # 创建时间
    create_time = db.Column(db.DateTime, default=datetime.now)
    # 最后修改人
    last_modify_user = db.Column(db.String(128), nullable=False)
    # 最后修改时间
    last_modify_time = db.Column(db.DateTime, default=datetime.now)
    # 该条记录是否可用，默认为0，可用
    is_del = db.Column(db.SmallInteger, default=0, nullable=False)

    def __repr__(self):
        return "<classroom %r>" % self.name

# 教师信息表
class teacher_info(db.Model):
    __tablename__ = 'teacher_info'
    # 教师id
    teacher_id = db.Column(db.Integer, primary_key=True)
    # 姓名
    name = db.Column(db.String(50), nullable=False)
    # 微信号
    chat = db.Column(db.String(100), nullable=False)
    # 头像照片
    head_photo = db.Column(db.String(200), nullable=False)
    # 教师分类 0--还未分类 1--计划制定教师 2--辅导教师 3--错题诊断教师
    classify = db.Column(db.Integer, default=0)
    # 毕业学校
    school = db.Column(db.String(50), nullable=False)
    # 专业
    major = db.Column(db.String(50), nullable=False)
    # 擅长模块
    adv_model = db.Column(db.String(200), nullable=False)
    # 擅长教学年纪
    adv_grade = db.Column(db.String(200), nullable=False)
    # 年纪
    grade = db.Column(db.String(200), nullable=False)
    # 有无家教经验
    experience = db.Column(db.String(10), nullable=False)
    # 自我介绍
    introduce = db.Column(db.String(200), nullable=True)
    # 创建人
    creator = db.Column(db.String(128), nullable=False)
    # 创建时间
    create_time = db.Column(db.DateTime, default=datetime.now)
    # 最后修改人
    last_modify_user = db.Column(db.String(128), nullable=False)
    # 最后修改时间
    last_modify_time = db.Column(db.DateTime, default=datetime.now)
    # 该条记录是否可用，默认为0，可用
    is_del = db.Column(db.SmallInteger, default=0, nullable=False)
    # 老师评价表外键连接
    teacher_evalu = db.relationship('teacher_evaluation', backref='teacher_info')
    # 班级表外键链接
    teacher_class = db.relationship('classroom', backref='teacher_info')

    def __repr__(self):
        return "<teacher_info %r>" % self.name


# 老师评价表
class teacher_evaluation(db.Model):
    __tablename__ = 'teacher_evaluation'
    # id
    id = db.Column(db.Integer, primary_key=True)
    # 教师id
    teacher_id = db.Column(db.Integer, db.ForeignKey("teacher_info.teacher_id"), nullable=False)
    # 评价分数
    score = db.Column(db.Integer, nullable=False)
    # 学生评价
    evaluation = db.Column(db.String(200), nullable=True)
    # 创建人
    creator = db.Column(db.String(128), nullable=False)
    # 创建时间
    create_time = db.Column(db.DateTime, default=datetime.now)
    # 最后修改人
    last_modify_user = db.Column(db.String(128), nullable=False)
    # 最后修改时间
    last_modify_time = db.Column(db.DateTime, default=datetime.now)
    # 该条记录是否可用，默认为0，可用
    is_del = db.Column(db.SmallInteger, default=0, nullable=False)

    def __repr__(self):
        return "<teacher_evaluation %r>" % self.name


# 错题表模型
class wrong_ques_table(db.Model):
    # 定义表名
    __tablename__ = 'wrong_ques_table'
    # 问题编号
    ques_id = db.Column(db.Integer, primary_key=True)
    # 编号
    id = db.Column(db.BigInteger, unique=True)
    # 学生编号
    student_id = db.Column(db.Integer, unique=True)
    # 题干信息
    ques_info = db.Column(db.String(100), nullable=False)
    # 问题答案
    ques_answer = db.Column(db.String(100), nullable=False)
    # 创建人
    creator = db.Column(db.String(128), nullable=False)
    # 创建时间
    create_time = db.Column(db.DateTime, default=datetime.now)
    # 最后修改人
    last_modify_user = db.Column(db.String(128), nullable=False)
    # 最后修改时间
    last_modify_time = db.Column(db.DateTime, default=datetime.now)
    # 该条记录是否可用，默认为0，可用
    is_del = db.Column(db.SmallInteger, default=0, nullable=False)
    # 做题记录表外键连接
    ques_reviews = db.relationship('wrong_ques_review', backref='wrong_ques_table')

    def __repr__(self):
        return "<wrong_ques_table %r>" % self.name


# 做题记录模型
class wrong_ques_review(db.Model):
    # 定义表名
    __tablename__ = 'wrong_ques_review'
    # 主键
    id = db.Column(db.BigInteger, primary_key=True)
    # 问题编号
    ques_id = db.Column(db.Integer, db.ForeignKey("wrong_ques_table.ques_id"),nullable=False)
    # 是否做对 1为做对 0为做错
    whether_right = db.Column(db.String(1))
    # 做题时间
    do_time = db.Column(db.DateTime, nullable = False)
    # 创建人
    creator = db.Column(db.String(128), nullable=False)
    # 创建时间
    create_time = db.Column(db.DateTime, default=datetime.now)
    # 最后修改人
    last_modify_user = db.Column(db.String(128), nullable=False)
    # 最后修改时间
    last_modify_time = db.Column(db.DateTime, default=datetime.now)
    # 该条记录是否可用，默认为0，可用
    is_del = db.Column(db.SmallInteger, default=0, nullable=False)


    def __repr__(self):
        return "<wrong_ques_review %r>" % self.name



# 学生基础信息表模型
class stu_info_table(db.Model):
    # 定义表名
    __tablename__ = 'stu_basic_info'
    # 主键
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    # 学生姓名
    stu_name = db.Column(db.String(128), nullable=False)
    # 学生学校
    stu_school = db.Column(db.String(100), nullable=False)
    # 创建账户时录入的年级
    create_class = db.Column(db.Integer, nullable=False)
    # 学生当前年级
    stu_class = db.Column(db.Integer, nullable=False)
    # 头像照片
    stu_profile = db.Column(db.String(200), nullable=False)
    # 学校表外键
    # school_id = db.Column(db.BigInteger, db.ForeignKey('school_table.id'), nullable=False)
    # 创建人
    creator = db.Column(db.String(128), nullable=False)
    # 创建时间
    create_time = db.Column(db.DateTime, default=datetime.now)
    # 最后修改人
    last_modify_user = db.Column(db.String(128), nullable=False)
    # 最后修改时间
    last_modify_time = db.Column(db.DateTime, default=datetime.now)
    # 该条记录是否可用，默认为0，可用
    is_del = db.Column(db.SmallInteger, default=0, nullable=False)
    # 学生成绩信息表外键连接
    score_tables = db.relationship('stu_score_table', backref = 'stu_basic_table')

    def __repr__(self):
        return "<stu_info_table %r>" % self.name


# 学生成绩信息表模型
class stu_score_table(db.Model):
    # 定义表名
    __tablename__ = 'stu_socre_table'
    # 主键
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    # 学生编号，与上表的id对应，作为上表外键
    stu_id = db.Column(db.BigInteger, db.ForeignKey('stu_basic_info.id'), nullable=False)
    # 学生录入的考试成绩
    score_offline = db.Column(db.Integer, nullable=False)
    # 考试所属年级
    score_exclass = db.Column(db.Integer, nullable=False)
    # 考试类型（月考、期中、期末、模拟考）
    score_exsort = db.Column(db.String(20))
    # 如果考试不属于上述考试类型就为单元名，反之为空
    exam_info = db.Column(db.String(30), nullable=True)
    # 创建人
    creator = db.Column(db.String(128), nullable=False)
    # 创建时间
    create_time = db.Column(db.DateTime, default=datetime.now)
    # 最后修改人
    last_modify_user = db.Column(db.String(128), nullable=False)
    # 最后修改时间
    last_modify_time = db.Column(db.DateTime, default=datetime.now)
    # 该条记录是否可用，默认为0，可用
    is_del = db.Column(db.SmallInteger, default=0, nullable=False)

    def __repr__(self):
        return "<stu_score_table %r>" % self.name

'''
# 学校表
class school_table(db.Model):
    # 定义表名
    __tablename__ = 'school_table'
    # 主键
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    # 学校名称
    school_name = db.Column(db.String(128), nullable=False)
    # 学校所属省级行政区（省、自治区、直辖市、特别行政区）
    school_province = db.Column(db.String(30), nullable=False)
    # 学校所属地级行政区（地级市、地区、自治州、盟）
    school_prefecture = db.Column(db.String(30), nullable=True)
    # 学校所属县级行政区（市辖区、县级市、县、自治县、旗、自治旗、林区、特区）
    school_county = db.Column(db.String(30), nullable=True)
    # 学校所属乡级行政区（镇、乡、民族乡、〔街道办事处/地区办事处管辖区域〕、苏木、民族苏木）
    school_countryside = db.Column(db.String(30), nullable=True)
    # 创建人
    creator = db.Column(db.String(128), nullable=False)
    # 创建时间
    create_time = db.Column(db.DateTime, default=datetime.now)
    # 最后修改人
    last_modify_user = db.Column(db.String(128), nullable=False)
    # 最后修改时间
    last_modify_time = db.Column(db.DateTime, default=datetime.now)
    # 该条记录是否可用，默认为0，可用
    is_del = db.Column(db.SmallInteger, default=0, nullable=False)
    # 学生基础信息表外键连接
    info_tables = db.relationship('stu_info_table', backref='school_table')

    def __repr__(self):
        return "<school_table %r>" % self.name
'''

# 学科表
class subject(db.Model):
    # 表名
    __tablename__ = "subject"
    # id
    subject_id = db.Column(db.Integer, primary_key=True)
    # 学科中文名称
    subject_name = db.Column(db.String(32), nullable=False)
    # 学科英文名
    subject_english_name = db.Column(db.String(32), nullable=False)
    # 创建人
    creator = db.Column(db.String(128), nullable=False)
    # 创建时间
    create_time = db.Column(db.DateTime, default=datetime.now)
    # 最后修改人
    last_modify_user = db.Column(db.String(128), nullable=False)
    # 最后修改时间
    last_modify_time = db.Column(db.DateTime, default=datetime.now)
    # 该条记录是否可用，默认为0，可用
    is_del = db.Column(db.SmallInteger, default=0, nullable=False)
    # 知识点表外键连接
    knowledge_basics = db.relationship('knowledge_basic', backref='subject')
    # 知识点等级表外键连接
    knowledge_levels = db.relationship('knowledge_level', backref='subject')
    # 章节表外键连接
    chapters = db.relationship('chapter', backref='subject')
    # 试题表外键连接
    questions_foreign = db.relationship('questions', backref='subject')

    def __repr__(self):
        return "<subject %r>" % self.name


# 教材版本表
class edition(db.Model):
    # 表名
    __tablename__ = "edition"
    # id
    edition_id = db.Column(db.Integer, primary_key=True)
    # 教材版本名
    edition_name = db.Column(db.String(32), nullable=False)
    # 创建人
    creator = db.Column(db.String(128), nullable=False)
    # 创建时间
    create_time = db.Column(db.DateTime, default=datetime.now)
    # 最后修改人
    last_modify_user = db.Column(db.String(128), nullable=False)
    # 最后修改时间
    last_modify_time = db.Column(db.DateTime, default=datetime.now)
    # 该条记录是否可用，默认为0，可用
    is_del = db.Column(db.SmallInteger, default=0, nullable=False)
    # 章节表外键连接
    chapters = db.relationship('chapter', backref='edition')

    def __repr__(self):
        return "<edition %r>" % self.name


# 学段名
class period(db.Model):
    # 表名
    __tablename__ = "period"
    # id
    period_id = db.Column(db.Integer, primary_key=True)
    # 学段名
    period_name = db.Column(db.String(32), nullable=False)
    # 创建人
    creator = db.Column(db.String(128), nullable=False)
    # 创建时间
    create_time = db.Column(db.DateTime, default=datetime.now)
    # 最后修改人
    last_modify_user = db.Column(db.String(128), nullable=False)
    # 最后修改时间
    last_modify_time = db.Column(db.DateTime, default=datetime.now)
    # 该条记录是否可用，默认为0，可用
    is_del = db.Column(db.SmallInteger, default=0, nullable=False)
    # 知识点表外键连接
    knowledge_basics = db.relationship('knowledge_basic', backref='period')
    # 知识点等级表外键连接
    knowledge_levels = db.relationship('knowledge_level', backref='period')
    # 章节表外键连接
    chapters = db.relationship('chapter', backref='period')

    def __repr__(self):
        return "<period %r>" % self.name


# 年级表
class grade(db.Model):
    # 表名
    __tablename__ = "grade"
    # id,三位数字表示，学段数字+年级数字+上下学期
    grade_id = db.Column(db.Integer, primary_key=True,
                         comment='三位数字表示，学段数字+年级数字+上下学期， 如小学一年级110，小学一年级上111，小学一年级下112，小学五年级下152，初中二年级上221')
    # 年级名
    grade_name = db.Column(db.String(32), nullable=False)
    # 创建人
    creator = db.Column(db.String(128), nullable=False)
    # 创建时间
    create_time = db.Column(db.DateTime, default=datetime.now)
    # 最后修改人
    last_modify_user = db.Column(db.String(128), nullable=False)
    # 最后修改时间
    last_modify_time = db.Column(db.DateTime, default=datetime.now)
    # 该条记录是否可用，默认为0，可用
    is_del = db.Column(db.SmallInteger, default=0, nullable=False)
    # 章节表外键连接
    chapters = db.relationship('chapter', backref='grade')
    # 试题表外键连接
    questions_foreign = db.relationship('questions', backref='grade')

    def __repr__(self):
        return "<grade %r>" % self.name


# 知识点表
class knowledge_basic(db.Model):
    # 表名
    __tablename__ = "knowledge_basic"
    # id
    knowledge_id = db.Column(db.Integer, primary_key=True)
    # 知识点名称
    knowledge_name = db.Column(db.String(32), nullable=False)
    # 关联学科id
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.subject_id'), nullable=False)
    # 关联学段
    period_id = db.Column(db.Integer, db.ForeignKey('period.period_id'), nullable=False)
    # 创建人
    creator = db.Column(db.String(128), nullable=False)
    # 创建时间
    create_time = db.Column(db.DateTime, default=datetime.now)
    # 最后修改人
    last_modify_user = db.Column(db.String(128), nullable=False)
    # 最后修改时间
    last_modify_time = db.Column(db.DateTime, default=datetime.now)
    # 该条记录是否可用，默认为0，可用
    is_del = db.Column(db.SmallInteger, default=0, nullable=False)
    # 知识点等级表外键关联
    knowledge_levels = db.relationship('knowledge_level', backref='knowledge_basic')
    # 试题知识点关联表外键连接
    relations = db.relationship('question_knowledge_relation', backref = 'knowledge_basic')

    def __repr__(self):
        return "<knowledge_basic %r>" % self.name


# 知识点等级表
class knowledge_level(db.Model):
    # 表名
    __tablename__ = 'knowledge_level'
    # id
    level_id = db.Column(db.Integer, primary_key=True)
    # 关联知识点表id
    knowledge_id = db.Column(db.Integer, db.ForeignKey('knowledge_basic.knowledge_id'), nullable=False)
    # 关联学科表id
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.subject_id'), nullable=False)
    # 关联学段表id
    period_id = db.Column(db.Integer, db.ForeignKey('period.period_id'), nullable=False)
    # 一级知识点id
    level_1_id = db.Column(db.Integer, nullable=False)
    # 一级知识点名称
    level_1_name = db.Column(db.String(32), nullable=False)
    # 二级知识点id，若无为0
    level_2_id = db.Column(db.Integer)
    # 二级知识点名称，若无为0
    level_2_name = db.Column(db.String(32))
    # 三级知识点id，若无为0
    level_3_id = db.Column(db.Integer)
    # 三级知识点名称，若无为0
    level_3_name = db.Column(db.String(32))
    # 创建人
    creator = db.Column(db.String(128), nullable=False)
    # 创建时间
    create_time = db.Column(db.DateTime, default=datetime.now)
    # 最后修改人
    last_modify_user = db.Column(db.String(128), nullable=False)
    # 最后修改时间
    last_modify_time = db.Column(db.DateTime, default=datetime.now)
    # 该条记录是否可用，默认为0，可用
    is_del = db.Column(db.SmallInteger, default=0, nullable=False)

    def __repr__(self):
        return "<knowledge_level %r>" % self.name


# 章节表
class chapter(db.Model):
    # 表名
    __tablename__ = 'chapter'
    # id
    chapter_id = db.Column(db.Integer, primary_key=True)
    # 关联学科表id
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.subject_id'), nullable=False)
    # 关联学段表id
    period_id = db.Column(db.Integer, db.ForeignKey('period.period_id'), nullable=False)
    # 关联版本表id
    edition_id = db.Column(db.Integer, db.ForeignKey('edition.edition_id'), nullable=False)
    # 关联年级表id
    grade_id = db.Column(db.Integer, db.ForeignKey('grade.grade_id'), nullable=False)
    # 章节代码，顺序增加
    chapter_code = db.Column(db.Integer, nullable=False)
    # 章节名
    chapter_name = db.Column(db.String(32), nullable=False)
    # 一级小节代码，顺序增加，若无则为0
    unit_code = db.Column(db.Integer, nullable=False)
    # 一级代码名称，若无则为0
    unit_name = db.Column(db.String(32), nullable=False)
    # 二级小节代码，顺序增加，若无则为0
    section_code = db.Column(db.Integer, nullable=False)
    # 二级小节名称,若无则为0
    section_name = db.Column(db.String(32), nullable=False)
    # 创建人
    creator = db.Column(db.String(128), nullable=False)
    # 创建时间
    create_time = db.Column(db.DateTime, default=datetime.now)
    # 最后修改人
    last_modify_user = db.Column(db.String(128), nullable=False)
    # 最后修改时间
    last_modify_time = db.Column(db.DateTime, default=datetime.now)
    # 该条记录是否可用，默认为0，可用
    is_del = db.Column(db.SmallInteger, default=0, nullable=False)

    def __repr__(self):
        return "<chapter %r>" % self.name


# 试题表
class questions(db.Model):
    # 表名
    __tablename__ = 'questions'
    # id
    ques_id = db.Column(db.BigInteger, primary_key=True)
    # 试题内容
    ques_content = db.Column(db.String(2048), nullable=False)
    # 答案1
    answer_1 = db.Column(db.String(2048), nullable=False)
    # 答案2,允许为空“”
    answer_2 = db.Column(db.String(2048), nullable=False)
    # 答案3，允许为空“”
    answer_3 = db.Column(db.String(2048), nullable=False)
    # 解析，允许为空""
    ques_analysis = db.Column(db.String(1024), nullable=False)
    # 识别结果包含知识点
    ocr_knowledge = db.Column(db.String(512), nullable=False)
    # ocr识别文字内容
    ocr_text = db.Column(db.String(1024), nullable=False)
    # 关联学科表id
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.subject_id'), nullable=False)
    # 关联年级表id
    grade_id = db.Column(db.Integer, db.ForeignKey('grade.grade_id'), nullable=False)
    # 创建人
    creator = db.Column(db.String(128), nullable=False)
    # 创建时间
    create_time = db.Column(db.DateTime, default=datetime.now)
    # 最后修改人
    last_modify_user = db.Column(db.String(128), nullable=False)
    # 最后修改时间
    last_modify_time = db.Column(db.DateTime, default=datetime.now)
    # 该条记录是否可用，默认为0，可用
    is_del = db.Column(db.SmallInteger, default=0, nullable=False)
    # 试题信息表外键连接
    question_infos = db.relationship('question_info', backref='questions')
    # 试题知识点关联表外键连接
    relations = db.relationship('question_knowledge_relation', backref = 'questions')

    def __repr__(self):
        return "<questions %r>" % self.name


# 试题信息表
class question_info(db.Model):
    # 表名
    __tablename__ = 'question_info'
    # id
    ques_info_id = db.Column(db.BigInteger, primary_key=True)
    # 关联questions表id
    ques_id = db.Column(db.BigInteger, db.ForeignKey('questions.ques_id'), nullable=False)
    # 试题难度，1-简单，2-中等，3-难题
    ques_difficulty = db.Column(db.SmallInteger, nullable=False, comment='1-简单，2-中等，3-难题')
    # 题型，没有则为0
    type_id = db.Column(db.Integer, db.ForeignKey('question_type.type_id'), nullable=False, default=0)
    # 题型名称
    type_name = db.Column(db.String(32), nullable=False)
    # 题目所属年份
    ques_year = db.Column(db.String(32), nullable=False)
    # 题目所属区域
    ques_area = db.Column(db.String(32), nullable=False)
    # 题目所属试卷类型,1-期中考试，2-期末考试，3-模考，4-中考真题，5-平时练习，6-单元检测，7-月考
    ques_paper_type = db.Column(db.SmallInteger, nullable=False,
                                comment='1-期中考试，2-期末考试，3-模考，4-中考真题，5-平时练习，6-单元检测，7-月考')
    # 创建人
    creator = db.Column(db.String(128), nullable=False)
    # 创建时间
    create_time = db.Column(db.DateTime, default=datetime.now)
    # 最后修改人
    last_modify_user = db.Column(db.String(128), nullable=False)
    # 最后修改时间
    last_modify_time = db.Column(db.DateTime, default=datetime.now)
    # 该条记录是否可用，默认为0，可用
    is_del = db.Column(db.SmallInteger, default=0, nullable=False)

    def __repr__(self):
        return "<question_info %r>" % self.name


# 题目类型表
class question_type(db.Model):
    # 表名
    __tablename__ = 'question_type'
    # id
    type_id = db.Column(db.Integer, primary_key=True)
    # 题型名称
    type_name = db.Column(db.String(32), nullable=False)
    # 创建人
    creator = db.Column(db.String(128), nullable=False)
    # 创建时间
    create_time = db.Column(db.DateTime, default=datetime.now)
    # 最后修改人
    last_modify_user = db.Column(db.String(128), nullable=False)
    # 最后修改时间
    last_modify_time = db.Column(db.DateTime, default=datetime.now)
    # 该条记录是否可用，默认为0，可用
    is_del = db.Column(db.SmallInteger, default=0, nullable=False)
    # 试题信息表外键连接
    question_infos = db.relationship('question_info', backref='question_type')

    def __repr__(self):
        return "<question_type %r>" % self.name


# 试题知识点关联表
class question_knowledge_relation(db.Model):
    __tablename__ = 'question_knowledge_relation'
    # id
    relation_id = db.Column(db.BigInteger, primary_key = True)
    # 关联试题表id
    ques_id = db.Column(db.BigInteger, db.ForeignKey('questions.ques_id'), nullable = False)
    # 关联知识点表id
    knowledge_id = db.Column(db.Integer, db.ForeignKey('knowledge_basic.knowledge_id'), nullable = False)
    # 创建人
    creator = db.Column(db.String(128), nullable=False)
    # 创建时间
    create_time = db.Column(db.DateTime, default=datetime.now)
    # 最后修改人
    last_modify_user = db.Column(db.String(128), nullable=False)
    # 最后修改时间
    last_modify_time = db.Column(db.DateTime, default=datetime.now)
    # 该条记录是否可用，默认为0，可用
    is_del = db.Column(db.SmallInteger, default=0, nullable=False)

    def __repr__(self):
        return "<question_knowledge_relation %r>" % self.name




if __name__ == "__main__":
#
# db.drop_all()
    db.create_all()


