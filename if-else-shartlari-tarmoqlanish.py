# avtolar = ['audi','bmw','volvo','kia','hyundai']
#
# for avto in avtolar: # avtolar ichidadi har bir avto uchun ...
#     if avto == 'bmw':  # ... agar avto bmw ga teng bo'lsa ...
#         print(avto.upper()) # avto nomini hamma harflarini katta bilan yoz.
#     else: # aks holda ...
#         print(avto.title()) # avto nomini faqat birinchi harfini katta bilann yoz.
#
# ism = input('Ismingiz nima?\n>>>') # Foydalanuvchi ismini so'raymiz
# if ism.lower() != 'ali': # Agar ism Aliga teng bo'lmasa ...
#     print(f"Uzr, {ism.title()} biz Alini kutayapmiz.") # quyidagi xabar chiqadi
# else:
#     print("Salom, Ali")
#
# javob = float(input("12x6 nechiga teng?>>>"))
# if javob!=72:
#     print("Javob xato!")
#
# yosh = int(input("Yoshingiz nechida?>>>"))
# if yosh>=18: # yosh 18 dan katta yoki teng bo'lsa
#     print('Xush kelibsiz!')
# else: # ask holda
#     print('Kirish mumkin emas!')
#
# login = input("Yangi login tanlang:")
# if len(login)<=5: # login uzunligini tekshiramiz
#     print("Login 5 harfdan ko'proq bo'lishi shart!")
#
# yil = int(input("Tug'ilgan yilingizni kiriting:"))
# if 2020-yil<18: # foydalanuvchining yoshini hisoblaymiz
#     print(f"Yoshingiz {2020-yil}da ekan.")
#     print("Kirish mumkin emas!")
# else:
#     print("Xush kelibsiz!")
#
# yosh = int(input("Yoshingiz nechida?>>>"))
# if yosh>65: print("Siz COVID-19 risk guruhida ekansiz")
#
# x, y = 25, 50 # x=25 va y=50
# print("x>y") if x>y else print("x<y")

# AMALIYOT
# Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.
#
# Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.
# Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!"  matnini konsolga chiqaring.
# Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
# Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring.
# Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring.


cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car == 'gm':
        print(car.upper())
    else:
        print(car.title())

for car in cars:
    print(car.title()) if car != 'gm' else print(car.upper())

username = input('enter your nickname here :')
if username.lower() == 'admin':
    print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    print(f"Xush kelibsiz, {username.title()}")

print('Enter two different numbers')
num1 = float(input('Enter number 1 here:'))
num2 = float(input('Enter number 2 here:'))
if num2 == num1:
    print('You has entered the same numbers')
else:
    print('Good Morning')

number = float(input('Enter you wanted number here:'))
if number < 0:
    print('It is negative number')
else:
    print('It\'s positive number')

number = float(input('Enter you wanted positive number here:'))
if number > 0:
    print(f"{number}ning ildizi={number**0.5}")
else:
    print('enter only positive number')

