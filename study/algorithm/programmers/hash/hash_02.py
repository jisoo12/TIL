# phone_book = ["119", "97674223", "1195524421"]
# phone_book = ["123", "456", "789"]
phone_book = ["12", "123", "1235", "567", "88"]


flag = True
dict_phone_book = {}
for i in phone_book:
    dict_phone_book.update({i: True})

for number in phone_book:
    _num = ""
    for num in number:
        _num += num
        if _num in dict_phone_book and _num != number:
            flag = False

print(flag)