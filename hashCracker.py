# Michael Narine
# CSC 6980
# Blockchain & Applications
# Assignment 2
# February 25, 2019

import sys
import time
import hashlib

hashIn = ""
salt = ""
count = 0
list1 = open("passList.txt",'r')
res = ""

# Checks for password in the list and returns the result
def simple(hash):
	result = ""
	global count
	for line in list1:
		count += 1
		h = hashlib.sha1()
		temp = line.strip()
		h.update(temp)
		if h.hexdigest() == hash:
			result = temp
			break
	return result

# Checks for a password in the list if a salt term is provided
def findWithSalt(s, hash):
	result = ""
	global count
	for line in list1:
		count += 1
		h = hashlib.sha1()
		temp = line.strip()
		h.update(s+temp)
		if h.hexdigest() == hash:
			result = temp
			break
	return result



def main():
	# Get starting time
	start = time.time()
	if len(sys.argv) == 1:			# if no arguments are given then ask for hashcode
		hashIn = raw_input("\tEnter hashcode: ").lower()
		start = time.time()			# reset start time to after the user has given an input
		print("\tChecking for Password...")
		res = simple(hashIn)
	elif len(sys.argv) == 2:		# if a single hashcode is provided
		print("\tChecking for Password...")
		hashIn = sys.argv[1].lower()
		res = simple(hashIn)
	elif len(sys.argv) >= 3:	# if 2 hashcodes are provided
		print("\tChecking For Salt...")
		hashIn = sys.argv[1].lower()
		salt = simple(sys.argv[2].lower())
		if salt != "":
			print("\tSalt: " + salt)
			print("\tChecking for Password...")
			res = findWithSalt(salt, hashIn)
		else:
			print("\tSalt not found")
			res = simple(hashIn)

	if res != "":
		print("\tPassword: " + res)
	else:
		print("\tPassword Not Found")
	# Print the time it took to get a result
	print("\tTime Elapsed: " + str(time.time() - start))
	print("\tNumber of Attempts: " + str(count))


if __name__ == '__main__':
	main()

print("\n\tDone")
