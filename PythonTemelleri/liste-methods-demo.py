names=['Ali','Yagmur','Hakan','Deniz']
years=[1998,2000,1998,1987]

#1-"Cenk" ismini listenin sonuna ekleyiniz
# names.append('Cenk')
# print(names)
#2-"Sena" değerini listenin başına ekleyin
# names.insert(0,'Sena')
# print(names)
#en sona eklemek içinse:
#names.insert(len(names),'Mehmet')
#3-"Deniz" ismini listeden silin
#names.remove('Deniz)
# names.pop()
#names.pop(1)
# print(names)
#4-"Deniz" isminin indeksi nedir
print(names.index('Deniz'))
#5-"Ali" listenin bir elemanı mıdır
result='Ali' in names
print(result)#True döndürür
print(names.count('Ali'))
#6-Liste elemanlarını ters çevirin
names.reverse()
print(names )
#7-Liste elemanlarını alfabetik olarak sıralayınız
names.sort()
print(names)
#8-years listesini rakamsal büyüklüğe göre sıralayınız
years.sort()
print(years)
#9-str="Chevrolet,Dacia" karakter dizisini listeye çeviriniz
str="Chevrolet,Dacia"
result=str.split(',')
print(result)
#10-years dizisinin en büyük ve ne küçük elemanı nedir
years.sort()
print(years[0])#en küçük
print(years[-1])#en büyük

min=min(years)
max=max(years)
print(min)
print(max)
#11-years dizisinde kaç tane 1998 değeri vardır
print(years.count(1998))
#12-years dizisinin tüm elemanlarını siliniz
years.clear()
print(years)
#13-Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız
marka=[]
x=input('x marka bilgisi girin:')
marka.append(x)
y=input('y marka bilgisi girin:')
marka.append(y)
z=input('z marka bilgisi girin:')
marka.append(z)
print(marka)
