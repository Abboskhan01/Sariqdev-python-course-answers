# yosh = int(input('Yoshingiz nechida? '))
# if yosh <= 4:
#     print('Sizga kirish bepul.')
# elif yosh <= 12:
#     print('Sizga kirish 5000 so\'m')
# else:
#     print('Sizga kirish 10000 so\'m')
#
# yosh = int(input('Yoshingiz nechida? '))
# if yosh <= 4:
#     price = 0
# elif yosh <= 12:
#     price = 5000
# else:
#     price = 10000
#
# print(f"Sizga kirish {price} so'm")
#
# yosh = int(input('Yoshingiz nechida? '))
# if yosh <= 4:  # yosh bolalarga bepul
#     price = 0
# elif yosh <= 12:  # 4 dan 12 yoshgacha 5000 so'm
#     price = 5000
# elif yosh < 65:  # 12 dan katta va 65 dan kichiklarga narh 10000 so'm
#     price = 10000
# else:  # qariyalarga esa 8000 so'm
#     price = 8000
# print(f"Sizga kirish {price} so'm")
#
# kun = input("Bugun nima kun?")
# harorat = float(input("Havo harorati qanday?"))
# if kun.lower() == 'yakshanba' and harorat >= 30:
#     print("Cho'milgani ketdik!")
# elif kun.lower() == 'yakshanba' and harorat < 30:
#     print("Uyda dam olamiz!")
#
# kun = input("Bugun nima kun?")
# harorat = float(input("Havo harorati qanday?"))
# if (kun.lower() == 'shanba' or kun.lower() == 'yakshanba') and harorat >= 30:
#     print("Cho'milgani ketdik!")
# elif (kun.lower() == 'shanba' or kun.lower() == 'yakshanba') and harorat < 30:
#     print("Uyda dam olamiz!")
#
# narh = 15000  # mijoz 15000 so'mga taom oldi.
# choy = True  # mijoz choy ham oldi
# salat = False  # mijoz salat olmadi
#
# if choy and salat:  # agar mijoz choy ham salat ham olgan bo'lsa
#     narh = narh + 10000  # narhga 10000 so'm qo'shamiz
# elif choy or salat:  # agar choy yoki salat olgan bo'lsa
#     narh = narh + 5000  # narhga 5000 so'm qo'shamiz
#
# print(f"Jami {narh} so'm")  # yakuniy narhni chiqaramiz
#
# narh = 15000  # mijoz 15 so'mga ovqat oldi
# choy = True
# salat = False
# non = True
# kompot = True
# assorti = False
# # Quyidagi har bir shart alohida tekshiriladi va bir-biriga bog'liq emas
# if choy:  # agar choy olsa
#     print("Mijoz choy oldi.")
#     narh = narh + 3000
# if salat:  # agar salat olsa
#     print("Mijoz salat oldi.")
#     narh = narh + 5000
# if non:  # agar non olsa
#     print("Mijoz non oldi.")
#     narh = narh + 2000
# if kompot:  # agar kompot olsa
#     print("Mijoz kompot oldi.")
#     narh = narh + 5000
# if assorti:  # agar assorti olsa
#     print("Mijoz assorti oldi.")
#     narh = narh + 15000
#
# print(f"Jami {narh} so'm")
#
# # AMALIYOT
# # Quyidagi dasturlarni alohida fayllarga yozing va bajaring:
# # Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.
# #
# # Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
# # Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
# # Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
# # Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm
# # Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring
# #
# # mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
# #
# # Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga, do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing.  Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.
# #
# # foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.
# #
# # Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring.

number = int(input('Enter a even number'))
if number % 2 == 0:
    print('Thank you')
else:
    print('It\'s not a even nuber')

age = int(input('How old are you'))
if age < 4 or age > 60:
    price = 0
elif age < 18 :
    price = 10000
else:
    price = 20000
print(f"You have to pay {price} so'm")

print('Enter two numbers')
num1 = float(input('Enter number 1 :'))
num2 = float(input('Enter number 2 :'))
if num1 > num2:
    print(f"{num1} > {num2}")
else:
    print(f"{num1} < {num2}")

products = ['Un', 'solt', 'sugar', 'meat', 'meal', 'loaf', 'bread', 'eggs', 'fish']
# savat = []
# print('Enter 5 products you want')
# for k in range(5):
#     savat.append(input('Enter the product'))
# for product in savat:
#     if product.lower() in products:
#         print(f"We have the {product} and you can buy")
#     else:
#         print(f"We haven't got the {product}, Sorry!")

savat = []
print('Enter 5 products you want')
for k in range(5):
    savat.append(input('Enter the product'))
bor = []
yoq = []
for product in savat:
    if product.lower() in products:
        bor.append(product)
    else:
        yoq.append(product)
if not yoq:
    print('We have got all of the products')
else:
    for product in yoq:
        print(f"We haven't got the {product}, Sorry!")



if not yoq:
    print('We have got all of the products')

logins = ['dsa','afsdfwg', 'fsdffs', 'fsdfwdgdf', 'rertewrwer']
new_login = input('enter your login')
if new_login.lower() in logins:
    print('That is not free')
else:
    print('Welcome')
numbers = range(2, 10)
num = int(input('enter butun son'))


for numb in numbers:
    if numb % num == 0:
        print(f"{num} {numb}ga qoldingsiz bo'linadi")
    else:
        print(f"{num} {numb}ga qoldiqli bo'linadi")