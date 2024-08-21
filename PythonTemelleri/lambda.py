# def square(number):
#     return number**2
square=lambda num:num **2


# result=square(2)
# print(result)

numbers=[1,3,5,7,9,10,4]
# result=list(map(square,numbers))#her değeri fonk. içine tek tek gönderir
#her bir tanesi square metodunda işlem gördükten sonra return edilir
# result=list(map(lambda num:num**2,numbers))
# result=list(map(square,numbers))
result=square(3)
print(result)

# for item in map(square,numbers):
#     print(item)
# print(result)
#map:dizi elemanlarını fonksiyona tek tek göndermek

# def chec_even(num): return num%2==0
check_even=lambda num:num%2==0
#result=list(filter(chec_even,numbers))
# result=list(filter(lambda num:num%2==0,numbers))
result=list(filter(check_even,numbers))
result=check_even(numbers[2])#Tek olduğu için FALSE döner
print(result)