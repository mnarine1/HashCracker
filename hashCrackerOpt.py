import sys
import time
import hashlib

hashIn = ""
salt = ""
count = 0
list1 = open("passList.txt",'r')
res = ""
dict = {}

# Creates a dictionary that is populated with hashed passwords as the keys and the original passwords as the values
# The dictionary is created using a file with these key-value pairs
def makeDict():
    global dict
    fin = open('dict.txt', 'r')
    for line in fin:
    	dict[line.strip()[0:40]] = line.strip()[41:]
    print("\tReady")  # Prints "Ready" when the dictionary is finished loading

def getFromDict(h):
    global count
    count += 1
    if h in dict.keys():
        return dict[h]
    else:
        return ""

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
    makeDict() # load dictionary of hashes
    global count
	# Get starting time
    start = time.time()
    if len(sys.argv) == 1:			# if no arguments are given then ask for hashcode
        hashIn = raw_input("\tEnter hashcode: ").lower()
        start = time.time()			# reset start time to after the user has given an input
        print("\tChecking for Password...")
        res = getFromDict(hashIn)
    elif len(sys.argv) == 2:		# if a single hashcode is provided
        print("\tChecking for Password...")
        hashIn = sys.argv[1].lower()
        res = getFromDict(hashIn)
    elif len(sys.argv) >= 3:	# if 2 hashcodes are provided
        print("\tChecking For Salt...")
        hashIn = sys.argv[1].lower()
        salt = getFromDict(sys.argv[2].lower())
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

    ans = raw_input("Decode another hash? Y or N: ").upper()
    while ans == 'Y':
        count = 0
        hashIn = raw_input("\tEnter hashcode: ").lower()
        start = time.time()			# reset start time to after the user has given an input
        print("\tChecking for Password...")
        res = getFromDict(hashIn)
        if res != "":
            print("\tPassword: " + res)
        else:
            print("\tPassword Not Found")
        print("\tTime Elapsed: " + str(time.time() - start))
        print("\tNumber of Attempts: " + str(count))
        ans = raw_input("Decode another hash? Y or N: ").upper()

if __name__ == '__main__':
	main()

print("\n\tDone")
