#!/usr/bin/python3.5
# _*_ coding: utf-8 _*_
# 继承示例 
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

class Teacher(SchooleMember):
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

if __name__ == '__main__':
    t1 = SchooleMember("Alex",22)
    t1.enroll()
    t2 = Teacher("A1",23,'Python',20000)
    t2.teaching()


