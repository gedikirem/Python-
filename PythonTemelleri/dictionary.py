#key-value şeklinde çalışan liste tipi

#41=> kocaeli 34=>istanbul
# sehirler=['kocaeli','istanbul']
# plakalar=[41,34]

# print(plakalar[sehirler.index('kocaeli')])
# print(plakalar[sehirler.index('istanbul')])

#print(plakalar['istanbul']) => 34
#print(plakalar['kocaeli]) => 41

# plakalar={'kocaeli':41,'istanbul':34}
# print(plakalar['kocaeli'])
# print(plakalar['istanbul'])

# plakalar['ankara']=6
# plakalar['kocaeli']='new value'
# print(plakalar)

users={
    'iremgedik':{
        'age':20,
        'roles':['user'],
        'email':'deneme@gmail.com',
        'adres':'adana',
        'phone':123456
    },
    'beyzanurgedik':{
        'age':18,
        'roles':['admin','user'],
        'email':'deneme2@gmail.com',
        'adres':'adana',
        'phone':78910
    }
   
}
print(users['beyzanurgedik']['roles'][0])
#r print(users['beyzanurgedik']['age'])
# print(users['beyzanurgedik']['email'])
# print(users['beyzanurgedik']['adres'])
# print(users['beyzanurgedik']['phone'])