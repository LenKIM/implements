import collections

input = "two times three is not four"

dic = {}

for w in input.split(' '):
    if w in dic:
        w_ = dic[w]
        dic[w] = w_ + 1
    else:
        dic[w] = 1

print(dic)

aa = "two times two is four"
#
for w in aa.split(' '):
    if w not in dic:
        print("No")
        exit()
    else:
        value = dic[w] - 1
        if value <= 0:
            dic.pop(w)
        else:
            dic[w] = value

print("Yes")
