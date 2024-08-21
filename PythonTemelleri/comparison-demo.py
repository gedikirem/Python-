#1-Girilen 2 sayıdan hangisi büyüktür?
sayi=int(input('Sayi giriniz: '))
sayi2=int(input('Sayi giriniz: '))
result=(sayi>sayi2)
print(f'a: {sayi} b: {sayi2} den büyüktür:{result}')

#2-Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın
vize1=float(input('1.vize  giriniz: '))
vize2=float(input('2.vize giriniz: '))
final=float(input('final: '))
ortalama=(((vize1+vize2)/2) * 0.6)+(final * 0.4)
print(f'not ortalamasi : {ortalama} ve dersten geçme durumunuz :{ortalama>=50}')

#3-Girilen  bir sayının tek mi çift mi olduğunu yazdırınız
sayi=int(input('sayi:'))
tekcift=(sayi%2==0)
print(tekcift)
print(f'girilen sayi cift olma durumu {tekcift}')

#4-Girilen bir sayının negatif pozitif olma durumunu yazdırınız
sayi=int(input('sayi: '))
pozitifmi=(sayi>0)
print(f'girilen sayinin pozitif olma durumu {pozitifmi}')

#5-Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
#(email: email@iremgedik.com parola:abc123)

email='email@iremgedik.com '
password='abc123'

girilenEmail=input('email: ')
girilenPassword=input('parola: ')

isEmail=(email==girilenEmail.lower())
isPassword=(password==girilenPassword)
print(f'Email bilgisi dogrumu:{isEmail} ve Parola dogrumu: {password}')
