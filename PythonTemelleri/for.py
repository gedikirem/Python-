numbers=[1,2,3,4,5]

#num aslında eleman sayısı
for num in numbers:#listenin içerisinden tek tek elemanları  al num değişkeninin içerisine at her for döngüsü döndüğünde num içeriğini yaz
    print(num)

for a in numbers: 
    print('Hello')

names=['beyza','emir','mete']

for name in names:
    print(f'my name is {name}')

name='Irem Gedik'
for n in name:
    print(n)

print('\n*****************\n')
tuple = (1,2,3,4,5)
for t in tuple:
    print(t)

print('\n*****************\n')
tuple=[(1,2),(1,3),(3,5),(5,7)]

for t in tuple:
    print(t)

for a,b in tuple:
    print(a)

for a,b in tuple:
    print(a,b)

d={'k1':1,'k2':2,'k3':3}
for item in d.items():#eleman gruplarına erişmek için d.items()
    print(item)

for key,value in d.items():
    print(key,value)
