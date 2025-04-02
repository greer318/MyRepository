### script mode
### - you'll write your code here
##
### comments
###  - created with a #
###  - line is ignored by the computer
##
### Numerical Data Types
### - integers: whole numbers
###    78   0   -6876
##
### - floating point numbers: decimal numbers
###   0.56546   0.0   987635.887
##
### Mathematical Operators (high to low precedence)
###  **   exponent
###  *    multiplication,   /   division (floating point)
###  +    addition,         -    subtraction
##
### data types in calculations
##
### for most operators, using 2 integers will result in
### an integer
##
###  10 * 3 = 30    7 + 4 = 11
##
### for / the result is always a floating point number
##
###   10 / 2 = 5.0
##
### for ALL operators, using 2 floating point numbers or
### using an integer and a floating point number results
### in a floating point number
##
###   10.0 * 3 = 30.0     7.0 + 4.0 = 11.0
##
### Abbreviations:
### integers = ints
### floating point numbers = floats
##
### print function    print()
### - displays data to the screen
### - can display one or more values
### - can display any data type
##
####print(159)
####print(4.5, 76.182)
##
###print("Birth Year:", 2025-35)
### print(24, -1)
##
## 
### functions
### every function:
### - has a name that must be exact same as Python
### - has (); where you give data to the function
##
### variables
### - store a single piece of data
### General format
###  variableName = value
##
### Naming Rules
### - first character: _  or letter (lowercase)
### - all others: _, letters, numbers
### - can't use keywords: they turn orange
### - need to be descriptive
###   - use camel case or underscores
##
### variable for the current
##
####currentYear = 2025   # camel case
####current_year = 2025  # underscores
####
####count1 = 0
####count2 = 0
####total = 0
####
####print(count)
####
####count = count + 1
####total = count + total
####
####print(count, total)
##
##
##
##
##
##
##
####print(25 / 5 + 2 - 6)
####print(7 ** 3 - 100 * 2)
####print(8 + 2 * 3 - 7)
####print(100 * 4 / 20 + 45 - 8)
##
##
##
##
##
##
####print(1)
####print(29)
####print(2025)
####print()
####print(1, 29, 2025)
##
##
##
##
##
### Display year you're born using current year and
### age
##
###print(2025 - 35)
##
### with variables
##
####currentYear = 2025
####age = 35
####
####birthYear = currentYear - age
####
####print(birthYear)
####
####print("Year:", currentYear)
##
### Math Functions
##
### absolute value function   abs()
### - calculate the absolute value
##
### general format
### variable = abs(number)
##
####result = abs(-24)
####
####result2 = abs(-8) * 20
#####       = 8 * 20
#####       = 160
####
####print(abs(-78))
### print(78)
### 78
##
##
##
### integer function   int()
### - converts a value into an integer
##
### general format
### variable = int(value)
##
####result = int(4.99999999)
####
####print(result)
##
### round function   round()
### - rounds numbers
##
### round using 1 number
### - rounds to nearest whole number as an int
##
####result = round(46.897987978)
####
####print(result)
##
### round using 2 numbers
### - rounds to a specified decimal place as a
###   float
##
### general format
### variable = round(number, decimal place)
##
##
####result = round(46.897987978, 3)
####
####print(result)
####
####result2 = round(46.897987978, 0)
####
####print(result2)
####
####result = round(46.897987978, 30)
####
####print(result)
##
##
##
##
### augmented assignment statments
### - used to shorten equations with out changing
###   the calculation
##
####count = 0
####num = 10
####
####count = count + 1 + num
####
####count += 1 + num
####
####print(count)
##
### integer division   //
### - divides 2 numbers and results in the whole
###   number value only as an int
##
### modulus    %    <---- percent sign
### - divides 2 numbers and result in the remainder
###   as an int
##
##
### Errors
##
### syntax errors
### - problem with your grammar
### - incorrect punctuation
### - using a keyword as a variable
##
####print(23, 45)
####print(123)
####
####while = 456
##
### runtime error
### - occur when the program is running
### - divide by 0
##
### - mispelled a name
###print(123 / 0)
##
### logic error
### - problem with your logic
### - the output doesn't match what you expected
##
####result = (40 + 70) / 2   # average
####
####print(result)
##
### Strings
### - data type that can consist any valid character
### - data in the string is surrounded by quotation
###   marks
###         ""    or   ''
##
### - a string is a sequence of characters
##
##name = "Tyler"
##
###print(name)
##
##
### indexing
### - gets access to one character in the string
### - based on the string's indicies
###   - the location of the characters
###   - first index is ALWAYS 0
##
### general format
###    string[index]
##
####letter = day[0]    # get the 'M'
####
####print(letter)
####
####print(day[5])    # display the 'y'
####
####print(day)
##
### slicing
### - gets multiple characters from a string
##
### general format
###   string[start index : end index + 1]
##
###      0123456789     <--- indicies 
####day = "Monday 3rd"
####
####print(day[0:3])    # Mon
####
####print(day[3:8])    # day 3
####
####print(day[7:10])    # 3rd
####
##
### methods
### - similar to functions in that they perform a
###   task
### - only works with a certain data type
##
### general format
###    string.method()
###       string is what the method is working with
##
##
### stringA.find(stringB)
### - search stringA starting at index 0
### - tells the start index of stringB
##
### stringA.rfind(stringB)
### - searches stringA starting at last index
### - gives the index of the last instance of
###   stringB
##
###        012345678910
##state = "Mississippi"
##
### find the last 'i'
####index = state.rfind('i')
####print(index)
####
##### find ippi
####index = state.find('ippi')
####print(index)
####
##### find MISS, doesn't exists, returns -1
####index = state.find('MISS')
####print(index)
##
##
### negative indices
### - last character's index is ALWAYS -1
##
### default bound
### - leave the start or the end index empty
##
####day = "Monday"
####
####print(day[-3: ])  # day
####
####print(day[ :-2])  # Mond
##
### empty string:  ""
##
### concatenation
### - adds 2 strings together to create a single
###   string
### - only works with strings
##
### general format
###   stringA + stringB
##
####color = "blue"
####
####result = color + " " + "green" + str(100)
####
####print(result)
##
### string function   str()
### - converts data type to a string
##
##
##
##
##
##
### repetition    *
### - repeats a string and concatenates it together
###   a specified number of times
##
### general format
###    string * int
##
####color = "blue"
####
####result = (color + " ") * 5
####
####print(result)
##
### precedence high to low
###  repetion
###  concatenation
##
##
##
##
##
##
##
##
##
### len function     len()
### - determines number of characters in a string
###   - including whitespace
##
####word = "Wednes day"
####
####length = len(word)
####
####print(length)
##
### input function   input()
### - gets input from the user
###   - input is always a string
##
### general format
###    variable = input(prompt)
##
##### get user's first name
####firstName = input("Enter your first name: ")
####
##### get user's age
####age = int(input("Enter your age: "))
####
####age = int(age)
####                 
##### get a price
####price = float(input("Enter a price: "))
####
####
####print()
####print(firstName, int(age) + 10, price * 4)
##
##
##
### Program: Gets full name from user, displays
###  the last name by itself, then displays all
###  other names on the line below
####
#####   Tyler Rene' Greer
####
##### get name from user
####name = input("Enter full name: ")
####
##### find last space
####spaceIndex = name.rfind(' ')
####
##### slice the last name from the full name
####lastName = name[spaceIndex + 1: ]
####
##### slice the rest of the names from full name
####otherNames = name[0:spaceIndex]
####
####print(lastName)
####print(otherNames)
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
### string methods
##
### string.upper()
### - gives you a string with all letters
###   capitalized
##
### string.lower()
### - gives you a string with all letters made
###   lowercase
##
### stringA.count(stringB)
### - tells number of times stringB appears in
###   stringA
##
####print(date.count('e'))    # 2
####print(date.count('day'))  # 1
####print(date.count('A'))    # 0
##
### string.capitalize()
### - Makes index 0 of the string uppercase
### - everything else is lowercase
##
### string.title()
### - make the first letter of each word uppercase
### - everything else is lowercase
##
### word: is anything separated by whitespace
###   "hello 2343 !!!!!"   <--- 3 words
##
####date = "wednesDAY 5th, #csci"
####
####print(date.title())
##
### string.rstrip()
### - removes whitespace from the end of a string
##
####word = " AB  C       "
####
####print(word + '!')
####print(word.rstrip() + '!')
##
##
### print(round(4.3978)) # nesting functions
##
### chaining methods
##
####praise = "Good dog".upper()
####numGs = praise.count('G')
####
##### chained version
####numGs = "Good dog".upper().count('G')
#####     = "GOOD DOG".count('G')
#####     = 2
####
####print(numGs)
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
####print(date.capitalize())
####
####date = "123wednesDAY 5th"
####
####print(date.capitalize())
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
### get sentence
####sentence = input("Enter a sentence: ")
####
####upperSent = sentence.upper() # make all letters uppercase
####
##### count number of individual vowels
####a_count = upperSent.count('A')
####e_count = upperSent.count('E')
####i_count = upperSent.count('I')
####o_count = upperSent.count('O')
####u_count = upperSent.count('U')
####
####print()
####print(sentence)  # display original sentence
####
##### display all vowel counts
####print()
####print("A =", a_count)
####print("E =", e_count)
####print("I =", i_count)
####print("O =", o_count)
####print("U =", u_count)
##
##
##
##
##
### evaluation function    eval()
### - converts strings to number
### - can solve expressions within a string
###     "4 + 8 / 2"
### - ONLY works with strings
##
####num = eval("123")
####
####print(num * 3)
####
####num = eval("12.78")
####
####print(num * 3)
####
####result = eval("4 + 7 * 3")
####
####print(result)
##
##
### Ch. 2.3
##
### sep argument
### - a variable
### - only stores strings
### - only used in print()
###   - changes what is displayed between each
###     piece of data in print()
###     - default is " "
### - always at the end of the print
##
####print(1,2,3, sep = ", ")
####
####print(1,2,3, sep = " + ")
####
####print(1,2,3, sep = " and ")
####
####print(1,2,3)
##
### end argument
### - a variable
### - only stores strings
### - always at the end of the print()
### - changes what's displayed after all of the
###   data is displayed
###   - default is "\n"
##
####print(1,2,3, sep = "&", end = " ==== ")
####print(4,5,6, end = " or ", sep = "")
####print(7,8,9)
##
##
### escape sequences
### - commands
### - all start with a   \
##
### newline character    "\n"
### - tells cursor to move to next line
##
###print("A\nB\n\nC")
##
### tab character    "\t"
### - moves cursor to the right some number of
###   spaces
### - by default, tab moves the cursor in
###   increments of 8
##
####print("1234567812345678")
####print("\tABC")
####print("AB\tC")
####print("ABBBBBB\tC")
####print("ABBBBBBBB\tC")
##
##
####print("1\\2\\3")
####
####print("\"hello\"")
####
####print('Rene\'')
####
####print('"hello"')
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
### Ch. 2.3 continued
##
### expandtabs
### - change the amount of space \t creates
##
####print("1234567812345678")
####print("\tABC")
####print("\tABC".expandtabs(3))
####print("\tABC".expandtabs(15))
##
### string.format()
### - creates formatted strings
##
### general format
###   "string containing format info".format(data)
###    - data can by any data type
##
### how to format
### - {} indicate that it's how the string should
###      be formatted
##
### format specifier general format
###    {index:how to format}
##
### index: index of the data listed in ()
##
### how to format
### - justification
###   >   right
###   <   left
###   ^
##
### space reserved for one piece of data
###  - an int
##
### data type
###   d  integer
###   f  float
###   s  string
##
####result = 5 + 7 \
####* 9 
####
####result = (5 + 7
####          * 9)
####
####
####
##### index:                                 0    1      2
####print("|{0:^10d}|{1:>5s}|{2:<8.2f}|".format(17, "cat", 2.3))
####
##
##
####print("|{0:<10d}|".format(17, 2.3))
####print("|{0:>10d}|".format(17, 2.3))
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
### Ch. 3.1
##
### Relational Operators
### - always produces True or False as the result
### - used to create conditions for decision and
###   repetition structures
##
### <   less than
### >   greater than
### <=  less than/equal to
### >=  greater than/equal to
### ==  equal to
### !=  not equal to
##
### CANNOT COMPARE NUMBERS AND STRINGS
##
### only strings:
##
### in   checks is stringB is in stringA
###          stringB in stringA
##
### not in  checks if stringB not in stringA
###          stringB not in stringA
##
##
### Operator Precedence High to Low
### - Mathematical operators
### - Relational operators
##
##
####print(4 * 6 < 12 + 2)
###     24 < 12 + 2
###     24 < 14
###      False
##
### comparing strings
##
### ASCII
### - numerical representation for each character
##
### MEMORIZE THESE ASCII VALUES!!!
### "A" is 65
### "a" is 97
##
####print("cat" < "car")
#####       "c" < "c"
#####       "a" < "a"
#####       "t" < "r"
#####          False
####
####
####print("cat" < "dog")
#####       'c' < 'd'
#####        99 < 100
#####         True
####
####print("Cat" < "dog")
###       "C" < "d"
###        67 < 100
##
### character function   chr()
### - convert an int into its ASCII character
##
####print(chr(78))
####print(chr(9456))
####
##### ord()
##### - converts a single character into to the int
#####   ASCII value
####
####print(ord('w'))
##
##
##
##
##
##
##
##
##
##
##
##
### Logical Operators
### - used to create more complex conditions
### - only work with True and False
### - result is always True or False
##
### and operator
### - used to check if both conditions are True
### - result will True only if BOTH conditions
###   are True
##
### want to check if a number is positive and even
####num = 10
####
####print(num > 0 and num % 2 == 0)
#####        T    and   T
#####             T
####
##### or operator
##### - result is True if at least one condition is
#####   True
####
##### want to check if the number is positive or
##### even
####num = 15
####
####print(num > 0 or num % 2 == 0)
#####        T    or   F
#####             T
##
### not operator
### - changes the truth value
###   - if True, result is False
###   - if False, result is True
##
##num = -4
##
### want to check if num is not positive
###print(not (num > 0))
###     not (F)
###      T
##
### Logical Operator Precedence High to Low
###  not
###  and
###  or
##
##True or not(False) and True
##True or True       and True
##True or True
##True
##
### Operator Precedence High to Low
### - math operators
### - relational operators
### - logical operators
##
##
### boolean data type
### - only consist of True and False
##
####result = 4 < 10
####
####print(result)
##
##
### isinstance()
### - checks the data type of a value
##
### general format
###   isinstance(value, data type)
##
####value = 45.6
####
####print(isinstance(value, str))
####print(isinstance(value, float))
####print(isinstance(value, int))
####print(isinstance(value, bool))
##
### stringA.startswith(stringB)
### - checks if stringA starts with stringB
##
####print("Wednesday".startswith("Wed"))
####print("Wednesday".startswith("Mon"))
####
#### stringA.endswith(stringB)
#### - checks if stringA ends with stringB
####
####print("February".endswith("ry"))
####print("July".endswith("ry"))
##
### string.isdigit()
### - checks if all characters are digits
###   - True only if all of them are digits
##
####print("123".isdigit())
####print("-123".isdigit())
####print("12 3".isdigit())
##
### string.isalpha()
### - check if all characters are letters upper or
###   lowercase
###   - True if all letters
##
####print("abcABC".isalpha())
####print("abc ABC".isalpha())
##
##
### string.isalnum()
### - checks for letters and/or digits
###   - True if all letters
###   - True if all digits
###   - True if all letters and digits
##
####print("abc123".isalnum())
####print("abc".isalnum())
####print("123".isalnum())
####print("abc 123".isalnum())
####print("abc,@#$123".isalnum())
##
### string.isupper()
### - checks if all letters are uppercase
###   - True if all uppercase
##
####print("ASD345><<".isupper())
####print("ASD345><<ffff".isupper())
##
### string.islower()
### - checks if all letter are lowercase
###   - True if all lowercase
##
####print("asd345><<".islower())
####print("ASD345><<ffff".islower())
##
### string.isspace()
### - checks if all characters are whitespace
###   characters
##
####print("     ".isspace())
####print("\n\t".isspace())
####print("  sdf  ".isspace())
##
##
### short circuit evaluation
### - when using and operator and or operator,
###   sometimes only the first condition is
###   evaluated
##
####True or False
####    True
####
####4 > 0  or  47 < 13
####True  or
####True
##
####num = 0
####
####print(num != 0 and  47 < 13 / num)
####False and
####False
##
##
##
##
##
##
##
##
##
##
### Ch. 3.2: Decision Structures
##
### if/else statement
### - 2 options
### - if represents the True path
### - else represents the False path
##
### general format
##
####if condition(s):   # if header
####
####    # indented code for the True path
####    # area is the if body
####
####else:  # else header
####
####    # indented code for the False path
####    # area is the else body
##
##
####menu = input("Enter Lunch or Dinner: ")
####
####if menu == "Lunch":
####    print("Lunch Menu")
####
####    price = 5.00
####
####else:
####    print("Dinner Menu")
####
####    price = 10.00
####
####print("Price:", price)
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
####num = eval(input("Enter a number: "))
####
####if num < 0 or num > 20:
####    print("hello")
####else:
####    print("goodbye")
####
####
####name = input("Enter your name: ")
####
####if name[0].isupper() and len(name) >= 5:
####    print("blue")
####else:
####    print("green")
##
### if statement
### - 1 option
##
### does user get a discount. 50 or more gets one
##
####total = 43
####
####if total >= 50:
####    print("discount!!!")
####
####print(total)
##
##
##
##
### nested decision structures
### - any number options
##
##
### if/elif/else statement
### - any number of options
### - combines the else and if step
##
####menu = input("Enter Breakfast, Lunch, or Dinner: ")
####
####if menu == "Lunch":
####    print("Lunch Menu")
####elif menu == "Dinner":
####    print("Dinner Menu")
####elif menu == "Brunch":
####    print("Brunch Menu")
####else:
####    print("Breakfast Menu")
##
### Ask user for a number
### Using if/elif/else display if a number is
### positive, negative, or zero
##
### Step 2:
### Ask user to enter their name.
### Using if/elif/else display if their name starts
### with letter A - E, F - N, or O - Z.
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
####num = eval(input("Enter a number: "))
####
####if num > 0:
####    print("Positive")
####elif num < 0:
####    print("Negative")
####else:
####    print("Zero")
####
####
####name = input("Enter name: ")
####
####letter = name[0]
####
####if letter >= "A" and letter <= "E":
####    print("A - E")
####elif letter >= "F" and letter <= "N":
####    print("F - N")
####else:
####    print("O - Z")
##
##
##
##
##
### Ch. 3.3: While loops
##
### while loops
### - allow us to repeat code
### - make programs more flexible
### - still uses conditions like the decision
###   structures
##
### general format
##
###while condition(s):
##
##    # indented code that repeats while the
##    # condition is True
##
### display "blue" 5 times
##
### loop variable: variable tested in loop header
##
### display the sum of 1 - 5
##
####count = 1
####spaces = ""
####
####while count <= 50:  
####
####    if count % 3 == 0:
####        print(spaces, count, sep = "")
####        spaces += " "
####
####    count += 1    
##
##
### controling loop with user input
##
### ask the user for their favorite colors
##
##
####again = "y"
####
####allColors = ""  # store all colors from user
####
####while again != 'n': 
####    color = input("Enter favorite color: ")
####
####    allColors = allColors + color + "\n"
####
####    again = input("Enter another color? (y/n): ")
####
####    print()
####
####print(allColors)
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
####numFav = int(input("Enter number of favorite foods: "))
####print()
####
####count = 0
####favFoods = ""
####
####while count < numFav:
####
####    food = input("Enter one food item: ")
####
####    favFoods += " - " + food + "\n"
####    
####    count += 1
####
####header = "Your Top " + str(numFav) + " Foods"
####
####print("\n" + header)
####print("=" * len(header))
####
####print(favFoods)
##
##
##
### input validation
### - check the data the user gives us before we
###   use it in our code
###   - if data is invalid, user must re-enter it
### - only done with while loop
###   - check if data is incorret
##
##### ask user for number 1 - 10
####num = int(input("Enter a number 1 - 10: "))
####
##### input validation: must be 1 - 10
####while num < 1 or num > 10:
####    num = int(input("Error! Enter a number 1 - 10: "))
####
##### display number
####print(num, "is from 1 - 10")
##
### get color from user
####color = input("Enter color (BLUE or RED): ")
####
####color = color.upper()
####
##### input validation: can only be BLUE or RED
#####while color != 'RED' and color != "BLUE":
####
####while not(color == "RED" or color == "BLUE"):
####    color = input("Error! Enter color (BLUE or RED): ")
####
####
####
##### display color
####print("Color:", color)
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##### indexing strings with a while loop
####
####state = "Mississippi"
####
####length = len(state)
####
####index = 0   # tracks current index
####
####while index < length:
####
####    if state[index].isupper():
####        print(state[index])
####
####    index += 1
##
##
##
##
##
##
##
##
##
##
### sentinels
### - a value
###   - value to indicate loop should stop
### - sentinel is entered in same input as actual
###   data
### - sentinel must be unique to data you're
###   asking 
##
####color = ""
####allColors = ""  # accumulator variable
####
####while color != "0":
####
####    color = input("Enter fav color (0 to quit): ")
####
####    if color != "0":
####        allColors += color + " "
####
####print(allColors)
####
##### counter variable
##### - a variable that increases or decreases by 1
####
##### accumulator varible
##### - modifies the same variable multiple times
####
####
####
####count = 0   # counter variable
####
####while count < 5:
####    print("hello")
####
####    count += 1
##
##
### break
### - a complete statement
### - immediately stops a loop
###   - any code in the loop after break doesn't
###     execute
### - used in decision structures
##
### continue
### - complete statement
### - immediately stops current iteration of loop,
###   and checks the condition again
### - used in decision structures
##
####count = 0
####
####while count < 5:
####
####    print(count)
####    
####    count += 1
####
####    if count == 3:
####        continue
####
####    print("*")
####
####print("AFTER LOOP")
##
##
##
##
### flags
### - boolean variables
###   - variable that only stores True or False
### - marks that an event has occured
##
### ask user for 4 numbers
### find the sum of numbers
### display if any even numbers were entered
##
####total = 0
####count = 0
####
####evenFlag = False   # False = no even numbers
####while count < 4:
####
####    num = eval(input("Enter a number: "))
####
####    if num % 2 == 0:
####        evenFlag = True
####
####    total += num
####    count += 1
####
####print(total)
####
####if evenFlag:
####    print("Found an even number")
####else:
####    print("No even numbers")
##
##
### Ch. 3.4: for loops
##
### while loop
### - condition-controlled loop
##
### for loop
### - count-controlled loop
###   - number of iterations depends on the number
###     of values in a given sequence
##
### types of sequences
### - strings
###   - a sequence of characters
###      "Monday"  'M','o','n','d','a','y'
##
### - sequence of integers
###      1,2,3,4,5
##
### - files
###   - sequence = number of lines in the file
###      "blue", "red", "green", "light pink"
##
### general format
###for loopVariable in sequence:
##    # code to repeat
##
### loopVariable is created and given a value by
### the for loop. You don't do this step
##
### strings and for loops
##
##word = "March"   # M,a,r,c,h
##
### display letters of March vertically
####for ch in word:
####
####    # display letters from a - e
####    if ch >= 'a' and ch <= 'e':
####        print(ch)
##
### Using your birthdate in the form
###    March 17, 2025
### use a for loop to only display the numbers.
##
### Sample Execution
###    172025
##
####lower = ""
####upper = ""
####
####reverse = ""
####
####for each in "February 17, 2025":
####
####    reverse = each + reverse
####
####print(reverse)
##
##
##    
##    
####    if each.isupper():
####        upper += each
####
####    if each.islower():
####        lower += each
####
####print(upper)
####print(lower)
##
##
##
##
##
##
##
##
##
##
##
### integer sequence with for loops
##
### range()
### - creates a sequence of integers in a specified
###   range
##
### range with 2 numbers
##
### general format
### range(startInt, endInt + 1)
##
### display numbers 1 - 5
####for num in range(1, 6):
####    print(num, end = " ")
####
####print()
####
##### display numbers 10 - 30
####for num in range(10, 31):
####    print(num, end = " ")
####
####print()
####
##### display numbers -3 to 3
####for num in range(-3, 4):
####    print(num, end = " ")
##
##
####total = 0
####
####for num in range(1, 6):
####    total += num
####
####print(total)
##
##
##
##
##
### range with 3 numbers
##
### general format
###   range(startInt, endInt + 1, step value)
##
### step value
### - used to generate the sequence
### - default value is 1
##
##
### display 5 - 1
##
####for num in range(5, 0, -1):
####    print(num, end = " ")
##
### value + step = next value in sequence
##
####1 + 2 = 3
####3 + 2 = 5
####5 + 2 = STOP
##
####1 + 1 = 2
####2 + 1 = 3
####3 + 1 = 4
####4 + 1 = 5
####5 + 1 = STOP
##
### range with 1 number
### - default startInt is 0
##
### general format
###   range(endInt + 1)
##
####for num in range(6):
####    print(num, end = " ")
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
####sentence = input("Enter a sentence: ")
####
####numDigits = 0
####
####for ch in sentence:
####
####    if ch.isdigit():
####        numDigits += 1
####
####print("\nThere are ", numDigits, "digit(s) in the sentence.")
####
########################################################################
####
####sentence = input("Enter a sentence: ")
####newSent = ""
####
####for ch in sentence:
####
####    if ch.lower() == 'a':
####        newSent += '0'
####    elif ch.lower() == 'e':
####        newSent += '1'
####    elif ch.lower() == 'i':
####        newSent += '2'
####    elif ch.lower() == 'o':
####        newSent += '3'
####    elif ch.lower() == 'u':
####        newSent += '4'
####    else:
####        newSent += ch
####
####print("\n" + newSent)
##
##
##
##
##
##
##
##
### allowing user to control for loop
##
### ask user for a number
### display the range 1 to their number
##
####num = int(input("Enter a number: "))
####dist = int(input("Enter distance between nums: "))
####
####print()
####
####for value in range(1, num + 1, dist):
####    print(value, end = " ")
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
### read from files with for loops
##
### Steps to Setup when Reading a File
### - make sure text file is in same folder
###   as Python file
### - make sure there is data in the text
##
### TO DO
### - go to folder with your Python file
### - create at text file called colors.txt
### - add 5 colors to the text file, with only
###   1 color per line
### - SAVE TEXT FILE
##
### 3 Steps to Read From File in Your Code
### - Open the file
### - Read thru the file (with for loop)
### - Close the text file
##
### Open the File
##
### open()
### - used to open a file
##
### general format
###   variable = open(name of file, mode)
##
### - mode:  'r'
### - must have .txt in file name
##
### reading the file with a for loop
### - sequence is the lines of the file
##### - each line is one value of the sequence
####
##### open file
####infile = open("colors.txt", 'r')
####
####total = 0
####
##### read the file
####for line in infile:
####    line = line.rstrip()  # remove \n
####
####    total += int(line)
####
####
####print(total)
####
####
####
####    
####    
####    # display colors that have an 'r'
######    if 'r' in line:
######        print(line)
####
####
####    
####
####
##### close file
####infile.close()
##
##
##
##
##
##
##
##
##
##
##
##
##
##
####
####infile = open("data.txt", "r")
####
####for line in infile:
####
####    line = line.rstrip()
####    
####    if line.count(' ') == 1:
####        print(line)
####
####infile.close()
####
####
####
####infile = open("data.txt", "r")
####
####for line in infile:
####
####    line = line.rstrip()
####    
####    if line[0] <= "M":
####        print("-", line)
####    else:
####        print(">", line)
####
####infile.close()
##
##
##
### Create a text file called numbers.txt and save
### it in the same folder as your Python file
##
### Write the numbers shown in the text file on
### the screen to your file and save it.
###   Follow the format shown.
##
### Goal: add all numbers in file
####infile = open("numbers.txt", "r")
####
####total = 0
####
####for line in infile:
####    line = line.rstrip()
####
####    # read each character in the line
####    for ch in line:
####        if ch.isdigit():
####            total += int(ch)
####
####print("Total:", total)
####infile.close()
##
### nested for loops
### - good for data in a table
###   - allows you to create rows and columns
##
####for row in range(3):  # 5 rows
####
####    for col in range(5):  # 4 columns
####        print(col + row, end = " ")
####
####    print() # move to next line for next row
####
##
##


















