def calculate_structure_sum(*data_structure):
    summa = 0
    val = data_structure
    new_list2 = []
    if isinstance(val, tuple):
        summa += sum(j for j in val if isinstance(j, int))
        summa += sum(len(j) for j in val if isinstance(j, str))
        if len(val) > 1:
            for g in range(len(val)):
                if isinstance(val[g], dict) or isinstance(val[g], tuple) or isinstance(val[g], list):
                    if isinstance(val[g], dict):
                        val = list(val)
                        for key, value in val[g].items():
                            new_list2.append([key, value])
                        val[g] = new_list2
                    summa += calculate_structure_sum(*val[g])
        if len(val) == 1:
            summa += calculate_structure_sum(*val[0])
    return summa

summa = 0
data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]
new_list = []

for i in range(len(data_structure)):
    if isinstance(data_structure[i], dict):
        for key, value in data_structure[i].items():
            new_list.append([key, value])
        data_structure[i] = new_list
    summa += calculate_structure_sum(*data_structure[i])

print(summa)