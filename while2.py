# Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.
# e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing. Foydalanuvchidan'
# lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.
# Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni' \
#  e-bozordagi mahsulotlar bilan solishitiring (tayyor ro'yxat ishlatishingiz mumkin). Agar mahsuot e-bozorda mavjud' \
#          bo'lsa mahuslot narhini chiqaring, aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating.


# Answers


# orders = []
#
# while True:
#     order = input('enter your order here for stop enter stop')
#     if order == 'stop':
#         break
#     else:
#         orders.append(order)
# print(orders)
#

e_bozor = {}

while True:
    product = input('enter product name here')
    price = input('enter price of the product here >>>')
    answer = input('will add new product or stop')
    if answer == 'stop':
        break
    else:
        e_bozor[product] = float(price)


while True:
    order = input('enter your order here for stop enter stop')
    if not order == 'stop':
        if order in e_bozor.keys():
            print(f"{order}' cost={e_bozor[order]}")
        else:
            print(f"{order} not exist in our market")
    else:
        break

