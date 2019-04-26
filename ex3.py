# + plus does addition
# - minus does subtraction
# / slash does division
# * asterisk does multiplication
# % percent is the modulus; this is the remainder after dividing one number
# into another i.e. 3 % 2 is 1 because 2 goes into 3 once with 1 left over
# < less-than
# > greater-than
# <= less-than-equal
# >= greater-than-equal

#PEMDAS (Python follows the standard order of operations)
#P   Parentheses, then
#E   Exponents, then
#MD  Multiplication and division, left to right, then
#AS  Addition and subtraction, left to right

#Modulus Tip: One way to look at this is "X divided by Y with J remaining"
# For example: "100 divided by 16 with 4 remaining." The result of '%' is the J part,
# or the remaining part.

#Python 2 doesn't calculate exact math unless you use a floating point number.
# For instance, 7/4 results in 1, while 7.0/4.0 results in 1.75
#So, floating points are basically numbers with a decimal. This is required
# in order for Python to calculate fractions and not just whole numbers.

#line below prints a string
print "I will now count my chickens:"

#line below prints the string and then prints answer to the math problem
print "Hens", 25 + 30 / 6

#below line prints the string and then prints the answer to the math problem
print "Roosters", 100 - 25 * 3 % 4
#75 % 4 = 3 (because 4 goes into 75 18 times; and
#4 times 18 = 72, which leaves 3 left over)

#line below prints the string
print "Now I will count the eggs:"

#lines below print the answer to the math problems
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
print 3+2+1-5+4%2-1/4+6
print 'NEW with floating numbers'
print 3.0+2.0+1.0-5.0+4.0%2.0-1.0/4.0+6
#the above two lines are the same; spacing doesn't matter
#3+2+1-5+0-0+6
#7
#python 2 calculates 1/4 as 0; in order to obtain the accurate answer of
# .25, you must use floating points (decimals)

#line below prints the question AND then the answer
print "Is it true that 3+2<5-7?"
print "Is it true that 3.0+2.0<5.0-7.0?"

#line below prints the answer to the math problem
print 3+2<5-7
print 3.0+2.0<5.0+7.0

#lines below print the question AND then the answer
print "What is 3+2?", 3+2
print "NEW now with floating points!"
print "What is 3.0+2.0?", 3.0+2.0

print "What is 5-7?", 5-7
print "NEW now with floating points!"
print "What is 5.0-7.0?", 5.0-7.0

#line below prints the string
print "Oh, that's why it's False."

#line below prints the string
print "How about some more."

#line below prints the question AND answer
print "Is it greater?", 5 > -2
print "NEW now with floating points!"
print "Is it greater?", 5.0>-2.0

#line below prints the question AND answer
print "Is it greater or equal?", 5 >= -2
print "NEW now with floating points!"
print "Is it greater or equal?", 5.0>= -2.0

#line below prints the question AND answer
print "Is it less or equal?", 5 <= -2
print "NEW now with floating points!"
print "Is it greater or equal?", 5.0<= -2.0
