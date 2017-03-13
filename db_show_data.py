#!/usr/bin/env python
#coding:utf-8

from app import models

teachers = models.Teacher.query.all()
print '<Teacher>  tid  tname  password'
for t in teachers:
    print t.tid, t.tname, t.password
print ''


courses = models.Course.query.all()
print '<Course>  cid  cname  ctime  tid  cstunum'
for c in courses:
    print c.cid, c.cname, c.ctime, c.tid, c.cstunum
print ''


students = models.Student.query.all()
print '<Student>  sid  sname  sclass  surl'
for s in students:
    print s.sid, s.sname, s.sclass, s.surl
print ''


scourses = models.SCourse.query.all()
print '<SCourse>  scid  sid  cid'
for sc in scourses:
    print sc.scid, sc.sid, sc.cid
print ''


attendances = models.Attendance.query.all()
print '<Attendance>  aid  sid  cid  atime  aresult'
for a in attendances:
    print a.aid, a.sid, a.cid, a.atime, a.aresult
