# val1 = {1: "one", 2: "two", 3: "three"}
# val2 = {4: "four", 5: "five"}



val1 = dict([input('Введите ключ и значение через пробел, для первого словаря:').split() for _ in range(3)])
print(val1)

val2 = dict([input('Введите ключ и значение через пробел, для второго словаря:').split() for _ in range(3)])
print(val2)

val1.update(val2)
print('Объединение двух словарей: ',  val1)

