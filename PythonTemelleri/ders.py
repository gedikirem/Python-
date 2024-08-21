#Döngüler
#1-"Merhaba Dunya" stringini bir değişkene atayan ve ekrana yazdıran
#a)Yazdırdığınız değerin içerisindeki 'b' harfinin konumunu bulan
#b)Yukarıdaki stringin bütün harflerini büyük ve küçük olarak ekrana yazdırın
#c)Yukarıdaki string içerisindeki istediğiniz bir harfi kullanarak bunu parçalayın

x="Merhaba Dunya"
print(x)
print(x[5])
x=x.upper()
print(x)
x=x.lower()
print(x)
x=x.split('a')
print(x)


#2-İki değişken tanımlayın ve bunlara birer değer atayarak boolean oparatörü ile karşılaştırma yapın
#Sonuçlar true false olmalıdır

degisken=5
degisken1=10
print(bool(degisken==degisken1))

#liste=[1,'a',2,3,True,4,5,'True','1'] verilen listeyi kullanarak 
#a)Listenin son elemanını bulun
#b)Yeni bir liste oluşturun ve yukarıdaki listenin ikinci ve üçüncü elemanlarını içerisine atın
#c)Listeyi ters sıralayın

liste=[1,'a',2,3,True,4,5,'True','1'] 
print(liste[8])
yeniListe=liste[2:4]
print(yeniListe)
print(liste)
print(liste[::-1])

#4-ic_ice_liste=[1,2,3,[4,5]] listeyi kullanarak 
#a)Listedeki 5 değerini ekrana yazdırın
#b)Listenin son elemanını listeden atın ve yerine yeni bir eleman ekleyin
#c)Pop komutunu kullanmayarak listede bulunan '3' karakterini silin

ic_ice_liste=[1,2,3,[4,5]]
print(ic_ice_liste[3][1])
liste.pop()
print(ic_ice_liste[:-1])
print(ic_ice_liste)


