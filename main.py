list1 = [1, 2, 3, 4, 5, 6]
list2 = [1, 2, 3]
min_len = len(list1) if len(list1) < len(list2) else len(list2)
max_list = list1 if len(list1) > len(list2) else list2
newlist = [0] * min_len

for i in range(min_len):
    newlist[i] = list1[i] + list2[i]

newlist.extend(max_list[-(len(max_list) - min_len):])

print(newlist)