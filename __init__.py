chislo = int(input("Введите число от 3 до 20 для которого нужен пароль: "))
proverka_na_povtor = []
result = ""
for i in range(1, chislo):
    for j in range(i + 1, chislo):
        if chislo % (i + j) == 0:
            if [j, i] not in proverka_na_povtor:
                proverka_na_povtor.append([i, j])
                result += f"{i}{j}"
print(chislo, " - ", result)
