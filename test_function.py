name = ""

def get_name():
	global name
	name = raw_input("What is your name? ")
	return name


def greeting():
	print "Hi, " + name

get_name()
greeting()