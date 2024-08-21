# 1-100 e kadar
#Koşul false olana kadar devam eder

x=0
while x<=10:
    if x%2==1:#tek-çift sayılar
        print(f'sayi tek: {x}')
    else:
        print(f'sayi cift: {x}')
    x+=1
print('bitti..')

name= ''#False
while not name.split():#isim girene kadar devam et
    name=input('isminizi giriniz: ')

print(f'Merhaba {name}')

