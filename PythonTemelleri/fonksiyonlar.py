# def fonk(a,b) :
#   #  return a
#   if a>b:
#     return a
#   else:
#     return b

#fonk(5)
#print(fonk(5,10))

# def en_buyuk(a,b):
#   en_buyuk_sayi=fonk(a,b)
#   print(f'{en_buyuk_sayi}')

# en_buyuk(14,16)

# def deger_ayir(isim_soyisim):
#   isim=isim_soyisim.split()[0]
#   soyisim=isim_soyisim.split()[1]
#   return isim,soyisim

# print(deger_ayir("Irem Ge"))

# def deger_birlestir(isim,soyisim):
#     return " ".join([isim,soyisim])#boşluk olmasını istemiyorsak ""
# print(deger_birlestir(isim="irem",soyisim="gre"))

# def birlestir(*args):
#     return " ".join(args)
# print(birlestir(*args:"Irem","Beyza","Emir"))

def keywrd(**kwargs):
    if 'anahtar' in kwargs:
        print("Anahtar bulundu")

