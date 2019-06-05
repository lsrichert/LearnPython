# Exercise 5: More Variables and Printing

name = "Zed A. Shaw"
age = 35 #not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." %(eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

inches = 74
centimeters = inches * 2.54
print "%r inches equals %r centimeters." % (inches, centimeters)

pounds = 180.00
kilograms = pounds * .4535
print "%r pounds equals %r kilograms." % (pounds, kilograms)

# These are called string formatting operations
# %s acts as a placeholder for a string value
# %d acts as a placeholder for a numeric or decimal value
# The values for the above are passed in via a tuple
# %r calls the repr function while %s calls the str function. These may behave
# differently for some types but not for others.

# s = "spam"
# print(repr(s))
# 'spam'
# the repr function prints the offical string representation of an object,
# exactly as shown. If repr is used to calculate a value, you get a more precise
# result (more decimal values)
# print(str(s))
# spam
# In this case, the repr is the literal representation of a string
# (which the Python interpreter can parse into a str object),
# while the str is just the contents of the string.

t = 'I like Python'
x = 2
print "%s and I've been studying it for %d weeks." % (t, x)
print "%r and I've been learning it for %d days." % (t, x)

print round(1.73333) #the round function rounds the number up
