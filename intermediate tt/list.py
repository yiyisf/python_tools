import datetime

# print(datetime.datetime.now())
# xyz = (i for i in range(50000000))
# print(list(xyz)[:5])
# print(datetime.datetime.now())
# xyz = [i for i in range(50000000)]
# print(xyz[:5])
# print(datetime.datetime.now())

# 查出列表中5的倍数
input_list = [5, 6, 2, 1, 6, 7, 10, 12]


def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False


xyz = (i for i in input_list if div_by_five(i))
print(list(xyz))
