sayilar=[1,3,5,7,9,12,19,21]

#1: sayilar listesini while ile ekrana yazdırın
x=0
while x<len(sayilar):
    print(sayilar[x])
    x+=1

#2-Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek saayıları ekrana yazdırın

bas_=int(input('Baslangic degeri giriniz: '))
bit_=int(input('Bitis degeri giriniz: '))

x=bas_
while x<bit_:
    if(x%2==1):
        print(x)
    x+=1

#3-1-100 arasındaki sayıları azalan şekilde yazdırın

x=100
while x>0:
    print(x)
    x-=1

#4-Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın

x=0
sayilar_=[]
while x<=5:
    sayi=int(input(f'{x}.sayi giriniz: '))
    sayilar_.append(sayi)
    x+=1

sayilar_.sort()#Sıralıyor
print(sayilar_)
#5-Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesini içinde saklayınız


# urunName=input('Urun adi giriniz: ')
# urunPrice=input('Urun fiyati giriniz: ')
# liste=[{'name': urunName,'price':urunPrice}]
# print(liste),

urunler=[]
adet=int(input('Urun sayisi girin : '))
i=0
while(i<adet):
    name=input('Urun ismi: ')
    price=input('urun fiyati: ')
    urunler.append({
        'name':name,
        'price':price
    })
    i+=1

for urun in urunler:
    print(f'urun adi:{urun["name"]} urun fiyati:{urun["price"]} ')