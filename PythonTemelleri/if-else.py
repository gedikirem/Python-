#Koşuldan gelecek mutlaka bir true - false değeri olması gerek
if 3>2:
    print('Hoş Geldin')

username='iremgedik'
password='1234'

girilenUsername=input('Username giriniz: ')
girilenPassword=input('Sifre giriniz: ')


# isLoggedin=(username==girilenUsername) and (password==girilenPassword)

# if isLoggedin== True:
#     print('Hoş geldiniz')
# else:
#     print('Username veya Password bilgisi yanlis tekrar deneyiniz')

if(girilenUsername==username):
    if(girilenPassword==password):
        print('Hoş Geldiniz')
    else:
        print('Parola Bilgisi Yanlis')
else:
    print('Username Yanlis')