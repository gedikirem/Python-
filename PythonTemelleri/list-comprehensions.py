for x in range(10):
    print(x)

numbers=[x for x in range(10)]#0 dan 10 a kadar olan sayıları x e attı sonra da onu numbersa
print(numbers)#dizi şeklinde yazdırdı


numbers=[]
for x in range (10):
    numbers.append(x)

print(numbers)


for x in range(10):
    print(x**2)

numbers=[x**2 for x in range(10)]
print(numbers)

numbers=[x*x for x in range(10) if x%3==0]
print(numbers)

myString='Hello'
myList=[]

for letter in myString:
    myList.append(letter)

print(myList)

myList=[letter for letter in myString]
print(myList)

years=[1983,1999,2008,1956,1986]
ages=[2019-year for year in years]
print(ages)

result=[x if x%2==0 else 'TEK' for x in range(1,10)]#Dögüden sonra istediğimiz her işlemi yaptırabiliriz
print(result)

result=[]

for x in range(3):
    for y in range(3):
        result.append((x,y))

print(result)

numbers=[(x,y) for x in range(3) for y in range(3)]
print(numbers)
