'''
1-Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz

sayi=float(input('sayı: ))
result=(sayi>0) and (sayi<=100)
print(f'sayı 0-100 arasındamı: {result}')

'''
sayi=float(input('sayi: '))

if (sayi>0) and (sayi<=100):
    print('sayi 0-100 arasinda')
else:
    print('sayi 0-100 arasinda degil')

'''
2-Girilen bir sayının pozitif çift sayi olup olmadığını kontrol ediniz

sayi=int(input('sayi: '))
result=(sayi>0) and (sayi% 2==0)
print(f'sayı pozitif cift sayı mı: {result}')

'''

sayi=int(input('sayi: '))
if sayi>0:
   if sayi%2==0:
    print('sayi pozitif cift')
   else:
    print('sayi pozitif tektir')
else:
    if(sayi%2==0):
      print('sayi negatif cifttir')
    else:
       print('sayi negatif tektir')


'''
3-Email ve parola bilgileri ile giriş kontrolü yapınız

email='emailiremgedik.com'
password='abc123'

girilenEmail=input('email: ')
girilenPassword=input('password: ')

result=(girilenEmail==email) and (girilenPassword==password)
print(f'uygulmaya giriş başarılı mı: {result})


'''
email='emailiremgedik.com'
password='abc123'

girilenEmail=input('Username giriniz: ')
girilenPassword=input('Sifre giriniz: ')

if(girilenEmail==email):
    if(girilenPassword==password):
        print('Hoş Geldiniz')
    else:
        print('Parola Bilgisi Yanlis')
else:
    print('Email Yanlis')

'''
4-Girilen 3 sayıyı büyüklük olarak karşılaştırınız

'''
a=int(input('a:'))
b=int(input('b:'))
c=int(input('c:'))

if (a>b) and (a>c):
   print('a en buyuk sayidir')
elif (b>a) and (b>c):
   print('b en buyuk')
else:
   print('c en buyuk')

'''
5-Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız

'''
vize1=float(input('Vize1 Giriniz: '))
vize2=float(input('Vize1 Giriniz: '))
final=float(input('Final Giriniz: '))
ortalama=((vize1+vize2)/2)*0.6 + (final*0.4)
# Sorgu=(ortalama>=50) and (final>=50)
# print(f'Ogrencinin ortalaması :{ortalama} ve gecme durumu :{result}')
#result=(ortalama>=50) or (final>=70)
if (ortalama>=50):
   if (final>=50):
      print(f' Ortalama :{ortalama} Basarili')
   else:
       print(f' Ortalama :{ortalama} Basarisiz.Final en az 50 olmali')
else:
   print(f' Ortalama :{ortalama} Basarisiz')
   

#6-Kişinin ad,kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#Formül :(Kilo/boy uzunluğunun karesi)
#Aşağıdaki tabloya göre kişşi hangi gruba girmektedir.
#0-18.4 => Zayıf
#18.5-24.9 =>Normal
#25.0-29.9=>Fazla Kilolu
#30.0-34.9=>Şişman(Obez)
   
name=input('adiniz: ')
kg=float(input('kilonuz: '))
hg=float(input('boyunuz: '))

index=(kg) / (hg**2)
if (index>=0) and (index<=18.4):
   print(f'{name} kilo indeksin :{index} ve kilo degerlendirmenz zayif ')
elif (index>=18.5) and (index<=24.9):
   print(f'{name} kilo indeksin :{index} ve kilo degerlendirmenz normal')
elif (index>=25) and (index<=29.9):
   print(f'{name} kilo indeksin :{index} ve kilo degerlendirmenz kilolu')
else:
   print(f'{name} kilo indeksin :{index} ve kilo degerlendirmenz sisman ')