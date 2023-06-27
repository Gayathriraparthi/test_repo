'''1. What is the output of the following python code?'''
#print(1, 2, 3, 4, sep='#', end='&')
#output : 1#2#3#4&

'''2. Which is the only string that Python considers as False when converting to boolean?'''
#a = '' # empty string

'''3. What would be the output of this code if the user tried to enter 3 in the console?
choice = int(input('Pick a number: '))
if choice == 3:
print('Good choice')
else:
print('You could have chosen better')
else:
print('No luck this time')'''
#output: Good choice

'''4. Given the following program:
answer_a = int(input('Try to guess the first number: '))
if answer_a == 8:
answer_b = int(input('Correct! Now, guess the second number: '))
    if answer_b == 5:
    print('You won!')
    else:
    print('You only got one number right. So close!')
else:
print('Wrong!')
What will happen when the user enters 8 and then 3?'''
#output: You only got one number right. So close!


'''5. Write a python program to calculate and print out the average of a set of integers.'''
#s = {1,2,3,4,5}
#avg = sum(s)/len(s)
#print(avg)

'''6. Write a python program to check whether the given integer is a multiple of 5.'''

# num = int(input('enter a number:'))
# if num % 5 == 0:
#     print(f'{num} is a multiple of 5')
# else:
#     print(f'{num} is not a multiple of 5')
    
'''7. Suppose that you have initialized ALPHABET as
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
What are the values of the following slice expressions?
(a) ALPHABET[7:9] ans= HI
(b) ALPHABET[-3:-1] ans = XY
(c) ALPHABET[:3] ans = ABC
(d) ALPHABET[-1:] ans= Z
(e) ALPHABET[14:-12] ans = '' empty string
(f) ALPHABET[1:-1] ans = BCDEFGHIJKLMNOPQRSTUVWXY
(g) ALPHABET[0:5:2] ans = ACE
(h) ALPHABET[::-1] ans = ZYXWVUTSRQPONMLKJIHGFEDCBA reverse of string
(i) ALPHABET[5:2:-1] ANS = FED
(j) ALPHABET[14:10:-2] ANS = OM '''

'''8. Write a program to replace whitespace with hyphen in any given string.'''
# string = input('enter a word:')
# x = string.replace(' ','-')
# print(x)

'''9. Consider an amusement park that charges different rates for different age groups:
● Admission for anyone under age 4 is free.
● Admission for anyone between the ages of 4 and 18 is Rs. 25.
● Admission for anyone age 18 or older is Rs. 40.
Write a program to print the admission price message.'''

# age = int(input('enter age in number:'))

# if  0 <= age < 4:
#     print(f'Free')
# elif 4 <= age < 18:
#     print(f'Amusement park charge is 25')
# elif age >= 18:
#     print(f'Amusement park charge is 40')
# else:
#     print('invalid input')
    

'''10. Alice, Bob and Carol have agreed to pool their Halloween candy and split it evenly among
themselves. For the sake of their friendship, any candies leftover will be smashed. For
example, if they collectively bring home 91 candies, they'll take 30 each and smash 1.
Write a program to calculate and print how many candies they must smash for a given
haul assuming that the variables are representing the number of candies collected by
alice, bob, and carol
alice_candies = 121
bob_candies = 77
carol_candies = 109'''

alice_candies = 121
bob_candies = 77
carol_candies = 109
sum_of_candies = alice_candies + bob_candies + carol_candies
smashed = sum_of_candies % 10

print(f'No.of. candies to be smashed :{smashed}')
