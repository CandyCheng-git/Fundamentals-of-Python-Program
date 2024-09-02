
# Fundamentals of Programming – Summary 

## Table of Contents

1. [Week 1](#week-1)
2. [Week 2](#week-2)
3. [Week 3](#week-3)
4. [Week 4](#week-4)
5. [Week 5](#week-5)
6. [Week 7](#week-7)

### Week 1
#### Introduction to Programming
- **Comments**: Using `#` to add comments in code.
- **Strings**: Understanding strings and their manipulation.
- **Variables**: Assigning values to variables and changing them.
- **Data Types**: Introduction to integers and floats.
- **Arithmetic Operations**: Basic operations like addition, subtraction, multiplication, division, modulus, and exponentiation.
- **Print Function**: Using `print()` to display output.

#### Python functions mentioned in the workshops
1. `print()`
2. `type()`


#### More concepts in Week 1
##### Comments
```python
# character enables a comment  
# Comment on a single line

name = "Alice"  # variable name has the value of Alice  
```


##### print() Function
The `print()` function prints a message to the console or output.
```python
# Prints blank line  
print()  

# Prints message "Cheatsheet"
print("Cheatsheet")
```


##### Syntax
Covers Strings, Boolean, Lists, and so on.


##### Strings
Strings contain characters enclosed by single quotes `' '` or double quotes `" "`.
```python
# Single quotes
single = 'Single'  

# Double quotes  
double = "Double"  
```


##### String Concatenation
The plus sign `+` can add two `str` types or Strings (and not just numeric types).
```python
single = 'Single'
double = "Double"
# String Concatenation  
concatenate = single + double  # becomes "SingleDouble"
```

##### Integer (and Float)
- **Integer** must be a whole number, it can be 0, positive, or negative, but must be without decimals.
- **Float** is a number, it can be positive or negative, but must contain one or more decimals.
```python
# Integer or int  
height = 183  
weather = -6  
zero = 0  

# Float  
f = 1.33  

# If unsure, use type() function 
print(type(f))  # For example
```

##### Variables
Variables assign a value or store data using an equals sign `=`.
```python
# Valid variable names and assignment 
string_var = "String is here"  
int_var = 10  
float_var = 10.13  
bool_statement = False  

# Variable value can be changed
int_var = 12  
```

##### Arithmetic Operations
- `+` for addition
- `-` for subtraction
- `*` for multiplication
- `/` for division
- `%` for modulus (returns the remainder)
- `**` for exponentiation (number^number)
```python
# Arithmetic operations  
addition = 2 + 5  # 7  
subtraction = 30 - 40  # -10  
multiplication = 2 * 90  # 180  
division = 4 / 4.0  # 1.0  
modulus = 13 % 2  # 1  
exponentiation = 2 ** 3  # 8  
```

##### Modulo Operator (%)
Modulo operation, with a percent sign `%`, returns the remainder of the division operation.
1. `6 % 2` results in 0 because 6 divided by 2 would return 3, leaving no remainder.
2. `7 % 2` results in 1 because 7 divided by 2 is not evenly divisible, leaving 1 remainder.
3. `9 % 50000` results in 9 because 9 divided by 50000 is not evenly divisible, leaving 9 remainder.
```python
# Modulo operator % 
# Example 1  
zero = 6 % 2  # 0  
  
# Example 2  
one = 7 % 2  # 1  
  
# Example 3  
nine = 9 % 50000  # 9
```

##### Plus Equals
A shortcut to update a variable value can be done by using the plus equals sign `+=`.
```python
# Plus Equals (int)  
count = 0  
count += 1  # equivalent to count = count + 1  
  
# Plus Equals (str)  
data = "Plus "  
data += " Equals"  # equivalent to data = data + " Equals" 
```

##### Errors
PyCharm will (a) display the error type; and (b) information where the error has occurred.
```python
# If unsure, use type() function 
# ^^^^^^  
SyntaxError: invalid syntax  
```

##### NameError
NameError is produced when variable(s) were not defined.
```python
# NameError  
print(result)
```

##### SyntaxError
SyntaxError is produced when Python syntax is not followed.
```python
# SyntaxError  
result = 'Wrong quotes"
```

##### ZeroDivisionError
ZeroDivisionError occurs when a number (denominator) is divided by a 0 or 0.0.
```python
# ZeroDivisionError  
numerator = 50  
denominator = 0  
result = numerator / denominator
print(result)  
```

### Week 2
#### Control Flow
- **Control Flow**: Understanding how the order of execution is determined in a program.
- **Conditional Statements**: Using `if`, `elif`, and `else` to control the flow based on conditions.
- **Boolean Expressions**: Evaluating conditions that return True or False.
- **Logical Operators**: Using `and`, `or`, and `not` to combine conditions.
- **Flowcharts and Pseudocode**: Representing algorithms visually and in plain language.

#### Python functions mentioned in the workshops
1. `input()`
2. `bool()`

#### More concepts in Week 2

##### Boolean - False
```python
# Empty, False, 0 None
```

##### Boolean – True
```python
# Any number (beside 0), True, String (that is not empty)
```

##### Equals and Not Equals
```python
test = ""
print(bool(test))  # False
'13' == 13  # False
```

##### If Statement
```python
day = 'Monday'  # Enter day here
if day == 'Monday':
    print('attend the Workshop')
```

##### Ask for User Input
```python
print('Enter your age: ')
age = input()  # stores String
age = int(age)  # converts to int
```

##### Logical Operators
1. `and`
2. `or`
3. `not`

###### Example
```python
print(not True)  # prints False
print(not False)  # prints True
```

##### Else Statement
```python
credits = 35  # Modify credits value here
if credits >= 1000:
    print("You are a Platinum member")
elif credits >= 500:
    print("You are a Gold member")
elif credits >= 250:
    print("You are a Silver member")
else:
    print("You are a Red member")
```

### Week 3
#### Loops
- **Loops**: Understanding the concept of iteration.
- **For Loops**: [Using for loops for definite iteration.](https://atlas.org/api/v1/files?documentId=7e053b4f-7a58-41df-9d61-fc3553aaabad)
- **While Loops**: Using `while` loops for indefinite iteration.
- **Loop Control**: Using `break`, `continue`, and `else` statements in loops.
- **Nested Loops**: Understanding loops within loops.

#### Python functions mentioned in the workshops
1. `range()`

#### More concepts in Week 3

##### Loops
1. **Indefinite**: where the number of times a loop is executed depends on the number of times a condition is met.
2. **Definite**: where the number of times a loop will be executed is declared in advance.

###### Example
```python
grades = [35, 50, 65, 85]
print(grades[0])  # 35
print(grades[1])  # 50
print(grades[2])  # 65
print(grades[3])  # 85
```

##### For Loops
A type of definite iteration that will know how many times to iterate the loop because our grades list contains a collection of elements or items with a predefined length.
```python
for g in grades:
    print(g)
```

##### One Line For Loops
```python
grades = [35, 50, 65, 85]
for g in grades: print(g)
```

##### Using Range in For Loops
```python
for temp in range(11):
    # Iterates 11 times, from 0 to 10
    print('I must attend my workshops')
```

###### Example
```python
for temp in range(11):
    print('Iteration number is: ' + str(temp))
# Output:
# Iteration number is: 0
# Iteration number is: 1
# Iteration number is: 2
# Iteration number is: 3
# Iteration number is: 4
# Iteration number is: 5
# Iteration number is: 6
# Iteration number is: 7
# Iteration number is: 8
# Iteration number is: 9
# Iteration number is: 10
```

##### While Loops
```python
iteration = 0
while iteration < 11:
    print('Iteration number is: ' + str(iteration))
    iteration = iteration + 1

grades = [35, 50, 65, 85]
iteration = 0
while iteration < len(grades):
    print(grades[iteration])
    iteration = iteration + 1
```

##### Loop Control - Break
```python
grades = [35, 50, 65, 85]
for grade in grades:
    print(grade)
    if grade < 50:
        break
# prints 35 because the break is after the print function
```

##### Loop Control - Continue
```python
grades = [35, 50, 65, 85]
for grade in grades:
    if grade < 50:
        continue
    print(grade)
# prints 50, 65, 85
```

##### Loop Control - Else
```python
grades = [35, 50, 65, 85]
for grade in grades:
    print(grade)
else:
    print('Completed the grades for loop.')
```

##### Nested Loops
```python
gradebook = [
    ['Jing', 35], 
    ['Jim', 50],
    ['Kerrie', 65],
    ['Rakesh', 85]
]
for student in gradebook:
    print(student)
    for detail in student:
        print(detail)
```

##### List Comprehension
```python
new_list = [name for name in students if 'i' in name]
```

###### Example
```python
new_list = [i for i in range(11)]
new_list = [i for i in range(11) if i > 5]
```

### Week 4
#### Lists
- **Lists**: [Creating and using lists to store collections of items.](https://atlas.org/api/v1/files?documentId=7e053b4f-7a58-41df-9d61-fc3553aaabad)
- **List Methods**: Using methods like `.append()`, `.remove()`, and `.pop()`.
- **Accessing List Elements**: Understanding indexing and slicing.
- **Two-Dimensional Lists**: Working with lists of lists (nested lists).
- **Length of a List**: Using `len()` to find the number of elements in a list.

#### Python functions mentioned in the workshops
1. `len()`
2. `append()`
3. `extend()`
4. `remove()`
5. `pop()`
6. `del`
7. `zip()`

#### More concepts in Week 4

##### Summary of Python collections
1. **List**: “is a collection which is ordered and changeable (Mutable). Allows duplicate members.”
2. **Tuple**: “is a collection which is ordered and unchangeable. Allows duplicate members.”
3. **Set**: “is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.”
4. **Dictionary**: “is a collection which is ordered** and changeable (Mutable). No duplicate members.”

##### List
- List is created using square brackets `[]`.
- Each item is separated by a comma `,`.
- Good Python practice: insert a space after each comma.
- Store a combination of different data types.
```python
list = ["String", 27, False, 25.65, [1, 2, 3, 4, "Count"], None]

# Create an empty list
list_empty = []
list_empty = list(())
```

##### List Methods / Class
```python
# list_name is our list
# .method() is a method of our list
# This example is for structure illustration,
# it will not work
list_name.method() 
AttributeError: 'list' object has no attribute 'method'

# Syntax for List methods
list.method(parameter)
```

##### Reference - Check Methods Documentation
Use the following official websites:
1. [Official Python Docs](https://docs.python.org/3/tutorial/datastructures.html)
2. [W3Schools Docs](https://www.w3schools.com/python/python_ref_list.asp)
3. [GeeksforGeeks Docs](https://www.geeksforgeeks.org/list-methods-in-python/)



##### List Method: .append()
```python
# adds an element to the end of a list
grades = [35, 50, 65, 85]
grades.append(67)
print(grades)  # Prints [35, 50, 65, 85, 67]
```

##### Adding Multiple Items to a List
```python
grades = [35, 50, 65, 85, 67]
grades += [76, 78, 52]  # OR grades = grades + [76, 78, 52]
grades.extend([68, 72])  # square brackets are used here and above
print(grades)  # prints [35, 50, 65, 85, 67, 76, 78, 52, 68, 72]
```

##### Accessing List Elements
- The first element in a list has an index of 0.
- Negative index can be used to access last element(s) of a list.
```python
students = ['Jing', 'Jim', 'Kerrie', 'Rakesh']
print(students[1])  # prints Jim
print(students[-1])  # prints Rakesh
```

##### Element Index and Negative Index Example:
| Element | Index | Negative Index |
|---------|-------|----------------|
| 'Jing'  | 0     | -4             |
| 'Jim'   | 1     | -3             |
| 'Kerrie'| 2     | -2             |
| 'Rakesh'| 3     | -1             |

##### Length of a List
The `len()` function returns the number of items in an object.
```python
students = ['Jing', 'Jim', 'Kerrie', 'Rakesh']
print(len(students))  # prints 4

guess = 'Howmansafayhschatersarehere can you guess? :-)'
print(len(guess))  # prints 46
```

##### Remove List Elements
1. `grades.remove(value)`
2. `grades.pop(specific_index)`
3. `del grades[specific_index]`

###### Example:
```python
grades = [35, 50, 65, 85]
grades.remove(35)
print(grades)  # prints [50, 65, 85]

grades = [35, 50, 65, 85]
grades.pop(0)
print(grades)  # prints [50, 65, 85]

grades = [35, 50, 65, 85]
del grades[0]
print(grades)  # prints [50, 65, 85]
```

##### Two Dimensional (2D) Lists
Known as a nested list – this logic can be applied to create a three-dimensional (3D) list.
```python
gradebook = [['Jing', 35], ['Jim', 50], ['Kerrie', 65], ['Rakesh', 85]]
gradebook = [
    ['Jing', 35], 
    ['Jim', 50], 
    ['Kerrie', 65], 
    ['Rakesh', 85]
]
print(gradebook[-1][1])  # prints 85
gradebook[0][1] = 35
gradebook[-4][1] = 35
gradebook[-4][-1] = 35
```

##### Zip
- Joins lists together. Extremely powerful!
- If zip parameters (or iterators) lengths are different, then the iterator with the least element determines the length of the new iterator.
```python
students = ['Jing', 'Jim', 'Kerrie', 'Rakesh', 'Candy']
grades = [35, 50, 65, 85]
gradebook_zip = list(zip(students, grades))
# print(gradebook_zip) # zip creation - note the tuples
# [('Jing', 35), ('Jim', 50), ('Kerrie', 65), ('Rakesh', 85)]
# print(gradebook) # original
# [['Jing', 35], ['Jim', 50], ['Kerrie', 65], ['Rakesh', 85]]
# "Candy" will be disappeared
```

##### Tuples
- Do the same operation as Lists.
- Tuples are unchangeable.
- However, instead of declaring using square brackets `[]` like Lists, it uses round brackets `()`.

###### Example:
```python
# .count(): returns the number of times the specified element appears in the list
# .insert(): inserts the specified value at the specified position
# .sort(): sorts the list ascending by default
# .sorted(): returns a sorted list of the specified iterable object
```

##### Built-in Function
```python
# Syntax for a built-in function
builtinfuncion(parameter)
```

##### Range
```python
numbers = [0, 1, 2, 3, 4, 5]
```

###### Example:
```python
# 0 to 5
range(6)

# 0 to 999
range(1000)
```

##### Reference - Range
Check [W3Schools](https://www.w3schools.com/python/ref_func_range.asp) for more information.

###### Example:
```python
# Even sequence of numbers ranging from -255 to 255
ans = list(range(-254, 256, 2))

print(list(range(-10, 10, 2))) 
# [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8]

print(list(range(-10, 10, 3))) 
# [-10, -7, -4, -1, 2, 5, 8]

print(list(range(0, 10, 3)))
# [0, 3, 6, 9]
```

##### Slicing Lists
```python
nums[start:end]
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
len(nums) = 9
nums[2:7]  # For i = 2 ; i < 7
nums[:n]  # For i = 0 ; i = n
nums[:3]  # For i = 0 ; i = 3
nums[n:]  # For i = len(nums)-n ; i < len(nums)
nums[-6:]  # For i = len(nums)-6 ; i < len(nums)
# [3, 4, 5, 6, 7, 8]
```

##### Sets
Using curly brackets `{}`:
1. Set items are unchangeable.
    - The exception: add and remove items allowed.
2. Set items are unordered – items can’t be indexed as there’s no structure.
```python
# prints {65, 50, 35, 85}
grades_set = {35, 50, 65, 85, 85, 85}
print(grades_set)
```

##### Dictionary
Using curly brackets `{}`, but store data values in key:value pairs.
```python
gradebook_dict = {
    'Jing': {
        'address': 'Fake Rd',
        'student_id': 12345,
        'ass1_grade': 20,
        'ass2_grade': 15,
        'ass3_grade': 0,
        'final_grade': 35
    },
    'Jim': 50,
    'Kerrie': 65,
    'Rakesh': 85
}
print(gradebook_dict['Jing'])  # prints {'address': 'Fake Rd', 'student_id': 12345, 'ass1_grade': 20, 'ass2_grade': 15, 'ass3_grade': 0, 'final_grade': 35}
```

### Week 5
#### Functions
- **Functions**: [Defining and calling functions to create reusable code.](https://atlas.org/api/v1/files?documentId=7e053b4f-7a58-41df-9d61-fc3553aaabad)
- **Parameters and Arguments**: Understanding how to pass data to functions.
- **Return Values**: Using `return` to send data back from functions.
- **Types of Arguments**: Positional, keyword, and default arguments.
- **Built-in vs. User-Defined Functions**: Understanding the difference and best practices.

#### Python functions mentioned in the workshops
1. `def` (for defining functions)
2. `print()`
3. `return`
4. `input()`
5. `str()`
6. `int()`

#### More concepts in Week 5

##### User Defined Functions
```python
def function_name(first_parameter):
    pass
```

##### Functions - Arguments
```python
def print_hello(name):
    print('Welcome ' + name + ' to print_hello function')

print_hello('Mark')  # OR print_hello(name = 'Mark')
# prints Welcome Mark to print_hello function
```

##### Functions - Multiple Parameters and Multiple Arguments
```python
def print_hello(name, surname):
    print('Welcome ' + name + ' ' + surname + ' to print_hello function')

# prints Welcome Mark Smith to print_hello function
print_hello('Mark', 'Smith')
# OR print_hello(name = 'Mark', surname = 'Smith')
# OR print_hello(surname = 'Smith', name = 'Mark')
```

##### Functions - Returns and Multiple Returns
```python
def find_max(numbers):
    max_value = numbers[0]  # Initialise the max value to the first number in the list
    for num in numbers:
        if num > max_value:
            max_value = num  # Update the max value if the current number is greater
    return max_value

numbers = [3, 6, 2, 8, 4, 10, 1]
max_num = find_max(numbers)
print(max_num)  # Output: 10
```

##### Currency Exchange Function Example
```python
def exchange_usd_to_aud(usd_amount, exchange_rate):
    return usd_amount * exchange_rate

aud_amount = exchange_usd_to_aud(100, 1.433)
print('100 US dollars would give: ' + str(aud_amount) + ' AUD dollars')
# prints 100 US dollars would give: 143.3 AUD dollars
```

##### Weather Report Function Example
```python
weather_data = [37, 23, 30]

def weather_report(weather):
    first = 'Today: ' + str(weather[0])
    second = 'Tomorrow: ' + str(weather[1])
    third = 'Two days after: ' + str(weather[2])

    return first, second, third

monday, tuesday, wednesday = weather_report(weather_data)
# monday = 'Today: 37'
# tuesday = 'Tomorrow: 23'
# wednesday = 'Two days after: 30'
```

##### Types of Arguments
1. **Positional arguments**: arguments that are called by their position in the function definition.
2. **Keyword arguments**: arguments that are called by their name.
3. **Default arguments**: arguments that are given default values.

###### Example:
```python
def travel_cost(destination_km, price_per_km):
    return destination_km * price_per_km

# Positional arguments:
print(travel_cost(15, 5))

# Keyword arguments:
print(travel_cost(destination_km = 15, price_per_km = 15))

def travel_cost(destination_km, price_per_km = 5):
   return destination_km * price_per_km

# Default arguments:
print(travel_cost(15))
```

###### More Complex Example:
```python
savings = 1000

def travel_cost(destination_km, price_per_km = 5):
    print('Your savings is: ' + str(savings))
    print('Destination (in km) provided: ' + str(destination_km))
    print('Total cost: ' + str(destination_km * price_per_km))

print(savings)
travel_cost(20)

# Output:
# 1000
# Your savings is: 1000
# Destination (in km) provided: 20
# Total cost: 100
```

##### Built-in Functions
###### Simple Example:
```python
print()
```

### Week 7
#### Strings
- **String Manipulation**: Slicing and concatenating strings.
- **Immutability of Strings**: Understanding that strings cannot be changed after creation.
- **Escape Characters**: Using escape characters for special characters in strings.
- **Iterating Strings**: Looping through characters in a string.
- **String Methods**: Using methods like `.lower()`, `.upper()`, `.replace()`, `.find()`, and `.split()`.

#### Python functions mentioned in the workshops
1. `len()`
2. `id()`
3. `str()`
4. `replace()`
5. `find()`
6. `join()`
7. `split()`
8. `strip()`
9. `int()`
10. `bool()`
11. `title()`
12. `upper()`
13. `lower()`
14. `print()`

#### More concepts in Week 7

##### Manipulation of Strings
```python
single = 'String with Single quotation marks'
#          ^
#           \
print(single[1])
# prints t
```
```python
single = 'String with Single quotation marks'
#           ^  ^
#           \  /
print(single[2:6])
# prints ring
```

##### Concatenating Strings
```python
single = 'String with Single quotation marks'
double = "String with Double quotation marks"

comb = single + double + 'extraString'
# 'String with Single quotation marksString with Double quotation marksextraString'
```

##### Counting Strings
```python
comb = 'String with Single quotation marksString with Double quotation marksextraString'
print(len(comb))
#print 79
```

##### Strings are Immutable
- The String can’t be changed once it’s created
- Using the Python built-in `id()` function, it returns the unique id for the specified object.
```python
string = 'Test'
print(id(string))
# prints 2084536090672
string = 'Test change'
print(id(string))
# prints 2084479927856
```

##### Escape Characters
- backslash `\` was used to combine multiple lines in the String
- escape character – double quotes `""` – needs to be included within the String – This is achieved by using `\"`
```python
tesla_quote = "\"I do not care that they stole my idea... "
              "I care that they do not have any of their own.\""
#print "I do not care that they stole my idea... I care that they do not have any of their own."
```


##### Iterating Strings
```python
def print_letter(word):
   for letter in word:
      print(letter)

name = 'Tesla'
print_letter(name)
""" prints
T
e
s
l
a
"""
```

##### Strings and Conditionals
```python
def print_a_occurrence(word, count = 0):
   for letter in word:
      if 'a' in letter:
         count += 1

   print(count)

name = 'Tesla'
print_a_occurrence(name) # prints 1
```


##### Strings Formatting Methods
1. `.lower()` - returns the String with all lowercase characters
2. `.upper()` - returns the String with all uppercase characters
3. `.title()` - first character of each word is capitalised
```python
name = 'ivAna'

name_lower = name.lower()
print(name_lower)
# name_lower = 'ivana'

name_upper = name.upper()
print(name_upper)
# name_upper = 'IVANA'

name_title = name.title()
print(name_title)
# name_title = 'Ivana'
```


##### Splitting Strings
```python
string = 'See what happens when split is used'
print(string.split())
# prints ['See', 'what', 'happens', 'when', 'split', 'is', 'used']
```
```python
string = 'See,what,happens,when,split,is,used'
print(string.split(','))
# prints ['See', 'what', 'happens', 'when', 'split', 'is', 'used']
```


##### Joining Strings
```python
list = ['See', 'what', 'happens', 'when', 'split', 'is', 'used']
print(','.join(list))
# prints See,what,happens,when,split,is,used
```


##### Strip Strings
```python
dirty = '\n,   Lee,,,'
print(dirty.strip('\n, '))
# prints Lee
```


##### Replace Strings
```python
csv = 'abc,def,ghi'
whitespace = csv.replace(',', ' ')
# whitespace = 'abc def ghi'
```
```python
txt = "I like bananas"
x = txt.replace("bananas", "apples")
# x = 'I like apples'
```


##### Find Strings
- If found, it will return the index value
- If not found, it will return -1
```python
csv = 'abc,def,ghi'
print(csv.find('g')) # prints 8
print(csv.find('ga')) # prints -1
```





