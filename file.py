'''
Омлет
3
Яйцо | 2 | шт
Молоко | 100 | мл
Помидор | 2 | шт
Утка по-пекински
4
Утка | 1 | шт
Вода | 2 | л
Мед | 3 | ст.л
Соевый соус | 60 | мл
Запеченный картофель
3
Картофель | 1 | кг
Чеснок | 3 | зубч
Сыр гауда | 100 | г
Фахитос
5
Говядина | 500 | г
Перец сладкий | 1 | шт
Лаваш | 2 | шт
Винный уксус | 1 | ст.л
Помидор | 2 | шт
Должен получится следующий словарь
cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }
'''

from pprint import pprint
with open ('recipes.txt', encoding = 'utf-8') as f:
    file_ = f.read()
    file_ = file_.split('\n\n')
# print(file_)

class Dish:
    def __init__(self,name_d, list_ing):
        self.name_d = name_d
        self.list_ing = list_ing

class Ingredient:
    def __init__(self, name_i, quantity, measure):
        self.name_i = name_i
        self.quantity = quantity
        self.measure = measure
cook_book ={}
for dish in file_:
    dish = dish.split('\n')
    # print(dish)
    dish = Dish(dish[0],dish[2:])
    list_ing = []
    for ingr in dish.list_ing:
        ingr = ingr.split('|')
        # print(ingr)
        ingr = Ingredient(ingr[0],ingr[1],ingr[2])
        dish_ingredients = {'ingredient_name': ingr.name_i.strip(), 'quantity': int(ingr.quantity), 'measure': ingr.measure.strip()}
        # print(dish_ingredients)
        list_ing.append(dish_ingredients)
        # print(list_ing)
    cook_book[dish.name_d] = list_ing
pprint(cook_book)

'''Задача №2
Нужно написать функцию, которая на вход принимает список блюд из cook_book и количество персон для кого мы будем готовить
get_shop_list_by_dishes(dishes, person_count)
На выходе мы должны получить словарь с названием ингредиентов и его количества для блюда. Например, для такого вызова
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
Должен быть следующий результат:
{
  'Картофель': {'measure': 'кг', 'quantity': 2},
  'Молоко': {'measure': 'мл', 'quantity': 200},
  'Помидор': {'measure': 'шт', 'quantity': 4},
  'Сыр гауда': {'measure': 'г', 'quantity': 200},
  'Яйцо': {'measure': 'шт', 'quantity': 4},
  'Чеснок': {'measure': 'зубч', 'quantity': 6}
}
Обратите внимание, что ингредиенты могут повторяться'''





def get_shop_list_by_dishes(dishes, person_count):
    cookbook ={}
    for elem in dishes:
     for dish in cook_book[elem]:
      cookbook.setdefault(dish['ingredient_name'],{'quantity': dish['quantity']*person_count, 'measure':dish['measure']})
    return cookbook


pprint(get_shop_list_by_dishes(['Запеченный картофель','Омлет'],2))

'''Задача №3
В папке лежит некоторое количество файлов. Считайте, что их количество и имена вам заранее известны, 
пример для выполнения домашней работы можно взять тут
Необходимо объединить их в один по следующим правилам:
Содержимое исходных файлов в результирующем файле должно быть отсортировано по количеству строк в 
них (то есть первым нужно записать файл с наименьшим количеством строк, а последним - с наибольшим)
Содержимое файла должно предваряться служебной информацией на 2-х строках: имя файла и количество строк в нем
Пример Даны файлы: 1.txt
Строка номер 1 файла номер 1
Строка номер 2 файла номер 1
2.txt
Строка номер 1 файла номер 2
Итоговый файл:
2.txt
1
Строка номер 1 файла номер 2
1.txt
2
Строка номер 1 файла номер 1
Строка номер 2 файла номер 1'''


import os


list_file = []

with open('1.txt', encoding = 'utf-8') as f1:
    file_n = f1.name
    file_text = f1.readlines()
    file_len = len(file_text)
    list_file.append([file_n, file_len, ''.join(file_text)])


with open('2.txt', encoding='utf-8') as f2:
    file_n = f2.name
    file_text = f2.readlines()
    file_len = len(file_text)
    list_file.append([file_n, file_len, ''.join(file_text)])



with open('3.txt', encoding = 'utf-8') as f3:
    file_n = f3.name
    file_text = f3.readlines()
    file_len = len(file_text)
    list_file.append([file_n, file_len, ''.join(file_text)])


def sort_list(list_):
   return list_[1]
str_=''
for elem in list_file:
  list_file.sort(key=sort_list)
for el in list_file:
    el[1]=str(el[1])
    str_ += el[0] + '\n'+el[1] + '\n'+el[2] + '\n'

file_path = os.path.join(os.getcwd(), 'All.txt')
with open(file_path, 'w', encoding = 'utf-8') as f4:
     f4.write(str_)





# print(file_path)
# with open(file_path, 'r', encoding = 'utf-8') as f:
#     print(f.read())
