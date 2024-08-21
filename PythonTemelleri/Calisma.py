""" musteriAdi="Grotis"
musteriSoyad="Kitty"
AdSoyad=musteriAdi+' '+musteriSoyad
gender="he/him"
tc="1234512345"
birthDate=2020
age=2024-birthDate
print(AdSoyad)
print(gender)
print(age)
x=input("Number1: ")
y=input("Number2: ")
toplam=int(x)+int(y)
print(toplam)
 """
""" #Daire alanı hesaplama
pi=3.14
r=float(input("yaricap: "))
alan=pi*r**2
cevre=2*pi*r
print("Alan:"+str(alan)+" Cevre: "+str(cevre)) """

# x=5
# y=2.5
# name='Irem'
# isOnline=True

# print(type(x))
# print(type(y))
# print(type(name))
# print(type(isOnline))

# message='Hello There .My name is Irem Gedik'
# #message=message.upper#Tüm harfler büyük
# message=message.lower()
# message=message.split('.')
# print(message)

#SORULAR
# website="http://www.iremgedik.com"
# course="Python Kursu:Baştan Sona Python Programlama Rehberiniz(40 saat)"
# #1-SORU
# result=' Hello World '
# print(result.strip())
# #2-SORU
# result='www.iremgedik.com'.strip('w.moc')
# print(result)

# Liste=['BMW','Mercedes','Opel','Mazda']
# print(Liste)
# length=len(Liste)
# print(length)
# print(Liste[0])
# print(Liste[length-1])
# Liste[-1]='Toyota'
# print(Liste)
# result='Mercedes' in Liste
# print(result)
# names=['Ali','Yağmur','Hakan','Deniz']
# years=[1998,2000,1998,1987]

# names.append('Cenk')
# print(names)
# names.insert(0,'Sena')
# print(names)
# names.pop(-2)
# print(names)
# names.count('Ali')
# print(names)

# ogrenciler={
#     '120':{
#         'ad':'Ali',
#         'soyad':'Yilmaz',
#         'telefon':'532 000 00 01'
#     },
#      '125':{
#         'ad':'Can',
#         'soyad':'Korkmaz',
#         'telefon':'532 000 00 02'
#     },
#      '128':{
#         'ad':'Volkan',
#         'soyad':'Yükselen',
#         'telefon':'532 000 00 03'
#     },

# }
#print(ogrenciler)
# ogrenciler={}
# numara=int(input("Numara giriniz:"))
# name=input("öğrenci adi: ")
# surname=input("öğrenci soyad: ")
# phone=input("öğrenci telefon: ")

# ogrenciler[numara]={
#     'ad':name,
#     'soyad':surname,
#     'telefon':phone
# }
# print(ogrenciler)

# x,y,z=2,5,10

# sayi1=int(input('Sayi1 giriniz: '))
# sayi2=int(input('Sayi2 giriniz: '))

# # toplam=x+y+z
# # # Sonuc=(sayi1*sayi2)-toplam
# # print(Sonuc)

# result=sayi1>sayi2
# print(result)

# vize1=int(input('Vize1 giriniz: '))
# vize2=int(input('Vize2 giriniz: '))
# final=int(input('Final giriniz: '))

# Sonuc=(vize1+vize2)*0.6 +final*0.4
# print(Sonuc>50)

#Birinci
#x=int(input('Sayi Giriniz: '))

#result= (x>0 and x<=100)
#print(f'Sayinin 0-100 arasinda olma durumu :{result}')

#İkinci
#result= ((x>0) and (x%2==0))
#print(f'Pozitif cift sayi olma durumu {result}')

#Üçüncü
# email='iremgedik@gmail.com'
# parola='123'

# mail=input('Mail girin: ')
# password=input('Sifre giriniz: ')

# Control=(email==mail) and (parola==password)
# print(f'Eslesme : {Control}')

#Dördüncü
# num1=int(input('Birinci sayi: '))
# num2=int(input('İkinci sayi: '))
# num3=int(input('Üçüncü sayi: '))

# Result=num1>num2 and num3>num1
# print(f'{num3}>{num1}>{num2} den buyuktur : {Result}')

#Besinci
# vize1=int(input('Vize-1 : '))
# vize2=int(input('Vize-2 : '))
# final=int(input('Final: '))

# ortalama=(((vize1+vize2)/2)*0.6 + final*0.4)
# # gecmeKalma=((ortalama==50) or (ortalama>50))
# # print(f'Gecme durumu : {gecmeKalma}')

# #a
# gecmeKalma=(ortalama>=50 and final>=50)
# print(f' Ortalama :{ortalama} Final :{final} Gecme durumu : {gecmeKalma}')
# #b
# gecmeKalma=(ortalama>=50) or final>=70
# print(f'Gecme durumu :{gecmeKalma}')

#Altıncı 
kilo=float(input('Kilo Giriniz: '))
boy=float(input('Boy Giriniz: '))

formul=kilo/(boy**2)
print(f'indeks : {formul}')
zayif=formul>0 and formul<18.4
normal=formul>18.5 and formul<24.9
fazlakilolu=formul>25 and formul<29.9
sisman=formul>30 and formul<34.9

print(f'zayif :{zayif} normal :{normal} fazlakilolu :{fazlakilolu} sisman :{sisman}')
