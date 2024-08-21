#global x
x='global x'

def function():
    # local scope
    x='Local x'
    #burda tanımladığımız değişkenler dışarıdakileri etkilemiyor
    print(x)

function()
print(x)
#######################
name='Irem'

def changeName(new_name):
    name=new_name
    print(name)

changeName('Beyza')
print(name)

##########################

name='global string'

def greeting():
    name='Irem'

    def helllo():
        print('hello '+name)
    
    helllo()

greeting()
print(name)

##################################

x=50

def test():
    global x
    print(f'x : {x}')

    x=100
    print(f'changed x to {x} ')

test()