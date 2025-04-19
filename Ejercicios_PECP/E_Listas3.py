my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
no_repeat = []

for i in my_list:
    if i not in no_repeat:
        no_repeat.append(i)
print(no_repeat)

my_list = [[0, 1, 2, 3] for i in range(2)]
print(my_list[2][0])

