##infile = open("dogInfo.txt", 'r')
##
##for dog in infile:
##
##    dog = dog.rstrip()
##    comma = dog.find(',')
##
##    name = dog[ :comma]
##    dogAge = int(dog[comma + 1:])
##
##    humanAge = dogAge * 7
##    
##    print(">", name, "is", humanAge, "year(s) old in human years.")
##
##infile.close()



# pass statement
# - complete statement that doesn't nothing

# menu with choices 1 - 3

##choice = 1
##
##if choice == 1:
##    print("choice 1")
##
##elif choice == 2:
##    pass
##    
##else:
##    pass
















# Ch. 4.1: User-defined Functions

# functions
# - small programs that focus one task
#   - can have input, processing, and output
#     - input: 4.8
#     - process: make 4.8 an int
#     - output: 4

# num = int(4.8)

# calling a function
# - use a function
#      functionName()

# print("hello") # calling the print function

# function definition
# - define:
#   - the input the function needs (optional)
#   - what task it performs
#   - what output it can produce   (optional)

# general format
##def functionName(parameters):
##
##    # code that peforms function's task
##
##    return value

# return statement
# - how function produces output

# parameters
# - store the values given to the function as input


##num = int(4.8)

# argument
# - value given to function when it is called
# - called "passing an argument to a function"





