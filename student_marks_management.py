with open ("subject_faculty.csv","r") as file:

    faculty = {}

    for line in file:
        i = student = line.rstrip('\n').split(',')
        faculty.update({i[0]:i[1]})
        
#print(faculty)  

with open ("student_marks.csv","r") as f:
   
    std_dict = {}  #student records dictionary

    for line in f:
        record = line.rstrip('\n').split(',')
        record[2] = int(record[2])
        student = record[0]
        subject = record[1]
        marks = record[2]
        
        if student not in std_dict:
            std_dict[student] = {subject:marks}
        else:
            std_dict[student].update({subject:marks})
            
# print(std_dict) 

#1. Find the faculty with highest student count who got more than 90%.

count_std_greater_than_90 = {"Mathematics": 0,"Telugu": 0, "English": 0, "Social": 0, "Physics":0,"Chemistry":0}

for i in std_dict:
    for sub in count_std_greater_than_90:
        if std_dict[i][sub] > 90:
            count_std_greater_than_90[sub] += 1

a = max(count_std_greater_than_90, key = lambda x:count_std_greater_than_90[x])

print(f"The faculty with highest student count greater than 90% is {faculty[a]} and subject is {a}")


#2. Find the faculty with highest pass percentage (> 40%) 

count_pass_std = {"Mathematics": 0,"Telugu":0,"English":0,"Social" :0,"Physics":0,"Chemistry":0}

for i in std_dict:
    for sub in count_pass_std:
        if std_dict[i][sub] > 40:
            count_pass_std[sub]+= 1

b =  count_pass_std[max(count_pass_std, key = lambda x:count_pass_std[x])] # highest pass

pass_percent = (b/len(std_dict))*100

res = [(k, v) for k,v in count_pass_std.items() if  b == v] # subjects with highest pass

if len(res) > 1:
    print(f"The faculty with highest pass pecentage are {','.join([faculty[i[0]] for i in res])}, their respective subjects are {', '.join([i[0] for i in res])} with a pass percentage of {pass_percent}")
else:
    print(f"The faculty with highest pass pecentage is {faculty[res[1]]}, their respective subjects is {res[0]} with a pass percentage of {pass_percent}")

#3.Find the faculty with least pass percentage (<= 40%) 

count_fail_std = {"Mathematics": 0,"Telugu":0,"English":0,"Social" :0,"Physics":0,"Chemistry":0}

for i in std_dict:
    for sub in count_fail_std:
        if std_dict[i][sub] <= 40:
            count_fail_std[sub]+= 1

f = max(count_fail_std,key = lambda x:count_fail_std[x])

fail_percent = (count_fail_std[f]/len(std_dict))*100

print(f"The faculty with least pass pecentage is {faculty[f]},subject is {f} and fail percentage is {fail_percent}")

#4.Who is the top student with maximum total?

total_marks = {}

subjects = ["Mathematics","Physics","Chemistry","English","Telugu","Social"]

for i in std_dict:
    total = 0
    for j in subjects:
        total += std_dict[i][j]
    total_marks[i] = total

top_student = max(total_marks, key = lambda x: total_marks[x])

print(f"The top_student is {top_student} with highest total of {total_marks[top_student]} marks")


#5.Who is the best student in Mathematics?

m = max(std_dict, key = lambda x:std_dict[x]["Mathematics"])

print(f"The best student in Mathematics is {m} with {std_dict[m]['Mathematics']} marks")


#6.What is the average mark for each subject, (ignore failures)?

sub = {"Mathematics": [0,0], "Social":[0,0], "Telugu": [0,0], "English": [0,0], "Physics": [0,0], "Chemistry": [0,0]}
# sub dict for sub wise total and count of students

for std in std_dict:
    for s in sub:
        if std_dict[std][s] > 40:
            sub[s][0] += std_dict[std][s]
            sub[s][1] += 1
            
for s in sub.items():
    avg = round(s[1][0]/s[1][1], 2)
    print(f"Ignoring failures Average mark of {s[0]} is {avg}")   
    
#7.Find the student with least numbers of marks as total.

least_mark_student = min(total_marks,key = lambda x: total_marks[x])

print(f" {least_mark_student} is with least total no. of marks and marks are {total_marks[least_mark_student]}")
