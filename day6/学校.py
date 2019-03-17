# -*- coding:utf-8 -*-
class School(object):
    def __init__(self,name,addr):
        self.name=name
        self.addr=addr
        self.students=[]
        self.staffs=[]
    def entroll(self,stu_obj):
        print("%s is注册成功"% stu_obj.name)
        self.students.append(stu_obj)
    def hire(self,staff_obj):
        print("%s 老师注册成功"% staff_obj.name)
        self.staffs.append(staff_obj)
class SchoolMember(object):
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def tell(self):
        pass



class Teacher(SchoolMember):
    def __init__(self,name,age,sex,salary,courser):
        super(Teacher,self).__init__(name,age,sex)
        self.salary=salary
        self.coures=courser
    def tell(self):
        print("""
        info of teacher
        name:%s,
        age:%s,
        sex:%s
        salary:%s,
        course:%s
        """ %(self.name,self.age,self.sex,self.salary,self.coures))
    def teach(self):
        print("%s is teache [%s]"% (self.name,self.coures))

class Students(SchoolMember):
    def __init__(self,name,age,sex,stu_id,gradge):
        super(Students,self).__init__(name,age,sex)
        self.stu_id=stu_id
        self.gradge=gradge
    def tell(self):
        print("""
        info of student
        name:%s,
        age:%s,
        sex:%s
        stu_id %s,
        gradge:%s
        """ %(self.name,self.age,self.sex,self.stu_id,self.gradge))
    def pay_tution(self,aoount):
        print("%s is pay %s"% (self.name,aoount))

school=School("老男孩IT","沙河")
t1=Teacher("oldboy","55","MF",20000,"Linux")
t2=Teacher("Alex","30","MF",3000,"PythonDevelops")
s1=Students("chengronghua","30","MF",1001,"PythonDevelops")
s2=Students("梁伟","30","MF",1001," Linux")

t1.tell()
s1.tell()
school.entroll(s1)
school.entroll(s2)
school.hire(t1)
print(school.students[0])
print(school.staffs[0])
school.staffs[0].teach()

for i in school.students:
    i.pay_tution(500)