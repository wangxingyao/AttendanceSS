#!venv/bin/python
#coding:utf-8

from app import db, models

# 添加老师信息
teachers = [
    (u'张翔', '123'),
    (u'wang', '123'),
    (u'费蓉', '123')
]
for teacher in teachers:
    t = models.Teacher(tname=teacher[0], password=teacher[1])
    db.session.add(t)
db.session.commit()


# 添加课程信息
courses = [
    (u'C语言', u'11', u'张翔'),
    (u'English', u'11', u'wang'),
    (u'Language C', u'22', u'wang'),
    (u'RFID', u'33', u'wang'),
    (u'软件工程', u'33', u'费蓉')
]
for course in courses:
    tname = course[2]
    teacher = models.Teacher.query.filter_by(tname=tname).first()
    if teacher == None:
        print ('添加课程失败:%r' % course[0])
        print ('不存在此老师:%r' % tname)
        continue
    c = models.Course(cname=course[0], ctime=course[1], tid=teacher.tid)
    db.session.add(c)
db.session.commit()


# 添加学生信息
students = [
    (u'王兴耀', u'ww141'),
    (u'杨乔英', u'jsj143'),
    (u'刘慧', u'ww141'),
    (u'王璞劼', u'ww141'),
    (u'王新宇', u'jsj143')
]
for student in students:
    s = models.Student(sname=student[0], sclass=student[1])
    db.session.add(s)
db.session.commit()


# 添加选课信息
scourses = [
    (u'王兴耀', u'C语言', u'张翔'),
    (u'杨乔英', u'C语言', u'张翔'),
    (u'刘慧', u'C语言', u'张翔'),
    (u'王璞劼', u'C语言', u'张翔'),
    (u'王新宇', u'C语言', u'张翔'),
    (u'王兴耀', u'English', u'wang'),
    (u'杨乔英', u'English', u'wang'),
    (u'刘慧', u'English', u'wang'),
    (u'王璞劼', u'English', u'wang'),
    (u'王新宇', u'English', u'wang')
]
for scourse in scourses:
    sname = scourse[0]
    student = models.Student.query.filter_by(sname=sname).first()
    if student == None:
        print ('该学生不存在:%r' % sname)
        continue
    tname = scourse[2]
    teacher = models.Teacher.query.filter_by(tname=tname).first()
    if teacher == None:
        print ('该老师不存在:%r' % tname)
        continue
    cname = scourse[1]
    course = models.Course.query.filter_by(cname=cname, tid=teacher.tid).first()
    if course == None:
        print ('该课程不存在:%r' % cname)
        continue
    sc = models.SCourse(sid=student.sid, cid=course.cid)
    db.session.add(sc)

    course = models.Course.query.filter_by(cname=cname, tid=teacher.tid).first()
    course.cstunum += 1
    db.session.add(course)
db.session.commit()

