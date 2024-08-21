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
    #methods


#object(instance)
p1=Person(name='ali',year=1990)#p1 objesi tanımlamış olduk
p2=Person(name='yağmur',year=1995)

#updating
p1.name='ahmet'
p1.address='kocaeli'
#accessing object attributes
print(f'p1 name: {p1.name} year: {p1.year} adress:{p1.address}')
print(f'p2 name: {p2.name} year: {p2.year} address:{p2.address}')

print(p1)
print(p2)

print(type(p1))
print(type(p2))

print(p1==p2)
