x,y,z=2,5,10
numbers=1,5,7,10,6
#1-Kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir?
sayi1=int(input("sayi giriniz"))
sayi2=int(input("sayi giriniz"))

carp=sayi1*sayi2
result=carp-(x+y+z)
print(result)

#2-y'nin x'e kalansız bölümünü hesaplayınız
print(y//x)

#3-(x,y,z) toplamının mod 3'ü nedir?
print((x+y+z)%3)

#4-y'nin x.kuvvetini hesaplayınız
print(y**x)

#5-x,*y,z=numbers işlemine göre z'nin küpü kaçtır
numbers=1,5,7,10,6
x,*y,z=numbers
print(z**3)

#6-x,*y,z=numbers işlemine göre y nin değerler toplamı kaçtır
numbers=1,5,7,10,6
x,*y,z=numbers
result=y[0]+y[1]+y[2]
print(result)