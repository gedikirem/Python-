#class 

class Person:
    pass#yer tutucu
    # class attributes
    address= 'no information'
    #constructor(yapıcı metod)
    def __init__(self,name,year):#Obje üstüne bir değer atamak istediğimizde self i kullanırız
        #object attributes 
        self.name=name
        self.year=year
        print('init metodu çalıştı')
    # instance methods
    def intro(self):# self diyerek tanımlanan objenin bir referansını buraya vermek
        print('Hello There .I am '+self.name)

    #instance methods
    def calculateAge(self):
        return 2024-self.year

#object(instance)
p1=Person(name='ali',year=1990)#p1 objesi tanımlamış olduk
p2=Person(name='yağmur',year=1995)

#accessing object attributes
p1.intro()
p2.intro()

print(f'adım : {p1.name} ve yaşım: {p1.calculateAge()}')
print(f'adım : {p2.name} ve yaşım: {p2.calculateAge()}')

class Circle:
    #Class object attribute
    pi=3.14

    def __init__(self,yaricap=1):
        self.yaricap=yaricap

    #Methods 
    def cevre_hesapla(self):
        return 2*self.pi*self.yaricap
    
    def alan_hesapla(self):
        return self.pi*(self.yaricap**2)
    
c1=Circle()#yaricap=1
c2=Circle(5)

print(f'c1 : alan = {c1.alan_hesapla()} ve cevre= {c1.cevre_hesapla()}')
print(f'c2 : alan = {c2.alan_hesapla()} ve cevre= {c2.cevre_hesapla()}')