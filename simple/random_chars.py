import random

"""
生成随机字符串，至少包含一个大写/小写/数字
"""
char_set = "abcdefghijklmnopqrstuvwxyz"
upper_char_set = char_set.upper()
pw_len = 8
pwlist = []

for i in range(pw_len//3):
    pwlist.append(char_set[random.randrange(len(char_set))])
    pwlist.append(upper_char_set[random.randrange(len(upper_char_set))])
    pwlist.append(str(random.randrange(10)))

for i in range(pw_len- len(pwlist)):
    pwlist.append(char_set[random.randrange(len(char_set))])

print("".join(pwlist))
random.shuffle(pwlist)
pwstr = "".join(pwlist)

print(pwstr)