import sys

def hashStr(string):
	stri = [ord(char) for char in string]
	rval = ""
	# print(ascii_values)
	for value in stri:
		rval = rval + str(value * 5)
	return rval

print(hashStr(str(sys.argv[1])))
