name = 'Saeed Gatson'
age = 28
height = 77 # inches
weight = 215 # lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print "Let's talk about %s" % name
print "He's %d inches tall." % height
print "That's about %d centimeters." % (height * 2.54)
print "He's %d pounds heavy." % weight
print "That's about %f kilograms." % (weight * 0.45)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
