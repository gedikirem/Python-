#value types=> string,number
#verinin kendisiyle ilgileniyoruz
x=5
y=25

x=y
y=10

print(x,y)
#reference types=>list,class
#herhangi bir liste üzerinde yaptığımız değişiklik  aynı adresi gösteren 2 tane objede otomatik olarak yapılır
a=["apple","banana"]
b=["apple","banana"]

a=b#adresler birbirine eşitleniyor
b[0]="grape"
print(a,b)