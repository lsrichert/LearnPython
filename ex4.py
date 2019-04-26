cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers/cars_not_driven
my_drivers = 10
most_traveled_to = 5



print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

print "I need", drivers, "cars today."
print "We have", cars, "cars available but only", space_in_a_car, "people will fit in each car."

print "I love", my_drivers, "a bunch."
print "We have", most_traveled_to, "destinations that people especially love."
print "I have", my_drivers, "drivers going to the city."

# The mistake Zeb made when he got the error was that he named the variable carpool_capacity,
# but when he called the variable, he added an extra underscore, i.e. car_pool_capacity.

i = 10
x = 1
j = 4
