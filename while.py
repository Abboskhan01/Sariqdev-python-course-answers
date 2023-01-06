# Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. Foydalanuvchi stop
# so'zini yozishi bilan dasturni to'xtating
# Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, ' \
# '18-65 gacha 10000 so'm, 65 dan kattalarga bepul. Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin ' \
#         '\va chipta narhini chiqarsin. Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).
# Yuqoridagi dasturni turli usullarda yozib ko'ring (break, ishora, yoki shart tekshirish)
# Quyidagi dasturda bir nechta mantiqiy xatolar bor. Jumladan, xusisiy holatlarda
# tsikl abadiy qaytarilib qolmoqda. Xatolarni to'g'rilay olasizmi?


# Answers
# books = []
# quession = 'What are your favourite books? Enter here : (or stop)'
#
# while True:
#     answer = input(quession)
#     if answer == 'stop':
#         break
#     else:
#         books.append(answer)
# print(books)
#
#
# quession = "Enter your age ('exit' or 'quit')"
#
# while True:
#     customer = input(quession)
#     if customer == 'exit' or customer=='quit':
#         break
#     elif int(customer) < 7:
#         print(2000)
#     elif int(customer) < 18:
#         print(30)
#     elif int(customer) < 65:
#         print(10000)
#     else:
#         print(0)

savol = "Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat == "exit":
        break
    elif float(qiymat) < 0:
        continue  # agar foydalanuvchi manfiy son kiritsa tsiklni takrorlaymiz
    else:
        ildiz = float(qiymat) ** (0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")



