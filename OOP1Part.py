"""class Cola ():
    def __init__(self, Brand , Color , Favorite):
        self.Brand = Brand
        self.Color = Color
        self.Favorite = Favorite

if __name__ == "__main__":
    Call1 = Cola("Coca Cola" , "Brown" , "Cola")
    Call2 = Cola("Pepsi" , "Black" , "Black")

print (Call1.Brand,'\n'+Call2.Brand)"""

"""class player ():
    pass

def demo_class ():
    Test1 = player()
    Test1.Fname = "SasiKarn"
    Test1.Lanme = "Srithud"
    Test1.Age = 19
    print (Test1.Fname,Test1.Lanme )

demo_class()"""
"""class Person ():
    def __init__(self , Fname , Lanme , Country="Thailand" ) :
        self.Fname = Fname
        self.Lname = Lanme
        self.Country = Country
    def __str__(self) :
        return"Fname : {} Lname : {} Country : {}".format(self.Fname,self.Lname,self.Country)

A = Person ("SasiKarn","Srithud",)
print (A.Fname,A.Lname,A.Country)
print (A)"""
#-------------------------------------------------------------------------------------------------
#Day2
#Self คืออะไร
"""class Medal ():
    def __init__(self ,country ,gold ,silver ,bronze):
        self.country = country
        self.gold=gold
        self.silver=silver
        self.bronze=bronze

    def total (self):
        return self.gold+self.silver+self.bronze

    def dummy (self,a,b):
        return a+b

if __name__=="__main__":
    Jp = Medal("Japan",5,5,5)
    print (Jp.country)
    print (Jp.total())
    print (Jp.dummy(1,2))
---------------------------------------------------------------------------------"""
#แปลงเป็นแบบ oop
"""class Bmi ():
    def __init__(self, w_kg , h_cm):
        self.h_cm = h_cm
        self.w_kg = w_kg
    def bmi (self):
        return self.w_kg / (self.h_cm / 100)**2
    def category (self):
        diag = ""
        if self.bmi() < 18.5 : 
            diag = "ผอม"
        elif self.bmi() > 18.5 and self.bmi() < 25:
            diag = "ตามเกณฑ์"
        elif self.bmi () > 25:
            diag = "ไออ้วน"
        return diag
    def __str__(self):
        return "BMI = {:.2f} ({})".format(self.bmi(),self.category())
if __name__ == "__main__":
    a = Bmi (90 , 178)
    print (a.h_cm,a.w_kg)
    print (a.bmi())
    print(a.category())
    print (a)"""

"""class Grade ():
    def __init__ (self , homework , midterm , final):
        self.homework = homework
        self.midterm = midterm
        self.final = final
    def total (self):
        return self.homework+self.midterm+self.final
    def category (self):
        diag = ""
        if self.total() < 50 :
            diag = "F"
        elif self.total() >= 50 and self.total() < 55 :
            diag = "D"
        elif self.total() >= 55 and self.total() < 60 :
            diag = "D+"
        elif self.total() >= 60 and self.total() < 65 :
            diag = "C"
        elif self.total() >= 65 and self.total() < 70 :
            diag = "C+"
        elif self.total() >= 70 and self.total() < 75 :
            diag = "B"
        elif self.total() >= 75 and self.total() < 80 :
            diag = "B+"
        elif self.total() >= 80 and self.total() < 101 :
            diag = "A"
        elif self.total() > 100 :
            diag = "Error"
        return diag
    def __str__(self):
        return "Grade : {:.1f} ({}) ".format(self.total(),self.category())
if __name__ == "__main__":
    Han = Grade (10 , 10 , 50)
    print (Han)"""


