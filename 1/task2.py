# abc_2026
# Федосов Артем
#
# todo: Преобразуйте переменную age и foo в число
# age = "23"
# foo = "23abc"
#
# Преобразуйте переменную age в Boolean
# age = "123abc"
#
# Преобразуйте переменную flag в Boolean
# flag = 1
#
# Преобразуйте значение в Boolean
# str_one = "Privet"
# str_two = ""
#
# Преобразуйте значение 0 и 1 в Boolean
#
# Преобразуйте False в строку




#Преобразуйте переменную age и foo в число
import re
age = "23"
foo = "23abc"

age_num = int(age)
foo_num = int(re.match(r'\d+', foo).group())

print(age_num)
print(foo_num)


#Преобразуйте переменную age в Boolean
# age = "123abc"

age = "123abc"
age_bool = bool(age)
print(age_bool)


# Преобразуйте переменную flag в Boolean
# flag = 1
flag = 1
flag = bool(flag)
print(flag)


# Преобразуйте значение в Boolean
# str_one = "Privet"
# str_two = ""
str_one = "Privet"
str_two = ""
bool_one = bool(str_one)
bool_two = bool(str_two)
print(bool_one)
print(bool_two)


# Преобразуйте значение 0 и 1 в Boolean
znachenie_0 = bool(1)
print(znachenie_0)
znachenie_1 = bool(0)
print(znachenie_1)


# Преобразуйте False в строку
F = str(False)
