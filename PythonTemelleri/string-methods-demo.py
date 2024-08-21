website="http://www.iremgedik.com"
course="Python Kursu:Baştan Sona Python Programlama Rehberiniz(40 saat)"

#1-' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin
# result=' Hello World '.strip()
# result=' Hello World '.lstrip()#soldan silme
# result=' Hello World '.rstrip()#sağdan silme
# result=website.lstrip('/:pth')#/,:,p,t,h karakterlerini siler

# print(result)


#2-'www.iremgedik.com' içindeki iremgedik bilgisi haricindeki her karakteri silin
# result='www.iremgedik.com'.strip('w.moc')
# print(result)

#3-'course' karakter dizisinin tüm karakterlerini küçük harf yapın
# result=course.lower()
# result=course.upper()
# result=course.title()#Her kelimenin baş harfi

#4-'website' içinde kaç tane a karakteri vardır?(count('a))
# result=website.count('e')
# result=website.count('www')
# result=website.count('www',0,10)#0 ile 10 arasında www karakteri kaç defa var

# print(result)

#5-'website' www" ile başlayıp com ile bitiyor mu?
# result=website.startswith('www')
# result=website.startswith('http')
# result=website.endswith('com')
# print(result)

#6-'website' içinde '.com' ifadesi var mı?
result=website.find('com')#bulduğu com ifadesinin indeks numarasını döndürdü
result=website.find('com',0,10)#bu aralıkta bulamadı
result=course.find('Python')
result=course.rfind('Python')

result=website.index('com')
result=website.rindex('com')
#result=website.rindex('comm')#Hata verir o eleman bulunmadığı için.Find ile arasındaki fark bu find -1 verir
#exception
#print(result)

#7-'course' içindeki karakterlerin hepsi alfabetik mi?(isalpha,isdigit)
result=course.isalpha()
result='Hello'.isalpha()
result=course.isdigit()#harf var mı
result='123'.isdigit()


#8-'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ soluna * ekleyiniz

result='Contents'.center(50,'*')
result='Contests'.ljust(50,'*')
result='Contests'.rjust(50,'*')
#9-'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin
result=course.replace(' ','-',5)#sadece 5 karakteri değiştirmiş oldu
result=course.replace(' ','')#boşuk karakterlerini sil

#10-'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin
result='Hello World'.replace('World','There')

#11-'course' karakter dizisini boşluk karakterlerden ayırıın
result=course.split(' ')
result=result[2]
print(result)