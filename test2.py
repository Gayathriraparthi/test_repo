"""1. Write a program to print a string formed with the first 2 and the last 2 characters of the given string. Assume
the size of given string is always greater than or equal to 4.
"""
string = input("given string:")
new_string = string[0:2] + string[-2:]
print(new_string)


"""2. Write a program to check if a word is present in the given string. For example, if the word 'orange' is present
in the "This is orange juice".
"""
string = "This is orange juice"
word = "orange"
if word in string:
    print(f"{word} is present in given string")
else:
    print(f"{word} is not present in given string")
    
"""3. Write a program that will print whether the number is a single digit number or double digit number or big number.
If given number is one digit number, print "Single digit number".If given number is two digit number, print "Double digit
number". If number is three digit number or bigger, print "Big number".
"""
num = int(input("enter number:"))

if len(str(num)) >= 3:
    print("Big number")
elif len(str(num)) == 2:
    print("Double digit number")
elif len(str(num)) == 1:
    print("Single digit number")
    
    
"""4. Write a program that takes a list and splits into smaller lists of given size. For example, 
if lst = [1, 2, 3, 4, 5, 6], size = 2, it should return [[1, 2], [3,4], [5,6]] and if lst = [1,2,3,4,5,6,7,8,9],
size = 4 then it should return [[1,2,3,4],[5,6,7,8],[9]]. 
"""
#lst = [1, 2, 3, 4, 5, 6]
lst = [1,2,3,4,5,6,7,8,9]
size = int(input("enter size:"))
lst_new = []
splits = (len(lst)//size)+1

for i in range(0,len(lst),size):
    sub_list = lst[i:i+size]
    lst_new.append(sub_list)
    
print(lst_new)   


"""5. Write a program to print a list with all duplicates in the given list. For example, if lst=[1, 3, 2, 1, 2, 5, 6] 
it should return [1, 2].
"""
lst = [1, 3, 2, 1, 2, 5, 6] 
dup = []
for i in set(lst):
    if lst.count(i) > 1:
        dup.append(i)
        
print(dup)
    
    
"""6. Write a program to find and group anagrams in a given list of words. Two words are called anagrams if one word can
be formed by rearranging letters of another. For example 'eat', 'ate' and 'tea' are anagrams. Assume the list given is
['eat', 'ate', 'done', 'tea', 'soup', 'node'] then it should return [['eat', 'ate', 'tea], ['done', 'node'], ['soup']]
"""
lst = ['eat', 'ate', 'done', 'tea', 'soup', 'node']
anagram = {}

for word in lst:
    sorted_word = "".join(sorted(word))
    if sorted_word not in anagram:
        anagram[sorted_word]= []
for i in anagram:
    for j in lst:
        if sorted(i) == sorted(j):
            anagram[i].append(j)
        

print(anagram.values())


"""7. Write a program to interchange keys and values in a dictionary. For example, if the given dictionary
is {'x': 1, 'y': 2, 'z': 3}, it should return {1: 'x', 2: 'y', 3: 'z'}.
"""
d = {'x': 1, 'y': 2, 'z': 3}

keys = d.values()
values = d.keys()

modified_d = dict(zip(keys,values))

print(modified_d)

"""8. Write a program to display the elements of list thrice if it is a number and display the element terminated 
with ‘#’ if it is not a number. For example, if the content of list is [‘41’, ‘DHRUVA’, ‘GURU’, ‘13’, ‘ZARA’]The output
should be414141DHRUVA#GURU#131313ZARA#
"""
l = ["41", "DHRUVA", "GURU", "13", "ZARA"]
output = ""

for i in l:
    if i.isdigit() == True:
        output += (str(i)*3)
    elif i.isalpha() == True:
        output += i+"#"
        
print(output)


"""9. Write a program to return a list of sorted values based on the keys in the dictionary. For example,
if {'x': 1, 'y': 2, 'a': 3} is the dictionary then it should return [3, 1, 2].
"""

d = {'x': 1, 'y': 2, 'a': 3}
sorted_keys = sorted(d)
values = []

for i in sorted_keys:
    values.append(d[i])
        
print(values)     

"""10. Write a program to remove all the tuples from a given list of tuples where the second element of the tuple is 
even number."""

l = [(1,2,3,4,5),
     (10,11,12,13),
     (23,14,15,17,18),
     (25,17,34,18,7)]

for i in (l):
    if l[l.index(i)][1] % 2 == 0:
        l.remove(i)

print(l)