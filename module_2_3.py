my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while index < len(my_list):
    a = my_list[index]
    index += 1
    if a == 0:
        continue
    elif a < 0:
        break
    print(a)
    