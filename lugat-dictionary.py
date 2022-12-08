# Homework
# otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta m'alumot
# kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring
# :Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan Oila a'zolaringizning sevimli taomlari
# lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin. Kamida uch kishining sevimli taomini konsolga
# chiqaring: Alining sevimli taomi osh Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (
# atamani) kiriting (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.
# Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering. Agar
# so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring. Yuqoridagi vazifani if-else
# yordamida qiling va natijani ham foydalanuvchiga tushunarli ko'rinishda chiqaring.

# Answers
# 1
father = dict(name='minavarjon', age='45', born='yangiqo\'rg\'on')
mother = dict(name='mother', age='40', born="Yangiqo'rg'on")
brother = dict(name='Og\'abek', age='20', born="Yangiqo'rg'on")
print(f"My father's name is {father['name'].title()} {father['age']} years old and was born in {father['born'].upper()}.")
print(f"My mother's name is {mother['name'].title()} {mother['age']} years old and was born in {mother['born'].upper()}.")
print(f"My father's name is {brother['name'].title()} {brother['age']} years old and was born in {brother['born'].upper()}.")
# 2
favourite_foods = dict(father='palov', mother='mastava', brother='shashlik')
print(f"My father'r favourite food is {favourite_foods['father']}")
print(f"My mother'r favourite food is {favourite_foods['mother']}")
print(f"My brother'r favourite food is {favourite_foods['brother']}")
# 3
python_book = dict(integer='Butun son', float='O\'nlik son', upper='Marnning hamasini katta harf qiladi')
key_word = input('Enter a key word there >>>')
print(python_book.get(key_word.lower(), 'Bunday so\'z mavjud emas'))
if key_word.lower() in python_book:
    print(f"{key_word}ning tarjimasi - {python_book[key_word]}")
else:
    print('Bunday so\'z mavjud emas')