
sayilar=[1,3,5,7,9,12,19,21]
#1-Sayılar listesindeki hangi sayılar 3 'ün katıdır ?
#2-Sayılar listesindeli sayıların toplamı kaçtır ?
#3-Sayılar listesindeki tek sayıların karesini alınız

for num in sayilar:
    if num%3==0:
        print(num)


toplam=0
for num in sayilar:
    toplam+=num

print(f'Toplam:{toplam}')

for num in sayilar:
    if num%2!=0:
        print(num**2)

sehirler=['kocaeli','istanbul','ankara','izmir','rize']
for city in sehirler:
    if city.__len__()<=5:
        print(city),

for sehir in sehirler:
    if (len(sehir) <=5):
        print(sehir)



urunler=[
    {'name':'samsung S6','price':'3000'},
    {'name':'samsung S7','price':'4000'},
    {'name':'samsung S8','price':'5000'},
    {'name':'samsung S9','price':'6000'},
    {'name':'samsung S10','price':'7000'},
]
#5-Ürünlerin fiyatları toplamı ?
toplam=0
for urun in urunler:
    fiyat=int(urun['price'])
    toplam+=fiyat

print(toplam)

#6-Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz ?
for urun in urunler:
    if int(urun['price']) <=5000:
        print(urun['name'])






