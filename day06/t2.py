#!/usr/bin/python3.5
# _*_ coding: utf-8 _*_
# 继承示例 
# Inheritance

import sys

class SchooleMember(object):
    members = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def tell(self):
        pass
    def enroll(self):
        '''注册'''
        SchooleMember.members += 1
        print("\033[32;1m new member [%s] is enrolled, not there are [%s] members. \033[0m " %(self.name, SchooleMember.members))
    def __del__(self):
        '''析构方法'''
        print("\033[31;1mmember [%s] is dead! \033[0m" %self.name)

class Relation(object):
    def make_friends(self,obj):
        print("%s is making friends with %s" %(self.name, obj.name))

class Teacher(SchooleMember,Relation):
    def __init__(self,name,age, course, salary):
        super(Teacher,self).__init__(name,age)
        self.course = course
        self.salary = salary
        self.enroll()
    def teaching(self):
        '''讲课方法'''
        print("Teacher [%s] is teaching [%s] for class [%s] " %(self.name, self.course, 's12' ))
    def tell(self):
        '''自我介绍'''
        msg = '''Hi, my name is [%s], work for [%s] as a [%s] teacher !''' %(self.name, 'Oldboy', self.course)
        print(msg)

class Student(SchooleMember,Relation):
    def __init__(self, name, age, grade, sid):
        super(Student,self).__init__(name,age)
        self.grade = grade
        self.sid = sid
        self.enroll()
    def tell(self):
        '''自我介绍方法'''
        msg = '''Hi, my name is [%s], I'm studying [%] in [%s]!''' %(self.name, self.grade, 'Oldboy')
        print(msg)

if __name__ == '__main__':
    t1 = Teacher("A1",23,'Python',20000)
    t2 = Teacher("TengLan",29,'Linux',3000)

    s1 = Student("Qinghua",24,'Python S12', 1483)
    s2 = Student("SanJiang",26,'Pyton S12', 1484)

    t1.teaching()
    t2.teaching()
    t1.tell()
    t1.make_friends(s1)

