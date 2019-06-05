# Exercise 6: Strings and Text

# The below line defines the variable 'x'and the % tells the program what value
# to assign the % within the string/variable that we're calling.
# The line below that defines the variable 'binary'
# The line below that defines the variable 'do_not'
# The line below that defines the varialbe 'y' and tells the program what values
# to assign the % when calling that variable.

x = "There are %d types of people." %10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
# The line below prints variable 'x'
# The line below that prints variable 'y'
print x
print y
# The line below prints the string and tells the program to print 'x' in place
# of the %. X is above.
# The line below that prints the string and tells the program to print variable 'y'
# in place of the %. It also tells the program to put single quotation marks around
# the printed string.
print "I said: %r." % x
print "I also said: '%s'." % y
# Here we've assigned 'False' to variable hilarious.
# Then we've assigned a string to variable joke_evaluation
hilarious = True
joke_evaluation = "Isn't that joke so funny?! %r"
# Here we're printing the variable joke_evaluation and assigning 'hilarious'
# to the % within that string.
print joke_evaluation % hilarious
# We assigned a string to the variable 'w'.
# Then we assigned a string to variable 'e'.
w = "This is the left side of..."
e = "a string with a right side."
# We are printing variable 'w' and right next to it, variable 'e'.
print w + e

z = "I love cubs"
f = 3
print "I just want to scream %r %d times." % (z, f)
