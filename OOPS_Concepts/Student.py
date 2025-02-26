class Student:
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def check_pass_fail(self):
        if self.score >= 40:
            return True
        else:
            return False

student1 = Student("Rajesh",45)
print(student1.check_pass_fail())
student2 = Student("Rohini",31)
print(student2.check_pass_fail())