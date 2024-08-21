list=[1,2,3]

tuple=(1,'iki',3)

# print(type(list))
# print(type(tuple))

# print(list[2])
# print(tuple[2])

# print(len(list))
# print(len(tuple))

list=['ali','veli']#önceki içeriği sil farklı içerikler ekle
tuple=('damla','ayse','ayse')
names=('demet','emel','ayse')+tuple

print(names)
list[0]='ahmet'
#Tuple da elemanlar atandıktan sonra hehangi bir elemanını değiştiremiyoruz
#tuple[0]='deniz' hata verir


print(tuple.count('ayse'))
print(tuple.index('ayse'))#ayse ilk nerde var oluyor onu döndürür
print(list)
print(tuple)