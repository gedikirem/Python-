name='Irem Gedik'

for letter in name:
    if letter=='e':
        break # letter e ise döngüyü durdur ve diğer harfler ekrana yazmaz
    #continue sadece o anki döngü turunu iptal eder
    print(letter)

x=0

while x<5:
    x+=1
    if x==2:
        continue
    print(x)
