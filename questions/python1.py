#------------------------------------------------------------------------------------------------------------------------------------------------------------------ 

	# INSTRUCTIONS

	# In case it is not clear, the Question appears first, then examples, then any hints and finally the function that you need to complete appears underneath:
	#
	# 	<QUESTION>
	#
	# 	<EXAMPLES>
	#
	# 	<HINT>

	# You are allowed access to the internet for this assessment, but remember you could use the DOCUMENTATION that comes bundled with your Python installation. 
	# Every command has help documentation. To read it:
	# 	1. Access Python from your CLI
	# 	2. Type help(<command>) and hit enter, where <command> is the command you want help with. For example: help(str)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------ 

	# <QUESTION 1>

	# Define a function that can accept two strings as input and returns the string with maximum length to the console. 
	
	# If two strings have the same length, then the function should return both strings separated by a " ".

	# In this case, the strings should be returned in the same order in which they were given.

	# <EXAMPLES>

	# one("hi","hello") → "hello"
	# one("three", "two") → "three"
	# one("three", "hello") → "three hello"

	# <HINT>

	# What was the name of the function we have seen to check the length of a container?  Use your CLI to access the Python documentation and get help(len).

def one(input1, input2):
	len1 = len(input1)
	len2 = len(input2)
	if len1==len2:
		solution = input1 + ' ' + input2
	elif len1>len2:
		solution = input1
	elif len2>len1:
		solution = input2
	return solution

#------------------------------------------------------------------------------------------------------------------------------------------------------------------ 

	# <QUESTION 2>

    # given a number
	# if this number is divisible by 3 return "fizz"
	# if this number is divisible by 5 return "buzz"
	# if this number is divisible by both 3 and 5 return "fizzbuzz"
	# if this number is not divisible by 3 or 5 return "null"
	    
    # <EXAMPLES>

	# two(3) → "fizz"
	# two(10) → "buzz"
	# two(15) → "fizzbuzz"
	# two(8) → "null"

	# <HINT>

	# No hints for this question

def two(arg1):
	if arg1 % 15 == 0:
		solution = 'fizzbuzz'
	elif arg1 % 3 == 0:
		solution = 'fizz'
	elif arg1 % 5 == 0:
		solution = 'buzz'
	else:
		solution = 'null'
	return solution

#------------------------------------------------------------------------------------------------------------------------------------------------------------------ 

	# <QUESTION 3>

    # Write a function which returns the integer number of vowels in a given string. 
    # You should ignore case.

	# <EXAMPLES>

    # three("Hello") → 2
    # three("hEelLoooO") → 6

	# <HINTS>

	# How do we ignore case in a String? help(str) may offer some insight.

def three(input):
	input = input.lower()
	vowel_total = 0
	for letter in 'aeiou':
		vowel_total += input.count(letter)
    
	return vowel_total

#------------------------------------------------------------------------------------------------------------------------------------------------------------------ 

	# <QUESTION 4>

    # There is a well known mnemonic which goes "I before E, except after C", which is used to determine which order "ei" or "ie" should be in a word.
    
    # Write a function which returns the boolean True if a string follows the mnemonic, and returns the boolean False if not.

	# <EXAMPLES>

    # four("ceiling") → True
    # four("believe") → True
    # four("glacier") → False
    # four("height") → False

	# <HINT>

	# Step through the logic here in order to solve the problem, you may find help(range) helpful.


def four(input):
	for index in range(len(input)-1):
		if 'c' in input:
			c_index = input.index('c')
			return 'ei' == input[c_index+1:c_index+3]
		elif 'ie' in input:
			return True
		elif 'ei' in input:
			return False
#------------------------------------------------------------------------------------------------------------------------------------------------------------------ 

	# <QUESTION 5>

	# Write a function which takes an input (between 1 and 10 inclusive) and multiplies it by all the numbers before it.
	# eg If the input is 4, the function calculates 4x3x2x1 = 24 

	# <EXAMPLES>

	# five(1) → 1
	# five(4) → 24
	# five(8) → 40320

	# <HINT>

	# You may need to create a list of numbers from 0 to i, take a look at help(range).

def five(input):
	total = 1
	for num in range(1, input+1):
		total *= num 
	return total
