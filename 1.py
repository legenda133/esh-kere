f = open("students.csv", encoding="utf8")
students = []
name = f.readline().strip()
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
    if 'Хадаров Владимир' in xd[i].name:
         print('Ты получил:', xd[i].score,'за проект -', xd[i].tidd)
for i in xd:
    s = 0
    k = 0
    if i.score == 'None':
        for j in xd:
            if j.clas == i.clas and j.score != 'None':
                k += 1
                s += int(j.score)
        i.score = f'{s / k:.3f}'
f = open('students_new.csv', 'w')
print(name, file=f)
for i in xd:
    print(i.idd, ',', i.name, ',', i.tidd, ',', i.clas, ',', i.score, file=f)
f.close()
