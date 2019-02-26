# Hash Cracker
### Author: Michael Narine
#### Class: CSC 6980 - Blockchain & Applications

Hash Cracker is a python script that will find the orginal password for a given hashcode.


This project contains two python scripts:
* A brute-force method (**hashCracker.py**)
* A more efficient method (**hashCrackerOpt.py**)


## How to run *hashCracker.py*

*hashCracker.py* takes in the hashcodes through command line arguments. If there are no command line arguments, then the user is prompted to enter a hashcode to be decoded. If there is one argument, then the script will find the password without using a salt term. If there are two arguments, then the script will find the salt term given through the second argument, and prepend the decoded salt term to each password in *passList.txt* to find the decoded salted hash.

To find the original password of a given unsalted hash, use the command:

	python hashCracker.py hashcode

*Example:*

	python hashCracker.py 049fb98932d97ceb9c08e87d9e420c8fbd1294de

*Returns:*

	Checking for Password...
	Password: buster02
	Time Elapsed: 1.57800006866
	Number of Attempts: 612608
	Done

If the given hashcode is salted and the salt term is known, use the command:

	python hashCracker.py hashcode salt_term

*Example:*

	python hashCracker.py ece4bb07f2580ed8b39aa52b7f7f918e43033ea1 f0744d60dd500c92c0d37c16174cc58d3c4bdd8e

*Returns*

	Checking For Salt...
	Salt: slayer
	Checking for Password...
	Password: harib
	Time Elapsed: 1.07600021362
	Number of Attempts: 546155
	Done
    

## How to run *hashCrackerOpt.py*

hashCrackerOpt.py is a more efficient script that decodes hashes.

In this script, a dictionary is created from passList.txt, where the hashed password if the key and the original password string is the value. Once the dictionary is created, the script will execute different functions based on the number of arguments. If there are no command line arguments, then the user is prompted to enter a hashcode to be decoded. If there is one argument, then the script will find the password without using a salt term. If there are two arguments, then the script will find the salt term given through the second argument, and prepend the decoded salt term to each password in *passList.txt* to find the decoded salted hash.

To find the original password of a given unsalted hash, use the command:

	python hashCrackerOpt.py hashcode

*Example:*

	python hashCrackerOpt.py 049fb98932d97ceb9c08e87d9e420c8fbd1294de

*Returns:*

	Ready
        Checking for Password...
        Password: buster02
        Time Elapsed: 0.0780000686646
        Number of Attempts: 1

If the given hashcode is salted and the salt term is known, use the command:

	python hashCrackerOpt.py hashcode salt_term

*Example:*

	python hashCrackerOpt.py ece4bb07f2580ed8b39aa52b7f7f918e43033ea1 f0744d60dd500c92c0d37c16174cc58d3c4bdd8e

*Returns*

	Checking For Salt...
        Salt: slayer
        Checking for Password...
        Password: harib
        Time Elapsed: 1.04600000381
        Number of Attempts: 546155


## Assignment Results

The results from the assignment's test cases are listed below:

##### Part A)	**b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3**
###### *hashCracker.py*

	python hashCracker.py b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3

    	Checking for Password...
	    Password: letmein
    	Time Elapsed: 0.00600004196167
    	Number of Attempts: 16
        Done

###### *hashCrackerOpt.py*

	python hashCrackerOpt.py b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3
    
    	Ready
        Checking for Password...
        Password: letmein
        Time Elapsed: 0.125
        Number of Attempts: 1
 
##### Part B)	**801cdea58224c921c21fd2b183ff28ffa910ce31**
###### *hashCracker.py*

	python hashCracker.py 801cdea58224c921c21fd2b183ff28ffa910ce31

    	Checking for Password...
        Password: vjhtrhsvdctcegth
        Time Elapsed: 2.50200009346
        Number of Attempts: 999968
        Done

###### *hashCrackerOpt.py*

	python hashCrackerOpt.py 801cdea58224c921c21fd2b183ff28ffa910ce31
    
    	Ready
        Checking for Password...
        Password: vjhtrhsvdctcegth
        Time Elapsed: 0.077999830246
        Number of Attempts: 1

##### Part C)	**ece4bb07f2580ed8b39aa52b7f7f918e43033ea1**
##### Salt Term = **f0744d60dd500c92c0d37c16174cc58d3c4bdd8e**
###### *hashCracker.py*

	python hashCracker.py ece4bb07f2580ed8b39aa52b7f7f918e43033ea1 f0744d60dd500c92c0d37c16174cc58d3c4bdd8e

    	Checking For Salt...
        Salt: slayer
        Checking for Password...
        Password: harib
        Time Elapsed: 1.53699994087
        Number of Attempts: 546155
        Done

###### *hashCrackerOpt.py*

	python hashCrackerOpt.py ece4bb07f2580ed8b39aa52b7f7f918e43033ea1 f0744d60dd500c92c0d37c16174cc58d3c4bdd8e
    
    	Ready
        Checking For Salt...
        Salt: slayer
        Checking for Password...
        Password: harib
        Time Elapsed: 1.59000015259
        Number of Attempts: 546156
