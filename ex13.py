from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

fourth = raw_input("Have anything else to add? ")

print "Your fourth variable is: %r" % (fourth)
