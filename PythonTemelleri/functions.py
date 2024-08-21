def sayHello(name ='user'):#varsayılan olarak user bilgisi aktarılıyor
    print('Hello '+ name)

sayHello('Irem')
sayHello('Beyza')
sayHello('Emirhan')
sayHello('Metehan')
sayHello()

def sayHello(name ='user'):#varsayılan olarak user bilgisi aktarılıyor
    return 'Hello '+name

msg=sayHello('Cınar')
print(msg)


def total (num1,num2):
    return num1+num2

topla=total(5,4)
print(topla)

def yasHesapla(dogumYili):
    return 2024-dogumYili

ageIrem=yasHesapla(2003)
print(ageIrem)

def EmekliligeKacYilKaldi(dogumYili,isim):

    yas=yasHesapla(dogumYili)
    emeklilik=65-yas
    if emeklilik>0:
        print(f'emekliliginize {emeklilik} yil kaldi')
    else:
        print('Zaten emekli oldunuz')

EmekliligeKacYilKaldi(2003,'Irem')

# list=[1,2,3]
# print(help(list.append))


