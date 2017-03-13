#coding:utf-8

from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)

class Teacher(db.Model):
    tid = db.Column(db.Integer, primary_key = True)
    tname = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(64), index=True)

    def __init__(self, tname, password):
        self.tname = tname
        self.password = password

    def __repr__(self):
        return '<Teacher tid:%r, tname:%r, password:%r>' % (self.tid, self.tname, self.password)

class Student(db.Model):
    sid = db.Column(db.Integer, primary_key = True)
    sname = db.Column(db.String(64), index=True)
    sclass = db.Column(db.String(64), index=True)
    surl = db.Column(db.String(64), index=True)


    def __init__(self, sname, sclass):
        self.sname = sname
        self.sclass = sclass

    def __repr__(self):
        return '<Student sid:%r, sname:%r, sclass:%r, surl:%r>' % (self.sid, self.sname, self.sclass, self.surl)

class Course(db.Model):
    cid = db.Column(db.Integer, primary_key = True)
    cname = db.Column(db.String(64), index=True)
    ctime = db.Column(db.String(64), index=True)
    tid = db.Column(db.Integer, db.ForeignKey('teacher.tid'))
    cstunum = db.Column(db.Integer, index=True)


    def __init__(self, cname, ctime, tid):
        self.cname = cname
        self.ctime = ctime
        self.tid = tid
        self.cstunum = 0

    def __repr__(self):
        return '<Course cid:%r, cname:%r, ctime:%r, tid:%r, cstununm:%r>' % (self.cid, self.cname, self.ctime, self.tid,
                                                                             self.cstunum)

class SCourse(db.Model):
    scid = db.Column(db.Integer, primary_key = True)
    sid = db.Column(db.Integer)
    cid = db.Column(db.Integer)

    def __init__(self, sid, cid):
        self.sid = sid
        self.cid = cid

    def __repr__(self):
        return '<SCourse scid:%r, sid:%r, cid:%r' % (self.scid, self.sid, self.cid)

class Attendance(db.Model):
    aid = db.Column(db.Integer, primary_key = True)
    sid = db.Column(db.Integer)
    cid = db.Column(db.Integer)
    atime = db.Column(db.DateTime(), default=datetime.utcnow)
    aresult = db.Column(db.String(64))

    def __init__(self, sid, cid, atime, aresult):
        self.sid = sid
        self.cid = cid
        self.atime = atime
        self.aresult = aresult

    def __repr__(self):
        return '<Absent aid:%r, sid=%r, cid=%r, atime=%r, aresult=%r' % (self.aid, self.sid, self.cid, self.atime, self.aresult)

