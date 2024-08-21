# 1-Kullanıcıdan isim ,yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz.
# Ehliyet alma koşulu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır

name=input('İsim giriniz: ')
age=int(input('Yas giriniz: '))
egitimDurumu=input('Eğitim Durumu giriniz: ')

if (age>=18):
    if(egitimDurumu=='lise' or egitimDurumu=='üniversite'):
     print(f'{name} ehliyet almaya hak kazanmistir')
    else:
       print('egitim durumunuz yetersiz ehliyet alamazsiniz')
else:
    print('Yasiniz tutmuyor ehliyet alamazsiniz')



#2-Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre not aralığına karşılık gelen not bilgisini yazdırın
#0-24 =>0
#25-44 =>1
#45-54 =>2
#55-69 =>3
#70-84 =>4
#85-100 =>5
    
# yaziliNot1=float(input('Yazili Not-1: '))
# yaziliNot2=float(input('Yazili Not-2: '))
# sozluNot=float(input('Sozlu Not: '))

# ortalama=(yaziliNot1+yaziliNot2+sozluNot)/3
# if ortalama>0 and ortalama<24:
#     print(f'Ortalamaniz:{ortalama} not bilginiz: 0')
# elif ortalama>25 and ortalama<44:
#      print(f'Ortalamaniz:{ortalama} not bilginiz: 1')
# elif ortalama>45 and ortalama<54:
#      print(f'Ortalamaniz:{ortalama} not bilginiz: 2')
# elif ortalama>55 and ortalama<69:
#      print(f'Ortalamaniz:{ortalama} not bilginiz: 3')
# elif ortalama>70 and ortalama<84:
#      print(f'Ortalamaniz:{ortalama} not bilginiz: 4')
# elif ortalama>85 and ortalama<100:
#      print(f'Ortalamaniz:{ortalama} not bilginiz: 5')
# else:
#      print('Ortalamaniz aralik disindadir')

#3-Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız
#1.Bakım =>1.yıl
#2.Bakım =>2.yıl
#3.Bakım =>3.yıl
#4.Bakım =>4.yıl

#** Süre hesabını alınan gün,ay,yıl bilgisine göre gün bazlı hesaplayınız
#*** datetime modülünü kullanmanız gerek
#(2018/8/1)
# from datetime import datetime
# dir(datetime)
# gun=int(input('Gun giriniz: '))
# ay=int(input('Ay giriniz: '))
# yil=int(input('Yil  giriniz: '))
# tarih = datetime(yil,ay,gun) 
# şu_an = datetime.now()
# fark=tarih-şu_an

# if fark.days<=365:
#     print('1.Bakim')
# elif fark.days>365 and fark.days<=365*2:
#     print('2.Bakim')
# elif fark.days>365*2 and fark.days<=365*3:
#     print('3.Bakim')
# else:
#    print('Hatali süre bilgisi')


import datetime
tarih=input('araciniz hangi tarihte tarfige cikti: ')
tarih=tarih.split('/')

# print(tarih[0])
# print(tarih[1])
# print(tarih[2])

trafigeCikis=datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi=datetime.datetime.now()
fark=simdi-trafigeCikis
days=fark.days


if fark.days<=365:
 print('1.Bakim')
elif fark.days>365 and fark.days<=365*2:
     print('2.Bakim')
elif fark.days>365*2 and fark.days<=365*3:
     print('3.Bakim')
else:
   print('Hatali süre bilgisi')