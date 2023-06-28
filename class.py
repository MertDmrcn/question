# class


# class Person:
#    #class attributes
#     adress = 'no information'
    
    
#     # constructor(yapıcı method)
#     def __init__(self,name,year):
       
#     # object attributes
#      self.name=name
#      self.year=year
     
#     # instance methods
#     def intro(self):
#         # print("hello mert. I am "+ self.name)
    
#      def calculateAge(self):
#         return 2019 - self.year



# p1 = Person(name='ali',year=1990)
# p2= Person(name='mert',year=1995)


# p1.intro()
# p2.intro()

# print(f'adım: {p1.name} ve  yaşım: {p1.calculateAge()}')
# print(f'adım: {p2.name} ve  yaşım:{p2.calculateAge()}')

# class Circle:
#     # class object attribute
#     pi=3.14
    
#     def __init__(self,yaricap=1):
#         self.yaricap =yaricap
       
#     # methods
#     def cevre_hesapla(self):
#         return 2 * self.pi * self.yaricap
    
#     def alan_hesapla(self):
#         return self.pi * (self.yaricap**2)
    
# c1 = Circle() # yarıçap 1 eşittir
# c2= Circle(5)

# print(f'c1: alan = {c1.alan_hesapla()} çevre = {c1.cevre_hesapla()}')
# print(f'c2: alan = {c2.alan_hesapla()} çevre = {c2.cevre_hesapla()}')
# !//////////////////////////////////////

# Inheritance (Kalıtım): Miras Alma

class Person():
    def __init__(self,fname,lname):
        self.firstName = fname
        self.lastName = lname 
        print('Person Created')
    
    def who_am_i(self):
        print('I am a person')
    
    def eat(self):
        print("I am a eating")
        
    
class Student(Person):
    def __init__(self,fname,lname,number):
        Person.__init__(self, fname, lname)
        self.studentNumber = number
        
        print('Student Created')
    def who_am_i(self):
        print('I am a student')
    
    def sayHello(self):
        print('mERHABA BEN MERT')
        
class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname)
        self.branch =branch
        
    def who_am_i(self):
        print(f'I am a {self.branch}')
       




p1 = Person('ALİ','yılmaz')
s1 = Student('mert','demircan', 1234)

print(p1.firstName + ' ' + p1.lastName)
print(s1.firstName + ' ' + s1.lastName+ ' '+ str(s1.studentNumber))

p1.who_am_i()
s1.who_am_i()
s1.sayHello()
t1= Teacher('Serkan','Yılmaz','Matematik')
t1.who_am_i()

p1.eat()
s1.eat()