"""
yeild基本用法
"""
# def simple_gen():
#     yield 'Oh'
#     yield 'hello'
#     yield 'there'
#
# for i in simple_gen():
#     print(i)


"""
不用生成器循环直至查找到CORRECT_COMBO
"""

CORRECT_COMBO = (3, 6, 1)
found_combo = False  # 使用一个标记,各层都需要判断中断的标记
for c1 in range(10):
    if found_combo:
        break
    for c2 in range(10):
        if found_combo:
            break
        for c3 in range(10):
            if (c1, c2, c3) == CORRECT_COMBO:
                print('Found the combo:{}'.format((c1, c2, c3)))
                found_combo = True
                break

"""
使用yeild生成器
"""


def combo_gen():
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                yield (c1, c2, c3)

for (c1, c2, c3) in combo_gen():
    # print(c1, c2, c3)
    if (c1, c2, c3) == CORRECT_COMBO:
        print('Found the combo:{}'.format((c1, c2, c3)))
        break
