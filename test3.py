"""1. Print all Pairs which make sum N for the given list.
e,g: l = [4, 3, 6, 8, 2, 9, 7,  5]
N = 10,
It should print (4, 6), (8,2),(3, 7)"""
l = [4, 3, 6, 8, 2, 9, 7,  5]
N = 10

for i in range(len(l)-1):
    for j in range(i+1,len(l)-1):
        if l[i] + l[j] == N:
            print((l[i],l[j]))


"""2. 
10
10 9
10 9 8
10 9 8 7
10 9 8 7 6"""

for i in range(10,5,-1):
    for j in range(10,i-1,-1):
        print(j,end = " ")
    print()

"""3. Merge the following lists
given 
l1 = [1, 4, 7, 9]
l2 = [3, 8, 10]
output = [1,3,4,7,8,9,10]
"""
#method-1
l1 = [1, 4, 7, 9]
l2 = [3, 8, 10]
output = sorted(l1 + l2)
print(output)

#method-2

l1 = [1, 4, 7, 9]
l2 = [3, 8, 10]

output = l1.copy()

for i in l2:
    output.append(i)
    
output = sorted(output)    
print(output)


"""4: sort the following list without using sort() function in increasing order"""
l = [1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0]

for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if l[i] > l[j]:
            l[i],l[j] = l[j],l[i]
    
print(l)   