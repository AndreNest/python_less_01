# a = 11
# b = 11,22
# c = 'hallow world'
# print(a, b , c)
# print(a, '-', b, '-', c)
# print('{} - {} - {}'.format(a,b,c))
# print(f'{a} - {b} - {c}')
# print('{2} - {1} - {0}'.format(a,b,c))

# a = 121 #целое
# b = 121.333 # целое
# c = 'Hallow World' # вещественное
# f = True # булевое
# c = False # булевое
# list = []  # список
# print(a)
# print(b)
# print(c)
# print(f)
# print(c)

# a = 12
# b = 3 # -3   - унарный минус и унарный плюс(необезателен)
# c = a + b # сложение
# d = a - b #  вычистание
# e = a * b # умножение
# f = a / b # обычное деление
# t = a // b # деление без остатка
# y = a % b # остаток от деления
# o = a ** b # возведение в степень

# #Логические операции
# a = 1 < 4
# print(a) # False
# a = 1 < 4
# print(a) # True

# a = [1, 2]
# b = [1, 2]
# print(a == b) # True

# a = 'qwe'
# b = 'qwe'
# print(a == b) #True

# a = 1 < 3 < 5 < 10
# print(a) #True

# func = 1
# T = 4
# x = 123
# print(func<T>x) # False

# f = 1 > 2 or 4 < 6
# print(f) #True

# f = 1 > 2 and 4 < 6
# print(f) #False

# f = [1,2,3,4]
# print(f) #(1,2,3,4)
# print(2 in f) # true
# print(not 2 in f) #False
# print(7 in f) # False

# is_odd = f[0] % 2 == 0
# print(is_odd) # False

# a = int(input('введите число А '))
# b = int(input('введите число B '))
# if a > b:
#     print(f'a = {a}')
# else:
#     print(f'b = {b}')

# user_name = input('Введите имя: ')
# if user_name == "маша":
#     print('Ура, это же маша!')
# elif user_name == "Марина":
#     print('Я так ждал вас, Марина')
# elif user_name == 'Ильнар':
#     print('Ильнар - топ')
# else: 
#     print(f'Привет, {user_name}')

#развернутое число
# original = 123
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else: 
#     print('Пожалуй \nхватит')
# print(inverted)

# for i in 1,2,3,4,5:
#     print(i**2)

# list = [1,2,3,4,5]
# for i in list :
#     print(i**2)

# r = range(10)
# for i in r:
#     print(i)

# for i in range(5):
#     print(i)

# for i in 'qweerty':
#     print(i)

#Работа со строками
# text = 'сьешь еще этих мягких французких  булок'
# print(len(text)) #39
# print('еще' in text) #True
# print(text.isdigit()) #False
# print(text.islower()) #True
# print(text.replace('еще', 'ЕЩЕ')) #

# for i in text:
#     print(i)

# text = 'сьешь еще этих мягких французких  булок'
# print(text)
# print(text[0]) #c
# print(text[1]) #ь
# print(text[len(text)-1]) #к
# print(text[-5])#б
# print(text[:])#print(text)
# print(text[:2]) #сь
# print(text[len(text)-2:]) #ок
# print(text[2:9]) #ешь еще
# print(text[6: - 18])# еще этих мягких
# print(text[0:len(text):6]) #сеикаил
# print(text[: : 6])#сеикаил


# #Списки

# numbers = [1, 2, 3, 4, 5]
# print(numbers) # [1, 2, 3, 4, 5]

# numbers_range = list(range(1,6))
# print(numbers_range) # [1, 2, 3, 4, 5]
# numbers[0] = 10 
# print(f'{len(numbers)} len') #5 len
# print(numbers)#[10, 2, 3, 4, 5]

# for i in numbers:
#     i *= 2
#     print(i) #[20, 4, 6, 8, 10]

# print(numbers) #[10, 2, 3, 4, 5]

def f(x):
    if x == 1:
        return 'целое' #str
    elif x  == 2.3:
        return 23 #int
    else:
        return #NoneType

print(f(1))