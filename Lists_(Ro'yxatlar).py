mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
narhlar = [12000, 18000, 10900, 22000] # narhlar ro'yxati (sonlar)
sonlar = ['bir', 'ikki', 3, 4, 5] # sonlar va matnlar aralash ro'yxat
ismlar = [] # bo'sh ro'yxat

mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
print("Birinchi meva: ", mevalar[0])
print("Ikkinchi meva: ", mevalar[1])

mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
print("Birinchi meva: ", mevalar[0].title())
print("Ikkinchi meva: ", mevalar[1].upper())

car_models = ['Toyota', 'GM', 'Volvo', 'BMW', 'Hyundai', 'Kia', 'Volkswagen']
print(car_models[-1]) # Listning eng oxirgi elementiga -1 bilan murojat qilamiz

narhlar = [12000, 18000, 10900, 22000]
narhlar[0] = 13000 # 1-qiymatni 13000 ga o'zgartiramiz
narhlar[2] = 11000 # 3-qiymatni 11000 ga o'zgartiramiz
narhlar[3] = narhlar[3]+2000 # 4-qiymatga 2000 qo'shamiz
print(narhlar)

cars = ['Lacetti', 'Nexia 3', 'Cobalt']
cars.insert(0, 'Malibu') # 1-o'ringa yangi qiymat qo'shamiz
print(cars)

mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
del mevalar[1] # 2-element (anjir) ni o'chirib tashlaymiz
print(mevalar)

print(mevalar.index('olma'))


# Practice
# Quyidagi mashqlarni bajaring:
# ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
# Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring:
#
# sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik).
# Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring.
# t_shaxslarva z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.
# Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:
#
# friendsnomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.
# Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang.
# Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
# Yangi mehmonlardeb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.

# Answers

names = ['Otabek']
names.append('Xurshid')
names.insert(0, 'Ilhom')
names.pop(2)
names.append('Xurshid')
print(names)
print(names[0], "qachon choyxona?")
print(names[1].title(), 'bugun choyxonaga kelasanmi?')
print(f"{names[2].capitalize()} qalesan o'rto?")

numbers = []
numbers.append(10)
numbers.insert(1, 12.8)
numbers.append(-12)
numbers.insert(2, -10.5)
print(numbers)
numbers[1] = 10
numbers.pop(2)
numbers[2] = 20
print(numbers[1] + 1)
print(numbers[-1] +10)
print(numbers[0] + numbers[-1])

t_shaxslar = []
z_shaxslar = []
t_shaxslar.append('Alisher Navoiy')
z_shaxslar.insert(0, 'Elon Mask')
t_shaxslar.insert(-1, 'Amir Temur')
z_shaxslar.append('Stiv Jobs')
print(t_shaxslar)
print(z_shaxslar)
z_person = z_shaxslar.pop(1)
t_person = t_shaxslar.pop()
print(z_person)
print(t_person)


friends = []
friends.append('Ilhom')
friends.append('Asadbek')
friends.append('Otabek')
friends.append('Stiv Jobs')
friends.append('Elon Mask')
friends.append('Xurshid')
print(friends)
friends.remove(friends[3])
friends.remove('Elon Mask')
print(friends)
friends.append('Ilyos')
friends.insert(2, 'Abbos')
friends.insert(-1, 'Xoji')
print(friends)

guests = []
guests.append(friends.pop(2))
guests.append(friends.pop(1))
guests.append(friends.pop(-1))
print(guests)