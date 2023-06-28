# # x,y,z = 5,16,20
# # x,y = y,x
# # x = x+5

# # x+=5
# # x-=5
# # x*=5
# # x/=5
# # x%=5
# # y//=5
# # y**=z
# # # print(x,y,z)


# values = 1,2,3,4,5

# print(values)
# print(type(values))

# x,y,*z = values

# print(x,y,z[0])


# !  Karşılaştırma  Operatörleri
# usernamei password => databese

# 'sadikturan', '123456'

# a, b ,c,d =5,5,10,4
# password='1234'
# username='sadikturan'


# result = (a==b) #True
# result = (a==c) #False
# result = ('sdktran'== username)
# result = ('sadikturan'== username)
# result = (a != b)


# ! if else
# username = 'sadikturan'
# password = '1234'



# if (username == 'sadikturan'):
#     if  (password == '1234'):
#         print('Hoşgeldiniz')
#     else:
#         print("Parola yanlış")
# else:
#     print("Kullanıcı Adı yanlış")

# x=int(input("x: "))
# y=int(input("y: "))

# if x > y:
#     print("x y den büyük")
# elif x == y:
#     print("x y eşit")

# else:
#     print("y x ten büyük")

# num = int(input("sayi: "))

# if num > 0:
#     print("sayı pozitif")
# elif num < 0:
#     print("sayı negatif")
# else:
#     print("sayı 0")


# ! For Döngüsü

# numbers = [1,2,3,4,5]

# for num in numbers:
#     # print("mert")
    

# names= ["çınar","sadık","sena"]
# for name in names:
#     # print(f"my names is {name}")


# name="mert"
# for n in name:
#     # print(n)
    
# tuple = [(1,2),(1,3),(3,5), (5,7)]

# for a,b in tuple:
#     print(a,b)

# d= {"k1":1, "k2":2, "k3":3}

# for key,value in d.items():
#     print(key,value)

# ! While Döngüsü

# x = 1

# while x <= 100:
#     if x % 2==1:   
#        print(f"sayı tek: {x}")
#     else:
#       print(f"sayı çift: {x}")
#     x= x + 1
    
# print("bitti...")

# name = ""
# while not name.strip():
#      name = input("isminizi giriniz")
     
# print(f"merhaba, {name}")

# name = "mert demircan"

# for letter in name:
#     if letter == 'm':
#         continue
#     print(letter)

# x =0
# while x<5:
#     if x == 2 :
#         continue
#     print(x)
#     x+=1

# ! Döngü Uygulaması

# import random

# sayi = random.randint(1,10)

# can = int(input("kaç hak kullanmak istersiniz: "))
# hak = can
# sayac=0


# while hak > 0:
#     hak -=1
#     sayac +=1
#     tahmin = int(input("tahmin"))
    
#     if sayi == tahmin:
#         print(f"tebrikler bildin {sayac}. defada bildin Toplam Puanınız: {100-(100/can) *(sayac-1)}")
#         break
#     elif sayi > tahmin:
#         print("yukarı")
#     else:
#         print("asağı")
#     if hak ==0:
#         print(f"hakkınız bitti. Tutulan sayı : {sayi}")    


# ! Python ile OOP