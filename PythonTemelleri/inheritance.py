#Inheritance(Kalıtım):Miras Alma 

#Person => name,lastname,age,eat(),run(),drink()
#Student(Person),Teacher(Person)

#Animal => Dog(Animal),Cat(Animal)

class Person():
    def __init__(self,fname,lname):
        self.firstName=fname
        self.lastName=lname
        print('Person Created')

    def who_am_i(self):
        print('I am a person')

    def eat(self):
        print('I am eating')


class Student(Person):
    def __init__(self,fname,lname,number):
        Person.__init__(self,fname,lname)#normalde üstteki metodu eziyor .Ama o metodun kullanılmasını istersek
        self.studentNumber=number#student a özel bir özellik eklemek istersek
        print('Student Created')
    #override
    def who_am_i(self):#Yukardaki metodu ezmek istersek
        print('I am a student')
    def sayHello(self):
        print('I am a student')

class Teacher(Person):
     def __init__(self,fname,lname,branch):
        super().__init__(fname,lname)#super la self i göndermemize gerek kalmıyor
        self.branch=branch
     def who_am_i(self):
         print(f'I am a {self.branch} teacher')

p1=Person('Ali','Yılmaz')
s1=Student('Irem','Gedik',4038)
t1=Teacher('Serkan','Yılmaz','Math')

t1.who_am_i()

print(p1.firstName + ' ' +p1.lastName)
print(s1.firstName + ' ' +s1.lastName+' '+str(s1.studentNumber))

p1.who_am_i()
s1.who_am_i()
p1.eat()
s1.eat()
s1.sayHello()