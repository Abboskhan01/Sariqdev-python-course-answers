# talaba_0 = {
#     'ism':'alijon',
#     'familiya':'shamshiyev',
#     'yosh':22,
#     'fakultet':'matematika',
#     'kurs':4
#     }
#
# print(talaba_0.items())

# for kalit, qiymat in talaba_0.items():
#     print(f"Kalit: {kalit}")
#     print(f"Qiymat: {qiymat} \n")

# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
#     }
#
# for k, q in telefonlar.items():
#     print(f"{k.title()}ning telefoni {q}")


# mahsulotlar = { # Do'kondagi mahsulotlar
#     'olma':10000,
#     'anor':20000,
#     'uzum':40000,
#     'anjir':25000,
#     'shaftoli':30000
#     }
#
# print(mahsulotlar.keys())


# print('Do\'kondagi mahsulotlar:')
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot.title())
#
# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos, do'koningizga {buyum} ham olib keling")


# Homework
# Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing.
# Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring.

# Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug' \
# 'atdagi davlatlarni, keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring.

#
# Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini konsolga chiqaring.' \
#  Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring
#
# Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting).
# Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. Foydalanuvchi kiritgan taomlarni menu bilan solishtiring,
# agar taom menuda bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q" degan xabarni chiqaring

# Answers
# python_lugat = {'dict':'dictionary', 'title':'bosh harfni katta qiladi', 'sorted':'sortlab beradi alifbo boyicha' }
# for k, q in python_lugat.items():
#     print(f"{k} - {q}")


country_capital = {'USA' : 'Washington DC', 'Uzbekistan': 'Tashkent', 'Spain' : 'Madrid'}
print('Dunyo davlatlari : ')
for k in sorted(country_capital.keys()):
    print(k)

print('Dunyo davlatlari poytaxtlari : ')
for q in sorted(country_capital.values()):
    print(q)

country_capital = country_capital.keys()
countrys = []
for k in country_capital:
    countrys.append(k)
country = input('Istalgan davlat nomini kiriting : ')
country = country_capital.get(country.lower())