# main function
# - holds main logic of the code
#   - details of logic will be put in other functions
##
##def main():
##    
##    # add 10 and 45
##    answer = addTwoNumbers(10, 45)
##
##    print(answer)
##
##def addTwoNumbers(num1, num2):
##
##    result = num1 + num2
##
##    return result
##
##main() # DON'T FORGET TO CALL MAIN
##























# No pre-quiz





##def checkLetterRange(word):
##    a_m_Flag = True   # True = all letters in a - m
##    
##    for ch in word:
##        if ch > 'm' or ch < 'a':
##            a_m_Flag = False
##
##    return a_m_Flag
##
##def main():
##
##    word = input("Enter a word: ")
##
##    if checkLetterRange(word):
##        print("\n" + word, "only has letters A - M.")
##    else:
##        print("\nNot all letters in", word, "are A - M.")
##    
##
##main()











# scope of variables
# - area in which you can access a variable
#   - scope is decided by where the variable
#     is created

# local scope
# - area within a function definition, including
#   the header
# - variables created here are local variables
# - local variables can only be accessed by
#   the function they're created in

# global scope
# - area outside all of the function defintions
# - variables created here are global variables
#   - global variable can be accessed by
#     everything
# - Use when multiple functions work with the
#   same variable

# global scope
word = "cat"   # global variable

def display(value):  # local variable
    print(value)

    # update global variable
    global word
    
    word = "dog"  # global variable    
    print(word)

def main():

    num = 10  # local variable

    display(num)
    print(word)

main()
print(word)





















































