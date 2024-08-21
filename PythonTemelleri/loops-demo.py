'''
1-100 arasında rastgele üretilecek bir sayıyı aşağı yukaro ifadeleri
ile buldurmaya çalışın

** "random modülü" için "python random" şeklinde arama yapın
** 100 üzerinden puanlama yapın .Her soru 20 puan
** Hak bilgisini kullanıcıdan alın ve her soru belirtilen
can sayısı üzerinden hesaplansın

'''
import random

#sayi=int(random.uniform(1,100))
sayi=random.randint(1,100)
print(sayi)
hak=int(input('Hak bilgisi girin:'))
for x in range(hak):
    tahmin=int(input(f'{x+1}.Tahmin girin '))
    if(sayi==tahmin):
        print(f'TEBRİKLER {x+1} denemede buldunuz.Toplam puanınız:{100- (100/hak) * (x)}')
        break
    elif(sayi>tahmin):
        print('Daha buyuk bir sayi giriniz ')
    else:
        print('Daha kucuk bir sayi giriniz')
    if x==hak-1:
        print('Hakkınız bitti ')