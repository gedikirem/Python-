numbers=[1,10,5,16,4,9,10]
letters=['a','g','s','b','y','a','s']

""" val=min(numbers)
val1=max(numbers)
val2=max(letters)
val3=min(letters)
print(val)
print(val1)
print(val2)
print(val3) """

# val=numbers[3:6]
# print(val)
# val=numbers[:3]#0 dan 3 e
# print(val)
# val=numbers[4:]#4 ten sona
# print(val)

#istediğimiz indisteki elemanı değiştirme
# numbers[4]=40
# print(numbers)

# numbers.append(49)#49 u en sona eklenir
# print(numbers)

#istediğimiz konuma eleman ekleme insert metoduyla
# numbers.insert(3,78)#3.indise 78 rakamını ekler
# print(numbers)
# numbers.insert(-1,52)#listenin en sonundan bir önceki yere 52 yi ekler
# print(numbers)

#eleman silmek için pop() methodu
# numbers.pop()
# numbers.pop(0)#0. indisteki eleman silinir
# numbers.pop(-1)#en sondaki elemanı siler
# print(numbers)

#silmek istediğimiz karakteri verdiğimiz method
numbers.remove(4)
print(numbers)

#Listeyi sıralı yazdırmak için
numbers.sort()
numbers.reverse()#listeyi ters çevir

letters.sort()
letters.reverse()

print(numbers)
print(letters)

print(len(numbers))#eleman sayısı 
print(len(letters))

print(numbers.count(10))#istediğimiz elemanı sayabiliriz
print(letters.count('a'))

numbers.clear()#eleman temizler
print(numbers)

