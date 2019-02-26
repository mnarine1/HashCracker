# Hash Cracker

Hash Cracker is a script that will find the orginal password for a given hashcode.


This project contains two python scripts: and brute-force method, and a optimized method.


## How to run hashCracker.py

hashCracker.py takes in the hashcodes through command line arguments. 

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
    
## How to run hashCrackerOpt.py

hashCrackerOpt.py is a more efficient script that decodes hashes.








## Assignment Results
