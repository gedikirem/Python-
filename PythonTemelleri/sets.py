#Set listeleri
fruits={'orange','apple','banana'};

#print(fruits[0]) normal listeden farkı :indekslenemez 
#sıralamayız
#Bir elemandan yalnızca bir kere var
for x in fruits:
    print(x)

fruits.add('cherry')
fruits.update(['mango','grape'])#listede gönderebiliriz
print(fruits)

myList=[1,2,5,4,4,2,1]
print(myList)
print(set(myList))#sete çeviriyor

fruits.remove('mango')
fruits.discard('apple')
print(fruits)
fruits.pop()#rastgele silme işlemi olur çünkü sıralı bir liste değil
print(fruits)
fruits.clear()#tüm elemanlar silinir.