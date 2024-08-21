#Bankmatik Uygulaması

IremHesap={
    'ad':'Irem Gedik',
    'hesapNo':'12345678',
    'bakiye':3000,
    'ekHesap':2000
}
BeyzaHesap={
    'ad':'Beyza Gedik',
    'hesapNo':'13245678',
    'bakiye':2000,
    'ekHesap':3000
}

def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")

    if(hesap['bakiye']>=miktar):
        hesap['bakiye']-=miktar
        print('paranizi alabilirsiniz')
        bakiyeSorgula(hesap)
    else:
        toplam=hesap['bakiye'] + hesap['ekHesap']

        if(toplam>=miktar):
            ekHesapKullanimi=input('ek hesap kullanilsin mi (e/h)')

            if ekHesapKullanimi=='e':
                ekHesapKullanilacakMiktar=miktar-hesap['bakiye']
                hesap['bakiye']=0
                hesap['ekHesap']-=ekHesapKullanilacakMiktar
                print('paranizi alabilirsiniz.')
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabinizda {hesap['bakiye']} bulunmaktadir")
        else:
            print('uzgunuz bakiye yetersiz')
            bakiyeSorgula(hesap)


def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır .Ek hesap limitinz ise {hesap['ekHesap']} TL bulunmkatadır.")
    

paraCek(IremHesap,3000)
bakiyeSorgula(IremHesap)
print('*'*50)
paraCek(IremHesap,2000)
bakiyeSorgula(IremHesap)