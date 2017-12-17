#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 14.  Recursion"""


#Fib sequence outputs the corresponding value for the nth term
nterms = int(input("How many terms? "))
fiblist=[]

def fibonnaci(n):
    if n <= 1:
        return n

    else:
        return(fibonnaci(n-1) + fibonnaci(n-2))

for i in range(nterms):
    fiblist.append(fibonnaci(i))

print("The {} -th element of the Fibonnaci sequence is:".format(nterms))
print fiblist[-1]


#Euclid’s GCD Algorithm
a=100
b=25

def gcd(a, b):
     if a == 0:
         return b
     elif b == 0:
         return a
     else:
         return gcd(b, a % b)

if __name__ == "__main__":
    print ("The GCD for {} and {} is:".format(a, b))
    print gcd(a,b)


#Comparing two strings.  This is not recursive.
def compareTO(s1, s2):
    if len(s1) < len(s2):
        return -1
    elif len(s1) == len(s2):
        return 0
    else:
        return 1

if __name__ == "__main__":
    print """
        • -1  if s1 < s2,
        • 0 if s1 == s2
        • 1 if s1 > s2
        """
    print (compareTO('abcdefgh', 'abcdefgh'))


