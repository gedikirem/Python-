# ogrenciler={
#     '120':{
#         'ad':'Ali',
#         'soyad':'Yilmaz',
#         'telefon':'532 000 00 01'   
#         },
#           '125':{
#         'ad':'Can',
#         'soyad':'Korkmaz',
#         'telefon':'532 000 00 01'   
#         },
#           '128':{
#         'ad':'Volkan',
#         'soyad':'Yükselen',
#         'telefon':'532 000 00 01'   
#         }
# }
#1-Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle
#dictionary içinde saklayınız

#2-Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin

ogrenciler={}
number=input("Ogrenci numaraniz:")
name=input("Adiniz:")
surname=input("SoyAdiniz:")
phone=input("Telefon Numarasi:")

# ogrenciler[number]={
#     'ad':name,
#     'soyad':surname,
#     'telefon':phone,
# }

ogrenciler.update({
    number:{
    'ad':name,
    'soyad':surname,
    'telefon':phone,
    }
})
print(ogrenciler)
print('*'*50)
ogrNo=input('ögrenci no: ')
ogrenci=ogrenciler[ogrNo]

print(f"Aradiginiz {ogrNo} nolu ogrencinin adi:{ogrenci['ad']} saoyadi:{ogrenci['soyad']} ve telefonu ise {ogrenci['telefon']}")