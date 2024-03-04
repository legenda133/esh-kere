def insertionSort(arr):
    n = len(arr)
    if n <= 1:
        return
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
f = open("students.csv", encoding="utf8")
students = []
for i in f:
    students.append(i[:-1])
xd = []
a=[]
class Student:
    pass
for i in range(len(students)-1):
    xd.append(Student())
for i in range(1,len(students)-1):
    s = students[i].split(",")
    xd[i].idd = s[0]
    xd[i].name = s[1]
    xd[i].tidd = s[2]
    xd[i].clas = s[3]
    if s[4] == "None":
        s[4] = '0'
    xd[i].score = s[4]
    a.append(xd[i].score)
print(insertionSort(a))
print("10 класс:")
k=0
for i in range(1,len(students)):
    if xd[i].clas[:-1] == "10":
        k += 1
        print(k, "место", xd[i].name)
    if k == 3:
        break
