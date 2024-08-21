#1-Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın
#2-Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu
#3-Gönderilen 2 sayı arasındaki tüm asal sayıları bulun
#4-Kendisine gönderilen bir sayının tam bölenlerinibir liste şeklinde döndüren

###############################
def kelimeyiGoster(kelime,n):
    for x in range(n):
        print(kelime)

kelime=input('Kelime Giriniz: ')
n=int(input('Kelimeyi kac kere gormek isteiyorsunuz: '))
kelimeyiGoster(kelime,n)
#Alternatif
# def yazdir(kelime,adet):
#     print(kelime*adet)

# yazdir('Merhaba\n',10)

##############################
def translate(*params):
    liste=[]
    
    for param in params:
        liste.append(param)

    return liste

result=translate(56,777,58,'Irem')
print(result)
##############################
def asalSAyilariBul(sayi1,sayi2):
    for sayi in range(sayi1,sayi2+1):
        if sayi>1:
            for i in range (2,sayi):
                if (sayi % i==0):
                    break
            else:
                    print(sayi)


sayi1=int(input('sayi 1: '))
sayi2=int(input('sayi 2: '))
asalSAyilariBul(sayi1,sayi2)
#############################

# def tambolenGonder(sayi):
#     for i in range(1,sayi+1):
#         if sayi%i==0:
#             print(i)

# tambolenGonder(12)

def tambolenGonder(sayi):
    tamBolenler=[]

    for i in range(2,sayi):
        if sayi%i==0:
            tamBolenler.append(i)
        
    return tamBolenler


sonuc=tambolenGonder(12)
print(sonuc)