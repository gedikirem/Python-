#Soru-1)Kullanıcıdan bir sayı alan ve bu sayının faktöriyelini hesaplayan python kodunu yazınız
#SOru-2)Kullanıcıdan alınan 2  sayının en büyük ortak bölenini hesaplayan python k
#Soru-3)Kullanıcıdan alınan sayının asal olup olmadığını kontrol eden 
#Soru-4)Kullanıcıdan alınan sayı kadar fibonacci serisi oluşturan 
#Soru-5)Kullanıcıdan kelime veya cümle alan ve bu kelime veya cümlenin palindrome olup olmadığını

# sayi=int(input("sayi giriniz:"))
# faktoriyel=1
# while sayi>0:
#     faktoriyel=faktoriyel*sayi
#     sayi=sayi-1
  
# print(faktoriyel)

sayi1=int(input("1.sayi giriniz"))
sayi2=int(input("2.sayi giriniz"))

while sayi2:
    sayi1,sayi2=sayi2,sayi1%sayi2
    print(sayi1)

# sayi3=int(input("sayi giriniz"))
# t=0
# for i in range(2,sayi3):
#      if( sayi3 % i== 0):
#         t=t+1

# if t>0:
#     print("Asal degil")
# else:
#     print("Asal ")

# n=int(input("N degeri giriniz"))
# secondDeger=1
# # 1 1 2 3 5 8
# firstDeger=0
# fibonacci=1
# for i in range(1,n):
#     fibonacci=firstDeger+secondDeger
#     firstDeger=secondDeger
#     secondDeger=fibonacci

# print(fibonacci)


str=str(input("Kelime giriniz"))
print(str.split())