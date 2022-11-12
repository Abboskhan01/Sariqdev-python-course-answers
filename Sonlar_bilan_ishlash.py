# a = 'Abbos'
# b = 'A   b  b  o  s'
# print(len(a))
# print(len(b))
a = 20  # Sonlar musbat yoko
b = -30 # manfiy bo'lishi mumkin
c = a + b
print(c)
# Kvadratning yuzini hisoblaymiz
kvdrt_tmni = 20 # Kavdratning tomoni 20 ga teng
kvdrt_yuzi = kvdrt_tmni**2 # Kvadrat yuzini hisoblaymiz
print(kvdrt_yuzi)

a = -20
b = 40
c = b/a
print(c) # natija o'nlik son bo'ladi

a = 2
b = 3.0
# Quyidagi arifmetik amallarning natijasi o'nlik son hosil qiladi
print(a+b)
print(a*b)
print(a**b)
print(2*(a+b))

aholi_soni = 7_594_000_000 # o'zmizga qulay bo'lishi uchun shinday yozdik
print("Yer kurrasida", aholi_soni, " ga yaqin odam yashaydi")

x, y, z = 10, -7.95, -30
print(x, end=',')
print(y)
print(z)
print(float(x))
print(int(y))
print(str(z))
x = float(x)

ism = 'Jobir'
yosh = 36
print(type(ism))  # ism degan o'zgaruvchining turini konsolga chiqaramiz
print(type(yosh)) # ismyosh degan o'zgaruvchining turini konsolga chiqaramiz
print(type(x))

# Practice
# Quyidagi dasturlarning har birini alohida fayl ko'rinishida yozing va bajaring:
# Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur
#
# Foydalanuvchining yoshini so'rab, uning tug'ilgan yilini hisoblab, konsolga chiqaruvchi dastur
#
# Foydalanuvchidan ikki son kiritshni so'rab, kiritilgan sonlarning yig'indisi, ayirmasi, ko'paytmasi va bo'linmasini chiqaruvchi dastur

# Answers

number = input('Enter any number \n>>>')
result1 = f"{number}sonning kvadrati {float(number)**2} ga teng"
result2 = f"{number}sonning kubi {float(number)**3} ga teng"
print(result1)
print(result2)
age = int(input('Enter your age \n>>>'))
now_year = 2022
born = now_year - age
print('Yoy was born in', born)

print('Please enter two number')
number1 = float(input('enter here number 1 :'))
number2 = float(input('enter here number 2 :'))
qosh = number1 + number2
ayr = number1 - number2
ayr1 = number2 - number1
kop = number2 * number1
bol = number2 / number1
bol1 = number1 / number2
print('Added two numbers = ', qosh)
print('first number - second number = ', ayr)
print('second number - first number = ', ayr1)
print('aggrandizement', kop)
print('bo\'lish', bol)
print("bo'lish 1 ", bol1)