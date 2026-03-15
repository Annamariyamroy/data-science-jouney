'''class Student:
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
        print(f"My name is {self.name}. I am {self.age} years old. My mark obtained is {self.score}")
obj= Student("Anna",24,45)'''

'''class Student:
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score

    def greet(self):
        print(f"Hi! I'm {self.name} and I'm {self.age} years old.")
    def is_pass(self):
        if self.score>=50:
            return "PASS"
        else:
            return "FAIL"
    def get_grade(self):
        if self.score>=90:
            return"A"
        elif self.score>=80:
            return "B"
        elif self.score>=70:
            return "C"
        else:
            return "F"
        
s1 = Student("Anna", 24, 95)
s2 = Student("Arjun", 22, 45)

s1.greet()
print(s1.is_pass())
print(s1.get_grade())
print(s2.get_grade())'''

#Inheritance

'''class Book:
    def __init__(self,title,author,pages):
        self.title=title
        self.author= author
        self.pages=pages
    def describe(self):
        print(f"Title: {self.title} | Author: {self.author} | Pages: {self.pages}")
    def __str__(self):
        return(f"{self.title} written by {self.author} in Book")

class EBook(Book):
    def __init__(self,title,author,pages,file_size):
        super().__init__(title,author,pages)
        self.file_size=file_size
    def __str__(self):
        return(f"{self.title} written by {self.author} in Ebook")
    def describe(self):
        print(f"Title: {self.title} | Author: {self.author} | Pages: {self.pages} | Filesize: {self.file_size} MB")

class AudioBook(Book):
    def __init__(self,title,author,pages,duration):
        super().__init__(title,author,pages)
        self.duration= duration
    def __str__(self):
        return(f"{self.title} written by {self.author} in AudioBook")
    def describe(self):
        print(f"Title: {self.title} |  Author: {self.author} | Pages: {self.pages} | Duration: {self.duration} hours")
            


b  = Book("Python 101", "John", 300)
eb = EBook("Learn AI", "Sara", 250, 5)
ab = AudioBook("Data Science", "Mike", 400, 6)

#__str__ inside class is called when the object is printed(print(object)) or str(object) is called or the object is used in an f string formatting
b.describe()
print(b)
eb.describe()
result=str(eb)
print(result)
ab.describe()
print(f"Audio book description: {ab}")'''


'''class BankAccount:
    def __init__(self,owner,balance):
        self.owner= owner
        self.balance= balance
    def deposit(self,amount):
        self.amount=amount
        self.balance=self.balance+self.amount
        return(f"Deposited {self.amount}. New balance : {self.balance}")
    def withdraw(self,amount):
        self.amount=amount
        if(self.amount> self.balance):
            return("Insufficient funds!")
        else:
            self.balance= self.balance-self.amount
            return(f"Withdrew {self.amount}. New balance : {self.balance}")
    def __str__(self):
        return(f"Account holder: {self.owner} | Balance : {self.balance}")
    

acc =BankAccount("Anna",1000)
print(acc)
print(acc.deposit(500))
print(acc.withdraw(200))
print(acc.withdraw(2000))
print(acc)'''

#Class variable. shared by all objects , whereas instance variables are unique to each object
'''class Student:
    count=0
    def __init__(self,name):
        self.name=name
        Student.count += 1
s1=Student("Anna")
s2=Student("Rahul")
s3=Student("Megha")
print(Student.count)'''

# Usage of @property to declare a method as an attribute an to call them without brackets
'''class circle:
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return 3.14* self.radius**2
    
    @property
    def circumference(self):
        return 2*3.14*self.radius
obj= circle(4)
print(obj.area())
print(obj.circumference)'''


# Static methods .Doesnt need self. Can be called with class or object
'''class mathhelper:
    def add(a,b):
        return a+b
    def is_even(n):
        return True if n%2==0 else False
print(mathhelper.add(2,4))
print(mathhelper.is_even(5))'''

#practise question1 
'''class Student:
    student_count=0
    def __init__(self,name,scores):
        self.name=name
        self.scores= scores
        Student.student_count+=1
    def average(self):
        return sum(self.scores)/len(self.scores)
    def grade(self):
        if(self.average()>=85):
            return("A")
        elif (self.average()>=70):
            return ("B")
        elif (self.average()>=55):
            return("C")
        else:
            return("F")
    def __str__(self):
        return(f"Student({self.name} ,avg = {self.average():.1f}, grade={self.grade()}) ")
    def __repr__(self):
        return (f"Student(name = '{self.name}')")

class GraduateStudent(Student):
    def __init__(self,name,scores,thesis_topic):
        super().__init__(name,scores)
        self.thesis_topic= thesis_topic
    def __str__(self):
        return(f"{super().__str__()}, thesis = {self.thesis_topic} ")

    
s1 = Student("Arjun", [85, 91, 78, 88])
s2 = Student("Priya", [95, 97, 93, 99])
s3 = Student("Ravi",  [60, 55, 72, 48])
s4 = GraduateStudent("Sneha", [91, 88, 95],"NLP for Medical Diagnosis")

print(s1)
print(s2.grade())
all_students=[s1,s2,s3]
print(all_students)
print(repr(s1))#calls repr method
print([s1])#calls repr
top_student=max(all_students, key=lambda x: x.average())
print(f"Top student name: {top_student.name}")
print(s4)
print(s4.grade())
print(f"Total student count:{Student.student_count}")'''






    




    