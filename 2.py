f = open("students.csv", encoding="utf8")
students = []
f.readline()
for i in f:
    students.append(i[:-1])
xd = []
a=[]
class Student:
    pass
for i in range(len(students)):
    xd.append(Student())
for i in range(len(students)):
    s = students[i].split(",")
    xd[i].idd = s[0]
    xd[i].name = s[1]
    xd[i].tidd = s[2]
    xd[i].clas = s[3]
    if s[4] == "None":
        s[4] = '0'
    xd[i].score = s[4]
print("10 класс:")
k=0
for i in range(len(xd)):
    t = xd[i]
    j = i - 1
    while j >= 0 and t.score > xd[j].score:
        xd[j+1] = xd[j]
        j -= 1
    xd[j+1] = t
for i in range(1,len(students)):
    if xd[i].clas[:-1] == "10":
        k += 1
        print(k, "место", xd[i].name)
    if k == 3:
        break
