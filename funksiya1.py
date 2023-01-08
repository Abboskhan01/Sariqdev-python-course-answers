# Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.
# Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.
# Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.
# Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing. Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
# Foydalanuvchidan x va y sonlarini olib, ni konsolga chiqaruvchi funksiya yozing.
# Yuqoridagi funksiyada y uchun 2 standart qiymatini bering.
# Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya yozing. Natijalarni konsolga chiqaring.


# Answers


def born(year=2022):
    name = input('enter your name here >>>')
    age = input('enter your age here >>>')
    wasborn = year - int(age)
    print(f"{name} you was born {wasborn}")


born()


def calculate():
    number = float(input('enter your number here >>> '))
    print(f"{number} ning kvadrati {number ** 2} ga teng")
    print(f"{number} ning kubi {number ** 3} ga teng")


calculate()
#

def toq_juft():
    number = float(input('enter your number here >>> '))
    if number//2 == 0:
        print(f"{number} just son")
    else:
        print(f"{number} toq son")

toq_juft()


def daraja():
    x = float(input('enter your x here >>> '))
    y = float(input('enter your y here >>> '))
    print(f"{x}ning {y}darajasi {x**y}ga teng")

daraja()


def a(x, y=2):
    print(f"{x}ning {y}darajasi {x**y}ga teng")

a(2)

def qoldiq(x):
    for k in range(2,10):
        print(f"{x}ni {k}ga bolganda qoldiq={x%k}")
qoldiq(100)