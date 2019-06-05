# Exercise 7: More Printing

# The line below prints the string.
print "Mary had a little lamb."
# If I replace the s with an r, it prints with the quotes (because it then
# prints in its 'raw' form).
# The line below prints the string and uses a formatter to insert string
# 'snow' inside the string.
print "Its fleece was white as %s." % 'snow'
# The line below prints the string.
print "And everywhere that Mary went."
print "." * 10 #what'd that do? This printed ten periods in a sort of line break.
# Similar to the above, this line prints 12 colons on a new line.
print ":" * 12

# Each of these lines declares values for the respective variables.
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
end13 = 'y'
x = 'Yes'
w = 'fantastic'
condition = 'cool'

# watch that comma at the end. try removing it to see what happens.
# If I remove that comma, Cheese and Burger print on two different lines.
# With the comma, they print on the same line, with a space between.

print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12
# I made this one up. It prints Cheese with a Y on the end and Then
# a question mark with the variable x, who's value is 'Yes'.
print end1 + end2 + end3 + end4 + end5 + end6 + 'y' + '?' + x
# Prints Cheesey
print end1 + end2 + end3 + end4 + end5 + end6 + end13
# Prints the string and uses the formatter to insert the word cats into
# the string. And then prints variable x, which is 'Yes'
print "Do we have three great %s?" % 'cats' + " " + x
print x
# Okay, so if I want to insert just a string with my formatter,
# I have to use quotes. If I want to insert a variable, no quotes.
print "Chicago is great because it is %s" % 'cool'
print "Chicago is great because it is %s" % condition
print "You really look %r!" % w
print 'You really look %s!' % w
print 'I am %d years old and my wife is %d.' % (40, 27)
print 'I am %d years old.' % 40
