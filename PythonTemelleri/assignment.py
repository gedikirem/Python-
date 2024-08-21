#atama operatörleri

x=5
y=10
z=20

x,y,z=5,11,20
#x,y=y,x
x+=5#x=x+5
x-=5#x=x-5
x*=5#x=x*5
x/=5#x=x/5
x%=5#x=x%5
y//=5#x=x//5
y**=5

#print(x,y,z)

values=1,2,3,4,5#tuple
print(values)
print(type(values))

#x,y,z=values
x,y,*z=values
print(x,y,z)#z elemanını dizi şeklinde oluşturur
print(x,y,z[0])