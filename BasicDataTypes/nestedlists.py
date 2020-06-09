#python3 solution

students = [[ input(), float(input())] for i in range(int(input()))]
studentsorted = sorted(set([student[1] for student in students]))
for name in sorted(student[0] for student in students if student[1] == studentsorted[1]):
    print (name)
