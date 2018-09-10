class Person:
    name = ""
    age =0
    department=""
    def __init__(self,name="",age=0,department=""):
        self.name=name
        self.age=age
        self.department=department
    def get_name(self):
        return self.name

class Student(Person):
    id=""
    GPA=0
    department=""
    advisor=""
    def __init__(self,name="",age=0,department="",id="",GPA=0):
        Person.__init__(self, name=name, age=age,department=department)
        self.id=id
        self.GPA = GPA
        self.advisor=""
    def print(self):
        print("제 이름은 {0}, 학과는 {1}, 나이는 {2}, 지도교수님은 {3}입니다".format(self.name,self.department,self.age,self.advisor))
    def reg_advisor(self,professor):
        self.advisor=professor.name
class Professor(Person):
    position=""
    laboratory=""
    student=[]
    def __init__(self,name="",age=0,department="",position="",laboratory=""):
        Person.__init__(self,name=name,age=age,department=department)
        self.position=position
        self.laboratory=laboratory

    def print(self):
        print("제 이름은 {0}, 학과는 {1}, 나이는 {2}, 지도학생은 {3}입니다".format(self.name,self.department,self.age,self.student))
    def reg_student(self,student):
        self.student.append(student.name)

stu1 = Student('Kim', 30, 'Computer',20001234, 4.5)
stu2 = Student('Lee', 22, 'Computer',20101234, 0.5)
prof1 = Professor('Lee', 55, 'Computer','Full', 'KLE')
stu1.reg_advisor(prof1)
stu2.reg_advisor(prof1)
prof1.reg_student(stu1)
prof1.reg_student(stu2)
stu1.print()
stu2.print()
prof1.print()