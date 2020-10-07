my_list = [13,14,15,16,25,26,28,33,36,223,221,258,299,356,339]


# result = list(filter(lambda x: (x % 13 == 0), my_list))
#
# print(result)

result = []

for i in range(len(my_list)):

    if my_list[i] % 13 == 0:
        result.append(my_list[i])

print(result)