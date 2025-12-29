'''
In this problem, we will implement the Sieve of Eratosthenes method for computing primes up to

a specified number (les than or equal to a given number).



You need to collect all the prime numbers in a list and print this list (sorted order). The

evaluation will check your output list, though the implementation efficiency is also important.



For an example, the python script will be run using the following command:

python3 sieve_of_eratosthenes.py 10



Here the input (10) is the number given, so the output should be a list of all prime numbers

that are less than or equal to 10:

[2, 3, 5, 7]



You will need to use a function from the sys library to implement the command line parameter.



This problem seems quite complicated, so let's break it down into steps:



Step 1:

First we will need a list of numbers from 2 to the given number, so that we can select the

primes out from this based on the method.



Step 2:

We need to keep iterating over this list till we have no more numbers to check. We also need

a list to store the output.



Step 3:

In the Sieve of Eratosthenes method, the next uncrossed/valid number is prime and is

recorded, and then from among the remaining numbers (yet to check), all the multiples

of this recorded number are removed. In this step, try using list comprehension (check

reference 2).


References:

1. Sieve of Eratosthenes
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

2. list comprehension
https://www.w3schools.com/python/python_lists_comprehension.asp

'''

import sys
import math

try:
	limit = int(sys.argv[1])
except:
	print("Usage: python3 sieve_of_eratosthenes.py <num>")
	sys.exit()

list1 = list(range(2, limit+1))
list2 = [True] * (limit-1)

for i in range(2,int(math.sqrt(limit))+1):
	if list2[i-2]:
		for j in range(0, int(limit/i) - i + 1): ## Blooody fast (method from pseudocode on wikipedia)
			list2[i*(i+j) - 2] = False

print([x for x in list1 if list2[x-2]]) # the index-2 everywhere is because in the code on wikipedia they allow indexing from custom index like 2

# # This one works too, but is EXPONENTIALLY slower
# while list1 != []:
# 	num = list1.pop(0)
# 	list2.append(num)
# 	list1 = [x for x in list1 if (x < num*num) or (x%num !=0)] # keep only non-multiples, while not checking mod for numbers below num^2 as all below multiples of num (before num^2) have already been removed

# print(list2)