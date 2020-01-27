# # 1 задача
# import re
#
# surname = input('Введите фамилию: ')
# if 0>len(surname)>1000:
#     print('Напишите строку поменьше')
# elif re.search('\d+', surname):
#     print(surname)
# else:
#     print(surname.title())



# # 2 задача
# charact = "google.com"
# ts1 = {}
#
# for i in charact:
#     if i in ts1:
#         ts1[i] += 1
#     else:
#         ts1[i] = 1
#
# print("Количество букв использ в слове \n" + str(ts1))


# # 3 задача
# str = input('Введите строку: ')
#
# if len(str) < 2:
#     print()
# else:
#     res = str[:2] + str[-2:]
#     print(res)

# # 4 задача
# li = [input('Введите строку больше 2: ') for _ in range(4)]
# print(len([x for x in li if len(x)>=2 and x[0] == x[-1]]))

# # 5 задача
#
# set1 = [1, 2]
#
# set2 = [2, 3]
#
# set3 = [5]
#
#
# print("Set1: " + str(set1))
#
# print("Set2: " + str(set2))
#
# print("Set3: " + str(set3))
#
# res = 0
#
# if ((set(set1) & set(set2)) == set(set3)):
#     res = 1
#
# if (res):
#
#     print("Является подмножеством")
#
# else:
#
#     print("Не является подмножеством")
#


# # 8 задача
# dic = {'a':7600, 'b':2374, 'c':1111,'d':2222, 'e':5454, 'f': 657}
# res = sorted(dic, key=dic.get, reverse=True)[:3]
# for val in res:
#     print(val, ":", dic.get(val))


# #  9 задача
# i = [1, 1, 2, 3, 5, 6, 7, 7, 3, 5]
# print(list(set(i)))


# # 10 задача
# list1 = [1, 2, 3, 4, 5]
# list2 = [2, 3, 5]
# list3=list(set(list1)-set(list2))
# print(list3)