grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
students.sort()
sred_ball = {students[0]: sum(grades[0]) / len(grades[0])}
for i in range(1, len(students)):
    sred_ball.update({students[i]: sum(grades[i]) / len(grades[i])})
print(sred_ball)