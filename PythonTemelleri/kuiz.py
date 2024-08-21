import random


Liste=[]
def ListeyiOlustur(sayi):
    if(sayi%3==0):
        Liste.append(sayi)
    return Liste


print("İki sayi giriniz")
sayi1=int(input("Birinci sayi : "))
sayi2=int(input("İkinci sayi : "))
for i in range(sayi1,sayi2):
    ListeyiOlustur(i)

print(Liste) 



""" Liste=[]

def ListeyiOlustur(sayi):
        Liste.append(sayi)
    

print("İki sayi giriniz")
sayi1=int(input("Birinci sayi : "))
sayi2=int(input("İkinci sayi : "))
for i in range(sayi1,sayi2):
    sayi3=random.uniform(sayi1,sayi2)
    ListeyiOlustur(sayi3)

print(Liste) 
 """

# Liste=[]
# def ListeyiOlustur(sayi):
#           Liste.append(sayi)


# for i in range (0,4):
#       sayi=int(input(f"{i+1}.sayi : "))
#       ListeyiOlustur(sayi)


# print(Liste)

# List=[]
# for i in  range(0,4):
        
#         gecici=Liste[i]
#         Liste[i]=Liste[i+1]
#         Liste[i+1]=gecici
#         List.append(Liste[i-1])
#         List.append(gecici)


# print("Yeni Liste")

# print(Liste) 