class Student ():
    def __init__(self,id_student,name_student):
        self.id_student = id_student
        self.name_student = name_student
    def total_score(self,thai,eng,scient):
        self.thai = thai 
        self.eng = eng
        self.scient = scient
    def categorythai (self):
        diag = 0
        if self.thai < 50 :
            diag = 0.0
        elif self.thai >= 50 and self.thai < 55 :
            diag = 1.0
        elif self.thai >= 55 and self.thai < 60 :
            diag = 1.5
        elif self.thai >= 60 and self.thai < 65 :
            diag = 2.0
        elif self.thai >= 65 and self.thai < 70 :
            diag = 2.5
        elif self.thai >= 70 and self.thai < 75 :
            diag = 3.0
        elif self.thai >= 75 and self.thai < 80 :
            diag = 3.5
        elif self.thai >= 80 and self.thai < 101 :
            diag = 4.0
        return diag
    def categoryeng (self):
        diag = 0
        if self.eng < 50 :
            diag = 0.0
        elif self.eng >= 50 and self.eng < 55 :
            diag = 1.0
        elif self.eng >= 55 and self.eng < 60 :
            diag = 1.5
        elif self.eng >= 60 and self.eng < 65 :
            diag = 2.0
        elif self.eng >= 65 and self.eng < 70 :
            diag = 2.5
        elif self.eng >= 70 and self.eng < 75 :
            diag = 3.0
        elif self.eng >= 75 and self.eng < 80 :
            diag = 3.5
        elif self.eng >= 80 and self.eng < 101 :
            diag = 4.0
        return diag
    def categoryscient (self):
        diag = 0
        if self.scient < 50 :
            diag = 0.0
        elif self.scient >= 50 and self.scient < 55 :
            diag = 1.0
        elif self.scient >= 55 and self.scient < 60 :
            diag = 1.5
        elif self.scient >= 60 and self.scient < 65 :
            diag = 2.0
        elif self.scient >= 65 and self.scient < 70 :
            diag = 2.5
        elif self.scient >= 70 and self.scient < 75 :
            diag = 3.0
        elif self.scient >= 75 and self.scient < 80 :
            diag = 3.5
        elif self.scient >= 80 and self.scient < 101 :
            diag = 4.0
        return diag
    def Avr (self):
        return (self.categorythai()+self.categoryeng()+self.categoryscient())/3


    def __str__(self):
        return "Thai = {:.1f} \nEng = {:.1f} \nSci = {:.1f} \nAverage Total = {:.1f} " .format(self.thai,self.eng,self.scient,self.Avr())

if __name__ == "__main__":
    # StudentList = [Student("64015130","Wanburhan"),Student("64015094","Phongpiphat")
    # ,Student("64015111","Puttiphong"),Student("64015222","Pom"),
    # Student("64015333","Guy"),]

    #  X = str(input (" : "))
    #  X=[Student for Student in StudentList if Student.id_student == X]
    #  for Student in X:
    #      print (Student.name_student)



    Han = Student("64015130","Wanburhan")
    Han.total_score(50,60,70)
    # print ("ID : "+Han.id_student+"\nName : "+Han.name_student)
    # print (Han)
    # print ("--"*10)

    Mark = Student("64015094","Phongpiphat")
    Mark.total_score(60,60,70)
    # print ("ID : "+Mark.id_student+"\nName : "+Mark.name_student)
    # print (Mark)
    # print ("--"*10)

    Phoon = Student("64015111","Puttiphong")
    Phoon.total_score(70,70,70)
    # print ("ID : "+Phoon.id_student+"\nName : "+Phoon.name_student)
    # print (Phoon)
    # print ("--"*10)

    Pom = Student("64015222","Pom")
    Pom.total_score(55,65,75)
    # print ("ID : "+Pom.id_student+"\nName : "+Pom.name_student)
    # print (Pom)
    # print ("--"*10)

    Guy = Student("64015333","Guy")
    Guy.total_score(80,80,80)
    # print ("ID : "+Guy.id_student+"\nName : "+Guy.name_student)
    # print (Guy)
    # print ("--"*10)

    Kuy = Student("64015444","Kuy")
    Kuy.total_score(10,10,10)
    # print ("ID : "+Kuy.id_student+"\nName : "+Kuy.name_student)
    # print (Kuy)
    # print ("--"*10)    

    StudentList = [Han,Mark,Phoon,Pom,Guy,Kuy]
    L = str(input ("Please Enter You : "))
    X=[Student for Student in StudentList if Student.id_student == L]
    for Student in X:
        print ("Name : "+Student.name_student)
        print (Student.__str__())

    if L in Han.id_student:
        print ("Han",True)
        print ("ID : "+Han.id_student+"\nName : "+Han.name_student)
        print (Han)
        print ("--"*10)
    if L in Mark.id_student:
        print ("Mark",True)
        print ("ID : "+Mark.id_student+"\nName : "+Mark.name_student)
        print (Mark)
        print ("--"*10)
    if L in Phoon.id_student:
        print ("Phoon",True)
        print ("ID : "+Phoon.id_student+"\nName : "+Phoon.name_student)
        print (Phoon)
        print ("--"*10)
    if L in Pom.id_student:
        print ("Pom",True)
        print ("ID : "+Pom.id_student+"\nName : "+Pom.name_student)
        print (Pom)
        print ("--"*10)
    if L in Guy.id_student:
        print ("Guy",True)
        print ("ID : "+Guy.id_student+"\nName : "+Guy.name_student)
        print (Guy)
        print ("--"*10)
    if L in Kuy.id_student:
        print ("Kuy",True)
        print ("ID : "+Kuy.id_student+"\nName : "+Kuy.name_student)
        print (Kuy)
        print ("--"*10)  





    