#------------------------------------------------------------------------------------------------------------------------------------------------------------------ 

	# <QUESTION 6>

    # Given a string, int and a char, return a boolean value if the 'nth' 
    # (represented by the int provided) char of the String supplied is the same as the char supplied.
    # The int provided will NOT always be less than than the length of the String.
    # IGNORE case and Whitespace. 
    
    # <EXAMPLES>

	# six("The",2,'h') → True
	# six("AAbb",1,'b') → False
	# six("Hi-There",10,'e') → False

	# <HINT>

	# How do we find the length of a container, take a look at help(len), you will also need to look at help(str) for String manipulation.
 
def six(string, int, char):
	string = string.lower()
	string = string.replace(' ','')

	if int > len(string):
		return False
	return string[int-1] == char

#------------------------------------------------------------------------------------------------------------------------------------------------------------------ 

	# <QUESTION 7>

    # Given a string and a char, returns the position in the String where the char first appears.
    # Ensure the positions are numbered correctly, please refer to the examples for guidance.
    # DO NOT ignore case
    # IGNORE whitespace
    # If the char does not occur, return the number -1.
    
    # <EXAMPLES>

	# seven("This is a Sentence","s") → 4
	# seven("This is a Sentence","S") → 8
	# seven("Fridge for sale","z") → -1

	# <HINT>

	# Take a look at the documentation for Strings, List and range.

def seven(inputString, char):
	seven_nospace = inputString.replace(' ','')
	if char not in seven_nospace:
		return -1
	else:
		position = seven_nospace.index(char)+1
	return position

#------------------------------------------------------------------------------------------------------------------------------------------------------------------ 

	# <QUESTION 8>

    # Given a string seperate the string into the individual numbers present, then add each digit of each number to get a final value for each number

	# String example = "55 72 86"
	
	# "55" will = the integer 10
	# "72" will = the integer 9
	# "86" will = the integer 14
	
	# You then need to return the highest value, in the example above this would be 14.
	 
    # <EXAMPLES>

	# eight("55 72 86") → 14
	# eight("15 72 80 164") → 11
	# eight("555 72 86 45 10") → 15

	# <HINT>

	# help(int) for working with numbers and help(str) for working with Strings.

def eight(arg1):
	numbers = arg1.split()
	total = []
	for num in numbers:
		num_list = list(num)
		for i in range(len(num_list)):
			num_list[i] = int(num_list[i])
		add = sum(num_list)
		total.append(add)

	return max(total)

print(eight("55 72 86"))

#------------------------------------------------------------------------------------------------------------------------------------------------------------------ 

	# <QUESTION 9>

    # Return the string that is between the first and last appearance of "bert" in the given string
	
	# Return the empty string "" if there is not 2 occurances of "bert" 
	
	# IGNORE CASE
    
    # <EXAMPLES>

	# nine("bertclivebert") → "clive"
	# nine("xxbertfridgebertyy") → "fridge"
	# nine("xxBertfridgebERtyy") → "fridge"
	# nine("xxbertyy") → ""
	# nine("xxbeRTyy") → ""

	# <HINT>

	# What was the name of the function we have seen to seperate a String? How can we make a string all upper or lower case?
	
	# Use your CLI to access the Python documentation and get help manipulating strings - help(str).

def nine(input):
	return ""

#------------------------------------------------------------------------------------------------------------------------------------------------------------------ 

	# <QUESTION 10>

    # Given a large string that represents a csv, the structure of each record will be as follows:
    
    # owner,nameOfFile,encrypted?,fileSize
    
    # "Bert,helloWorld.py,True,1447,Bert,strings.py,False,1318,Jeff,dice.py,False,1445"
    
    # For each record, if it is not encrypted, return the names of the owners of the files in a String Array.
    # Do not include duplicate names.
	# If all records are encrypted, return an empty Array.
    
    # <EXAMPLES>
    
    # ten("Jeff,random.py,False,1445") → ["Jeff"]
	# ten("Bert,numberGen.py,True,1447,Bert,integers.py,True,1318,Jeff,floats.py,False,1445") → ["Jeff"]
	# ten("Bert,boolean.py,False,1447,Bert,conditions.py,False,1318,Jeff,loops.py,False,1445") → ["Bert","Jeff"]
    # ten("Bert,prime.py,True,1447,Bert,ISBN.py,False,1318,Jeff,OOP.py,False,1445") → ["Bert","Jeff"]
    
	# <HINT>

	# Dont't forget, False is a String, not a Boolean value in the Tests above.

	# help(str) and help(list), you might also need to use a function that can create a list of numbers for you, try help(range).

def ten(input):
	return []

#------------------------------------------------------------------------------------------------------------------------------------------------------------------ 

