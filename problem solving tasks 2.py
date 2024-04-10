#program to calculate total no of vowels and count each individual vowels:
string = "Guvi Geeks Networks Private Limited"
string_lower = string.lower()
vowels = 0
vowels_a=0
vowels_e=0
vowels_i=0
vowels_o=0
vowels_u=0
for i in string_lower:
     #if i == "a","e"."i","o","u":
             
        if  i =="a" or i =="e" or  i =="i" or  i=="o" or i=="u":
             vowels=vowels+1
    
        if  i == "a": 
            vowels_a+=1
        if  i == "e": 
            vowels_e+=1
        if  i == "i": 
            vowels_i+=1
        if  i == "o": 
            vowels_o+=1
        if  i == "u": 
            vowels_u+=1

print("Total no of vowels in given string:", vowels, "and no of vowel a is:", vowels_a, "and no of vowel e is:", vowels_e, ", and no of vowel i is:", vowels_i, "and no of vowel o is:", vowels_o, "and no of vowel u is:", vowels_u)

"""
Output:

Total no of vowels in given string: 12 and no of vowel a is: 1 and no of vowel e is: 5 , and no of vowel i is: 4 and no of vowel o is: 1 and no of vowel u is: 1

"""
====================================================================================================================================================================================
#program to display 1 to 20 tnumbers in pyramid pattern using for loop 

rows = 21
# if you want user to enter a number, uncomment the below line
# rows = int(input('Enter the number of rows'))
# outer loop
for i in range(rows):
    # nested loop
    for j in range(i):
        # display number
        print(i, end=' ')
    # new line after each row
    print('')


    """
    output
Output:
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
6 6 6 6 6 6 
7 7 7 7 7 7 7 
8 8 8 8 8 8 8 8 
9 9 9 9 9 9 9 9 9 
10 10 10 10 10 10 10 10 10 10 
11 11 11 11 11 11 11 11 11 11 11 
12 12 12 12 12 12 12 12 12 12 12 12 
13 13 13 13 13 13 13 13 13 13 13 13 13 
14 14 14 14 14 14 14 14 14 14 14 14 14 14 
15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 
16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 
17 17 17 17 17 17 17 17 17 17 17 17 17 17 17 17 17 
18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 
19 19 19 19 19 19 19 19 19 19 19 19 19 19 19 19 19 19 19 
20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 

    """
================================================================================================================================================================

#Program to remove vowels from the given string:

string = "python is user friendly language!"
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
result = ""
for char in string:
    if char not in vowels:
        result += char
print(result)


"""
Output:
pythn s sr frndly lngg!
"""
===========================================================================================================================================================
#program to return unique chacracters from given string:

string = "python is used friendly language"
string=set(string)
print(string)

"""
Output:
{'s', 'h', 'g', 'd', 'r', 'f', 'a', 'u', 'p', 'l', 'y', ' ', 'e', 'o', 'i', 'n', 't'}

"""
======================================================================================================================================================


#Program to take string and return true if its palindrome or return false:

string=input("Enter a string " )
print("\n")
string_reverse=string[::-1]
if string_reverse == string: 
     print(True)
else:
     print(False)


"""

Output:
Enter a string madam

True
"""
================================================================================================================================================


# initializing string 
test_str = "Python Programming"
 
# printing original string
print ("The original string is : " + test_str)
====================================================================================================================================================
 
# using naive method to get
# Maximum frequency character in String
all_freq = {}
for i in test_str:
 if i in all_freq:
  all_freq[i] += 1
 else:
  all_freq[i] = 1
res = max(all_freq, key = all_freq.get) 
print (" Maximum frequency character in String", test_str + " is "+ str(res))

"""
Output:
The original string is : Python Programming
 Maximum frequency character in String Python Programming is P
"""
====================================================================================================================================================

#program to find given string are "anagram"
s1=input("Enter first string:" )
s2=input("Enter second string:")
if(sorted(s1)==sorted(s2)):
      print("The strings are anagrams.")
else:
      print("The strings aren't anagrams.")


Output:
========
Enter first string:silent
Enter second string:listen
The strings are anagrams.

=================================================================================================================================================

#program to count no of words in given string

countOfWords = len("Guvi is Computer Science Portal".split())
print("Count of Words in the given Sentence:", countOfWords)
print(len("Guvi is Computer Science Portal".split()))
 

Output:
========
Count of Words in the given Sentence: 5
5
