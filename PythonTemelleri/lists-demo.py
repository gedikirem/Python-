#1-"BMW",Mercedes,Opel,Mazda" elemanlarına sahip bir liste oluşturunuz
liste=['BMW','Mercedes','Opel','Mazda']
print(liste)
#2-Liste Kaç elemanlıdır?
print(len(liste))
#3-Listenin ilk ve son elemanı nedir?
print(liste[0])
print(liste[3])     
print(liste[-1])
#4-Mazda değerini Toyota ile değiştirin
liste[3] ="Toyota"
print(liste[3])
#5-Mercedes listenin bir elemanı mıdır?
result='Mercedes' in liste
print(result)
#6-Listenin -2 indeksindeki değer nedir?
print(liste[-2])
#7-Listenin ilk 3 elemanını alın
print(liste[0:3])
print(liste[:3])
print(liste[-2:])#-2 den sona kadar git
#8-Listenin  son 2 elemanı yerine "Toyota" ve "Renault" değerlerini ekleyiniz.
liste[-2:]=['Toyota','Renault']
print(liste)
#9-Listenin üzerine "Auidi" ve "Nissan" değerlerini ekleyin
result=liste + ['Auidi','Nissan']
print(result)
#10-Listenin son elemanını silin
del liste[-1]
result= liste
print(liste)
#11-Liste elemanlarını tersten yazdırınız
result=print(liste[::-1])
#12-Aşağıdaki verileri bir liste içinde saklayınız

    #studentA:Yigit bilgi 2010,(70,60,70)
    #studentB:Sena Turan 1999,(80,80,70)
    #studentC:Ahmet Turan 1998,(80,70,90)


studentA=['Yigit','bilgi', 2010,[70,60,70]]
studentB=['Sena','Turan', 1999,[80,80,70]]
studentC=['Ahmet','Turan', 1998,[80,70,90]]

result=studentA[0]
print(result)
result=studentC[3][2]
print(result)
result=f"{studentA[0]} {studentA[1]} {2023-studentA[2]} yasinda ve not ortalamasi {(studentA[3][0]+studentA[3][1]+studentA[3][2])/3}"
print(result)