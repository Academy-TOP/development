bool_true = True
bool_false = False
string = "строка"
zero_string = ""
my_int_float = 1
zero = 0
my_list = [0]
zero_list = []
my_tuple = 0,
zero_tuple = tuple()
my_set = {0}
zero_set = set()
my_dict = {0: 0}
zero_dict = {}
print('bool_true -', str(bool_true))
print('bool_false -', str(bool_false))
print('string -', str(string))
print('zero_string -', str(zero_string))
print('my_int_float -', str(my_int_float))
print('zero -', str(zero))
print('my_list -', str(my_list))
print('zero_list -', str(zero_list))
print('my_tuple -', str(my_tuple))
print('zero_tuple -', str(zero_tuple))
print('my_set -', str(my_set))
print('zero_set -', str(zero_set))
print('my_dict -', str(my_dict))
print('zero_dict -', str(zero_dict))

print('\nПреобразование в целочисленный тип данных:')
bool_true = True
bool_false = False
string = "0"
my_int = 1
my_float = 1.1
zero = int()
print('bool_true -', int(bool_true))
print('bool_false -', int(bool_false))
print('string -', int(string))
print('my_int -', int(my_int))
print('my_float -', int(my_float))
print('zero -', zero)

print('\nПреобразования в список, кортеж, множество и frozenset')
string = "string"
my_list = [0]
my_tuple = 0,
my_set = {0}
my_frozenset = frozenset()
my_dict = {0: 0}
zero_list = list()
print('string -', frozenset(string))
print('my_list -', frozenset(my_list))
print('my_tuple -', frozenset(my_tuple))
print('my_set -', frozenset(my_set))
print('my_frozenset -', frozenset(my_frozenset))
print('my_dict -', frozenset(my_dict))
print('zero_list -', frozenset(zero_list))

print('\nПреобразования в словарь')
my_list = ['01', ["1", 2], (2, "3"), {3.3, 4}, frozenset({5, 6})]
my_tuple = ('01', ["1", 2], (2, "3"), {3.3, 4}, frozenset({5, 6}))
my_set = {'01', (2, "3"), frozenset({5, 6})}
print(dict(my_list))
print(dict(my_tuple))
print(dict(my_set))

my_dict = dict(string='string', number=0, list=[])
print(my_dict)

print('\nЗадача "Стартапер"')
my_basket = {}
ware_1 = input('Введите продукт:\n')
my_basket[ware_1] = int(input('Введите стоимость выбранного Вами продукта:\n'))
ware_2 = input('Введите продукт:\n')
my_basket[ware_2] = int(input('Введите стоимость выбранного Вами продукта:\n'))
ware_3 = input('Введите продукт:\n')
my_basket[ware_3] = int(input('Введите стоимость выбранного Вами продукта:\n'))
ware_4 = input('Введите продукт:\n')
my_basket[ware_4] = int(input('Введите стоимость выбранного Вами продукта:\n'))
ware_5 = input('Введите продукт:\n')
my_basket[ware_5] = int(input('Введите стоимость выбранного Вами продукта:\n'))
total_cost = sum(my_basket.values())
print('Ваша продуктовая корзина:\n')
print(my_basket.popitem())
print(my_basket.popitem())
print(my_basket.popitem())
print(my_basket.popitem())
print(my_basket.popitem())
print('Общая стоимость: ', total_cost)
