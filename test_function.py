def get_name():
	global name
	name = raw_input("What is your name? ")
	return name


def greeting():
	name = get_name()
	print "Hi, " + name

greeting()