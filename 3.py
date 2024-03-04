f = open("students.csv", encoding="utf8")
students = []
for i in f:
    students.append(i[:-1])
xd = []
class Student:
    pass
for i in range(len(students)-1):
    xd.append(Student())
for i in range(len(students)-1):
    s = students[i].split(",")
    xd[i].idd = s[0]
    xd[i].name = s[1]
    xd[i].tidd = s[2]
    xd[i].clas = s[3]
    xd[i].score = s[4]
    if s[4] == "None":
        s[4] = -1
for i in range(len(students)):
    x = input()
    while x != 'СТОП':
        d=int(x)
        print('Проект №:', (d),'делал:', xd[d+1].name, 'он(а) получил(а) оценку -', xd[d+1].score)
        x=input()
    if x=='СТОП':
        break