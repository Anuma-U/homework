calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(str):
    count_calls()
    print("Результат вывода 1 функции: ", len(str), str.upper(), str.lower())

def is_contains(str, list_to_search):
    count_calls()
    list_to_search = list((i.lower() for i in list_to_search))
    str = str.lower()
    return str in list_to_search

anser = "да"
while anser == "да":
    anser = input("Вы хотите записать строку для выполнения 1 функции? да/нет: ")
    if anser.lower() == "да":
        string_info(input("Введите любую строку: "))
    else:
        break

anser = "да"
while anser == "да":
    anser = input("Вы хотите записать строку и список для выполнения 2 функции? да/нет: ")
    if anser.lower() == "да":
        str = (input("Введите любую строку: "))
        list_to_search = (input("Введите список слов без запятой через пробел: ")).split()
        print("Результат работы 2 функции: ", is_contains(str, list_to_search))
    else:
        break

print(" колличество вызывов функций: ", calls)