#Identity Operator : is

x=y=[1,2,3]
z=[1,2,3]

print(x==y)
print(x==z)
print(x is y)#is referansları karşılaştırır
print(x is z)

x=[1,2,3]
y=[2,4]


del x[2]
y[1]=1
y.reverse()#ters çevirir

print(x==y)
print(x is y)
print(x is not y)

#Membership Operator : in

x=['apple','banana']
print('banana' in x)#banana liste içinde var mı onu kontrol eder

name='Irem'
print('e' in name)