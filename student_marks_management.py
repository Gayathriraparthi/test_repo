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

count_std_greater_than_90 = {"Mathematics": 0,"Telugu":0,"English":0,"Social" :0,"Physics":0,"Chemistry":0}

for i in std_dict:
    if std_dict[i]["Mathematics"] > 90:
        count_std_greater_than_90["Mathematics"]+= 1
    if std_dict[i]["Telugu"] > 90:
        count_std_greater_than_90["Telugu"]+= 1
    if std_dict[i]["English"] > 90:
        count_std_greater_than_90['English']+= 1
    if std_dict[i]["Chemistry"] > 90:
        count_std_greater_than_90["Chemistry"] += 1
    if std_dict[i]["Physics"] > 90:
        count_std_greater_than_90["Physics"] += 1
    if std_dict[i]["Social"] > 90:
        count_std_greater_than_90["Social"]+= 1

#print(count_std_greater_than_90)

a = max(count_std_greater_than_90, key = lambda x:count_std_greater_than_90[x])

print(f"The faculty with highest student count greater than 90% is {faculty[a]} and subject is {a}")

#2. Find the faculty with highest pass percentage (> 40%) 

count_pass_std = {"Mathematics": 0,"Telugu":0,"English":0,"Social" :0,"Physics":0,"Chemistry":0}

for i in std_dict:
    if std_dict[i]["Mathematics"] > 40:
        count_pass_std["Mathematics"]+= 1
    if std_dict[i]["Telugu"] > 40:
        count_pass_std["Telugu"]+= 1
    if std_dict[i]["English"] > 40:
        count_pass_std['English']+= 1
    if std_dict[i]["Chemistry"] > 40:
        count_pass_std["Chemistry"] += 1
    if std_dict[i]["Physics"] > 40:
        count_pass_std["Physics"] += 1
    if std_dict[i]["Social"] > 40:
        count_pass_std["Social"]+= 1

#print(count_pass_std)

b = max(count_pass_std, key = lambda x:count_pass_std[x])

pass_percent = (count_pass_std[b]/len(std_dict))*100

res = [(k, v) for k,v in count_pass_std.items() if  count_pass_std[b] == v]

if len(res) > 1:
    print(f"The faculty with highest pass pecentage are {', '.join([faculty[i[0]] for i in res])}, their respective subjects are {', '.join([i[0] for i in res])} with a pass percentage of {pass_percent}")
else:
    print(f"The faculty with highest pass pecentage is {faculty[res[1]]}, their respective subjects is {res[0]} with a pass percentage of {pass_percent}")


#3.Find the faculty with least pass percentage (<= 40%) 

count_fail_std = {"Mathematics": 0,"Telugu":0,"English":0,"Social" :0,"Physics":0,"Chemistry":0}

for i in std_dict:
    if std_dict[i]["Mathematics"] <= 40:
        count_fail_std["Mathematics"]+= 1
    if std_dict[i]["Telugu"] <= 40:
        count_fail_std["Telugu"]+= 1
    if std_dict[i]["English"] <= 40:
        count_fail_std['English']+= 1
    if std_dict[i]["Chemistry"] <= 40:
        count_fail_std["Chemistry"] += 1
    if std_dict[i]["Physics"] <= 40:
        count_fail_std["Physics"] += 1
    if std_dict[i]["Social"] <= 40:
        count_fail_std["Social"]+= 1

f = max(count_fail_std,key = lambda x:count_fail_std[x])

fail_percent = (count_fail_std[f]/len(std_dict))*100

print(f"The faculty with least pass pecentage is {faculty[f]},subject is {f} and fail percentage is {fail_percent}")


#4.Who is the top student with maximum total?

total_marks = {}

for i in std_dict:
    total = std_dict[i]["Social"] + std_dict[i]["Physics"]+ std_dict[i]["Chemistry"]+std_dict[i]["English"]+std_dict[i]["Telugu"]+std_dict[i]["Mathematics"]
    total_marks[i] = total
    
top_student = max(total_marks, key = lambda x: total_marks[x])

print(f"The top_student is {top_student} with highest total of {total_marks[top_student]} marks")

#5.Who is the best student in Mathematics?

m = max(std_dict, key = lambda x:std_dict[x]["Mathematics"])

print(f"The best student in Mathematics is {m} with {std_dict[m]['Mathematics']} marks")

#6.What is the average mark for each subject, (ignore failures)?

avg_of_each_sub = {"Mathematics": 0,"Telugu":0,"English":0,"Social" :0,"Physics":0,"Chemistry":0}

math_sum = 0; math_count = 0
tel_sum = 0; tel_count = 0
eng_sum = 0; eng_count = 0
chemistry_sum = 0; chemistry_count = 0
physics_sum = 0; physics_count = 0
social_sum = 0; social_count = 0

for std in std_dict:
    
    if std_dict[std]["Mathematics"] > 40:
        math_sum += std_dict[std]["Mathematics"]
        math_count += 1
        avg_of_each_sub["Mathematics"] = round(math_sum / math_count,2)
               
    if std_dict[std]["Telugu"] > 40:
        tel_sum += std_dict[std]["Telugu"]
        tel_count += 1
        avg_of_each_sub["Telugu"] = round(tel_sum / tel_count,2)
        
    if std_dict[std]["English"] > 40:
        eng_sum += std_dict[std]["English"]
        eng_count += 1
        avg_of_each_sub["English"] = round(eng_sum / eng_count,2)
        
    if std_dict[std]["Chemistry"] > 40:
        chemistry_sum += std_dict[std]["Chemistry"]
        chemistry_count += 1
        avg_of_each_sub["Chemistry"] = round(chemistry_sum / chemistry_count,2)
        
    if std_dict[std]["Physics"] > 40:
        physics_sum += std_dict[std]["Physics"]
        physics_count += 1
        avg_of_each_sub["Physics"] = round(physics_sum / physics_count,2)
        
    if std_dict[std]["Social"] > 40:
        social_sum += std_dict[std]["Social"]
        social_count += 1
        avg_of_each_sub["Social"] = round(social_sum / social_count,2)

print(f"Ignoring failures Average percentage of each subject is {avg_of_each_sub}")

#7.Find the student with least numbers of marks as total.

least_mark_student = min(total_marks,key = lambda x: total_marks[x])

print(f" {least_mark_student} is with least total no. of marks and marks are {total_marks[least_mark_student]}")