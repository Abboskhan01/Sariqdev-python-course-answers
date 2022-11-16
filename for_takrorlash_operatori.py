mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
for mehmon in mehmonlar:
    print(mehmon)


mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
for mehmon in mehmonlar:
    print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
    print("Hurmat bilan, Palonchiyevlar oilasi")


sonlar = list(range(1,11))
for son in sonlar:
    print(f"{son} ning kvadrati {son**2} ga teng")


sonlar = list(range(11)) # 1 dan 10 gacha sonlar ro'yxatini yaratamiz
sonlar_kvadrati =[] # bo'sh ro'yxat yaratamiz
for son in sonlar:  # sonlar dagi har bir son uchun
    sonlar_kvadrati.append(son**2) # uning kv.ni hisoblab, sonlar_kvadrati ga yuklaymiz

print(sonlar)
print(sonlar_kvadrati)

# dostlar = []
# print("Eng yaqin 5ta do'stingizni kiriting")
# for k in list(range(5)):
#     dostlar.append(input(f"{k+1}-dostingizni kiriting\n>>>"))
#
# print(dostlar)

# Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
# Yuoqirdagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)
#
# 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
#
# Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
# Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.


# Answers
dostlar = ['Abbos', 'Ilhom', "Xurshid", "Asad", "Xoji"]
d = 0
for dost in dostlar:
    print(f"{dost} tuzumisan ishlarin yaxshimi")
    d += 1
print(f"Kod {len(dostlar)} marta takrorlandi")
print("Kod", d, "marta takrorlandi")

tub_sonlar = list(range(11,100, 2))
# print(tub_sonlar)
for tub in tub_sonlar:
    print(f"{tub}ning kubi {tub**3}ga teng")

customers = []
count = input('How many customers Have you met\n>>>')
for k in range(int(count)):
    customers.append(input(f"enter {k+1}-cutomers's name"))

print(customers)