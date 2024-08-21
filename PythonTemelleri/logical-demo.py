#1-Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
# x=float(input('Sayi giriniz: '))
# result=(x>0) and (x<100)
# print(f'sayi 0-100 arasindami:{result}')

#2-Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz
# x=int(input('Sayi Giriniz: '))
# result= (x>0) and (x%2==0)
# print(f'Girilen sayi pozitif cift sayi mi:{result}')

#3-Email ve parola bilgileri ile giriş kontrolü yapınız
# kontrolMail="iremgedik@gmail.com"
# kontrolParola=1234
# email=input('Email giriniz: ')
# parola=int(input('Parola Giriniz:'))
# result=(kontrolMail==email) and (kontrolParola==parola)
#print(f'Uygulamaya giris basarili mi :{result}')

#4-Girilen 3 sayıyı büyüklük olarak karşılaştırınız
# sayi1=int(input('Sayi1 Giriniz: '))
# sayi2=int(input('Sayi2 Giriniz: '))
# sayi3=int(input('Sayi3 Giriniz: '))
# result= (sayi1>sayi2) and (sayi1>sayi3)
# print(f'sayi1 en büyük sayıdır :{result}')
# result= (sayi2>sayi1) and (sayi2>sayi3)
# print(f'sayi2 en büyük sayıdır :{result}')
# result= (sayi3>sayi2) and (sayi3>sayi1)
# print(f'sayi3 en büyük sayıdır :{result}')

#5-Kullanıcıdan 2 vize (%60) ve final(%40) notunu alıp ortalama hesaplayınız 
#Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın
#a-)Ortalama 50 olsa bile final notu en az 50 olmalıdır
#b-)Finalden 70 alındığında ortalamanın önemi olmasın 

# vize1=float(input('Vize1 Giriniz: '))
# vize2=float(input('Vize1 Giriniz: '))
# final=float(input('Final Giriniz: '))
#ortalama=((vize1+vize2)/2)*0.6 + (final*0.4)
# Sorgu=(ortalama>=50) and (final>=50)
# print(f'Ogrencinin ortalaması :{ortalama} ve gecme durumu :{result}')
#result=(ortalama>=50) or (final>=70)

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
zayif=(index>=0) and (index<=18.4)
normal=(index>=18.5) and (index<=24.9)
fazlakilolu=(index>=25) and (index<=29.9)
sisman=(index>=30) and (index<=34.9)

print(f'{name} kilo indeksin :{index} ve kilo degerlendirmenz zayif : {zayif}')
print(f'{name} kilo indeksin :{index} ve kilo degerlendirmenz normal : {normal}')
print(f'{name} kilo indeksin :{index} ve kilo degerlendirmenz kilolu: {fazlakilolu}')
print(f'{name} kilo indeksin :{index} ve kilo degerlendirmenz sisman : {sisman}')
#print(result)