print('Hello World!')
print('Hello \tWorld!')
print('Hello \nWorld!')
print('Abb\tos')
ism = 'Ahad'
familiya = 'Qayum'
ism_sharif = f"{ism} {familiya}"
print(ism_sharif.upper())

ism = 'Ahad'
familiya = 'Qayum'
ism_sharif = f"{ism} {familiya}"
print(ism_sharif.lower())

ism_sharif = 'james bond'
print(ism_sharif.capitalize())

meva = "     olma     "
print("Men " + meva.lstrip() + " yaxshi ko'raman")
print("Men " + meva.rstrip() + " yaxshi ko'raman")
print("Men " + meva.strip() + " yaxshi ko'raman")
print("Men " + meva + " yaxshi ko'raman")
ism = input("Ismingiz nima?")
print("Assalom alaykum, " + ism)
ism = input("Ismingiz nima?\n>>>") # Foydalanuvchi ismini yangi qatordan kiritadi
print("Assalom alaykum, " + ism.title())


# AMALIYOT
# Quyidagi mashqlarni bajaring:
# Quyidagi o'zgaruvchilarni yarating:
# kocha="Bog'bon"
# mahalla="Sog'bon"
# tuman="Bodomzor"
# viloyat="Samarqand"
# Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
# Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati
# Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat) qiymatini foydalanuvchidan so'rang. Va avvalgi mashqni takrorlang.
# Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing
# Yuqoridagi matnni f-string yordamida, yangi, manzil deb nomlangan o'zgaruvchiga yuklang
# manzilga biz yuqorida o'rgangan title(), upper(), lower() , capitalize() metodlarini qo'llab ko'ring.


# Answers

kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor"
viloyat="Samarqand"
# Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati
result = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
print(result)
print("Assalom Alekum savollarga javob bering")
kocha = input('Iltimos kochangizni nomini kiriring!\n>>>')
mahalla = input('Iltimos mahallangiz nomini kiriring!\n>>>')
tuman = input('Iltimos tumaningiz nomini kiriring!\n>>>')
viloyat = input('Iltimos viloyatingiz nomini kiriring!\n>>>')
result = f"{kocha.lower()} ko'chasi,\n{mahalla.title()} mahallasi, \n{tuman.capitalize()} tumani, \n{viloyat.upper()} viloyati."
print(result)
