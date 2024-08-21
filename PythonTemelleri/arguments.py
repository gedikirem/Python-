def changeName(n):
    n='ada'

name='irem'
changeName(name)
print(name)

def change (n):
    n[0]='istanbul'#adres kopyalama yapıyor 

sehirler=['ankara','izmir']
#change(sehirler)
change(sehirler[:])

print(sehirler)

n=sehirler#adres kopyalama
n=sehirler[:]#şehirler dizisinin tüm elemanlarını n ismindeki  diziye aktar SLICING İŞLEMİ
n[0]='istanbul'
print(sehirler)
print(n)#güncelleme yapmaz ,değişken gibi

def add(a,b,c=0):#3 parametreli fonksiyonun da çalışmasını istersek
    return sum((a,b,c))

print(add(10,20))
print(add(10,20,30))

def add(*params):#istediğimiz kadar parametre göndersekte toplar
    print(params)#gönderdiğimiz tüm parametreleri tuple listesiyle yazdırır
    return sum((params))

print(add(10,20,300,45,67,89))

def add(*params):
    sum=0

    for n in params:
        sum=sum+n
    
    return sum

def displayUser(**args):#dictionary
    for key,value in args.items():
        print('{} is {}'.format(key,value))



displayUser(name='Irem',age=20,city='malatya')
displayUser(name='Mete',age=8,city='adana',phone='123123')
displayUser(name='Yagmur',age=21,city='mardin',phone='123123',email='yagmur@gmail.com')

def myFunc(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50,key1='value1',key2='value2')