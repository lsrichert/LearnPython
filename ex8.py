# Exercise 8: Printing, printing

formatter = "%r %r %r %r"
anotherFormatter = "%s %s"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
"I had this thing.",
"That you could type up right.",
"But it didn't sing.",
"So I said goodnight."
)
print formatter
# The below did not work because there aren't enough arguments.
# This is because formatter requires 4 arguments. I commented this out as a result.
### print formatter % ("Does this work?", "What about this?")
# However, once I changed the variable to something else and declared
# that variable as needing just two arguments, it worked.
print anotherFormatter % ("Does this work?", "What about this?")
print anotherFormatter
