
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
- **Print Function**: Using `print()` to display output.
- **Strings**: Understanding strings and their manipulation.
- **String Concatenation**: Joining multiple strings together using `+`.
- **Integers and Floats**: Introduction to numeric data types: whole numbers (integers) and decimal numbers (floats).
- **Variables**: Assigning values to variables and changing them.
- **Data Types**: Introduction to integers and floats.
- **Arithmetic Operations**: Basic operations like addition, subtraction, multiplication, division, modulus, and exponentiation.


#### Python functions mentioned in the workshops
1. `print()`: Outputs messages to the console.
2. `type()`: Returns the type of a variable.
3. `len()`: Returns the number of items in a collection (e.g., lists, strings).


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
- **Introduction to Control Flow**: Managing the order in which code executes.
- **Flowcharts and Pseudocode**: Representing algorithms visually and in plain language.
- **Control Flow before Code**: Pseudocode and flowcharts to design control logic before coding.
- **Control Flow**: Understanding how the order of execution is determined in a program.
- **Conditional Statements**: Using `if`, `elif`, and `else` to execute code based on conditions.
- **Boolean Expressions**: Evaluating conditions that return True or False.
- **Logical Operators**: Using `and`, `or`, and `not` to combine conditions.
- **Relational Operators**: Using `==`, `!=`, `>`, `<`, `>=`, and `<=` to compare values.
- **If Statement**: Executing code based on a true condition.
- **Logical Operators**: Combining conditions with `and`, `or`, and `not`.
- **Else Statement**: Providing alternative code execution when `if` conditions are not met.
- **Else If Statement**: Handling multiple conditions with `elif`.

#### Python functions mentioned in the workshops
1. `input()`: Accepts user input from the console.
2. `int()`: Converts a string input to an integer.

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
- **Introduction to Loops**: Repeating code multiple times.
- **Loops**: Understanding the concept of iteration.
- **For Loops**: [Using `for` loops for definite iteration over a sequence like lists or ranges.](https://atlas.org/api/v1/files?documentId=7e053b4f-7a58-41df-9d61-fc3553aaabad)
- **While Loops**: Using `while` loops for indefinite iteration until a condition is met.
- **Loop Control**: Using `break`, `continue`, and `else` statements to control loop execution.
- **Nested Loops**: Understanding loops within loops.

#### Python functions mentioned in the workshops
1. `range()`: Generates a sequence of numbers, often used in `for` loops.

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
- **Introduction to Lists**: Creating and working with lists, a collection of elements.
- **Accessing List Elements**: Using indexing to access elements in a list.
- **Modifying List Elements**: Changing elements in a list through indexing or list methods.
 **Lists**: [Creating and using lists to store collections of items.](https://atlas.org/api/v1/files?documentId=7e053b4f-7a58-41df-9d61-fc3553aaabad)
- **List Methods**: Using methods like `.append()`, `.remove()`, and `.pop()`.
- **Accessing List Elements**: Understanding indexing and slicing.
- **Two Dimensional (2D) Lists**: Creating and manipulating lists of lists.
- **`zip()` Function**: Combining multiple lists into tuples using the `zip()` function.
- **Other Useful List Methods**: Exploring methods like `append()`, `insert()`, `remove()`, `pop()`, and `sort()`.
- **Length of a List**: Using `len()` to find the number of elements in a list.

#### Python functions mentioned in the workshops
1. `list()`: Converts other data types (like range) into a list.
2. `len()`: Returns the number of elements in a list.
3. `count()`: Returns the number of times a specified element appears in a list.
4. `len()`
5. `append()`
6. `extend()`
7. `remove()`
8. `pop()`
9. `del`
10. `zip()`

#### [Python List Methods](https://www.geeksforgeeks.org/list-methods-python/)
1. `append()`: Used for adding elements to the end of the List.
2. `copy()`: Returns a shallow copy of a list.
3. `clear()`: Removes all items from the list.
4. `count()`: Counts the elements in the list.
5. `extend()`: Adds each element of an iterable to the end of the List.
6. `index()`: Returns the lowest index where the element appears.
7. `insert()`: Inserts a given element at a given index in a list.
8. `pop()`: Removes and returns the last value from the List or the given index value.
9. `remove()`: Removes a given object from the List.
10. `reverse()`: Reverses objects of the List in place.
11. `sort()`: Sorts a List in ascending, descending, or user-defined order.
12. `min()`: Calculates the minimum of all the elements of the List.
13. `max()`: Calculates the maximum of all the elements of the List.

#### [Python List/Array Methods](https://www.w3schools.com/python/python_ref_list.asp)
1. `append()`: Adds an element at the end of the list.
2. `clear()`: Removes all the elements from the list.
3. `copy()`: Returns a copy of the list.
4. `count()`: Returns the number of elements with the specified value.
5. `extend()`: Adds the elements of a list (or any iterable) to the end of the current list.
6. `index()`: Returns the index of the first element with the specified value.
7. `insert()`: Adds an element at the specified position.
8. `pop()`: Removes the element at the specified position.
9. `remove()`: Removes the first item with the specified value.
10. `reverse()`: Reverses the order of the list.
11. `sort()`: Sorts the list.

#### [Python Data Structures](https://docs.python.org/3/tutorial/datastructures.html)

##### Common List Methods:
1. `append(x)`: Add an item to the end of the list.
2. `extend(iterable)`: Extend the list by appending all the items from the iterable.
3. `insert(i, x)`: Insert an item at a given position.
4. `remove(x)`: Remove the first item from the list whose value is equal to x.
5. `pop([i])`: Remove the item at the given position in the list and return it.
6. `clear()`: Remove all items from the list.
7. `index(x[, start[, end]])`: Return zero-based index in the list of the first item whose value is equal to x.
8. `count(x)`: Return the number of times x appears in the list.
9. `sort(key=None, reverse=False)`: Sort the items of the list in place.
10. `reverse()`: Reverse the elements of the list in place.
11. `copy()`: Return a shallow copy of the list.

##### Additional Functions Mentioned:
12. `len(s)`: Return the length (the number of items) of an object.
13. `del s[i]`: Delete the item at a specific position.
14. `del s[i:j]`: Delete a slice from the list.
15. `max(iterable, *[, key, default])`: Return the largest item in an iterable.
16. `min(iterable, *[, key, default])`: Return the smallest item in an iterable.
17. `sum(iterable, /, start=0)`: Sums up the items of an iterable from left to right and returns the total.
18. `sorted(iterable, *, key=None, reverse=False)`: Return a new sorted list from the items in iterable.
19. `reversed(seq)`: Return a reverse iterator over the values of the given sequence.
20. `enumerate(iterable, start=0)`: Return an enumerate object.
21. `filter(function, iterable)`: Construct an iterator from elements of iterable for which function returns true.
22. `map(function, iterable, ...)`: Return an iterator that applies function to every item of iterable, yielding the results.
23. `zip(*iterables)`: Make an iterator that aggregates elements from each of the iterables.

##### Set Methods:
24. `add(x)`: Add an element to a set.
25. `remove(x)`: Remove an element from a set; it must be a member.
26. `discard(x)`: Remove an element from a set if it is a member.
27. `pop()`: Remove and return an arbitrary set element.
28. `clear()`: Remove all elements from this set.

##### Dictionary Methods:
29. `dict()`: Create a new dictionary.
30. `dict.clear()`: Remove all items from the dictionary.
31. `dict.copy()`: Return a shallow copy of the dictionary.
32. `dict.fromkeys(iterable[, value])`: Create a new dictionary with keys from iterable and values set to value.
33. `dict.get(key[, default])`: Return the value for key if key is in the dictionary, else default.
34. `dict.items()`: Return a new view of the dictionary’s items (key, value).
35. `dict.keys()`: Return a new view of the dictionary’s keys.
36. `dict.pop(key[, default])`: If the key is in the dictionary, remove it and return its value, else return default.
37. `dict.popitem()`: Remove and return a (key, value) pair as a 2-tuple.
38. `dict.setdefault(key[, default])`: Return the value of the key if it is in the dictionary; if not, insert key with a value of default and return default.
39. `dict.update([other])`: Update the dictionary with the key/value pairs from other, overwriting existing keys.
40. `dict.values()`: Return a new view of the dictionary’s values.

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
- **Introduction to Functions**: Understanding the purpose of functions for code reusability.
- **Defining a User Function**: Using `def` to create a function.
- **Calling a Function**: Running a function by its name with parentheses.
- **Functions**: [Defining and calling functions to create reusable code.](https://atlas.org/api/v1/files?documentId=7e053b4f-7a58-41df-9d61-fc3553aaabad)
- **Parameters and Arguments**: Understanding how to pass data to functions.
- **Return Values**: Using `return` to send data back from functions.
- **Multiple Returns**: Returning multiple values from a function.
- **Types of Arguments**: Using positional, keyword, and default arguments in function definitions.
- **Built-in Functions vs. User-Defined Functions**: Differentiating between Python’s built-in functions and custom functions.


#### Python functions mentioned in the workshops
1. `def`: Used to define a function.
2. `print()`
3. `return`: Used to return values from a function.
4. `input()`
5. `str()`
6. `int()`

#### Python functions mentioned in the link are available in the workshop
[Python Built in Functions](https://www.w3schools.com/python/python_ref_functions.asp)
1. `abs()`: Returns the absolute value of a number
2. `all()`: Returns True if all items in an iterable object are true
3. `any()`: Returns True if any item in an iterable object is true
4. `ascii()`: Returns a readable version of an object. Replaces non-ASCII characters with escape character
5. `bin()`: Returns the binary version of a number
6. `bool()`: Returns the boolean value of the specified object
7. `bytearray()`: Returns an array of bytes
8. `bytes()`: Returns a bytes object
9. `callable()`: Returns True if the specified object is callable, otherwise False
10. `chr()`: Returns a character from the specified Unicode code
11. `classmethod()`: Converts a method into a class method
12. `compile()`: Returns the specified source as an object, ready to be executed
13. `complex()`: Returns a complex number
14. `delattr()`: Deletes the specified attribute (property or method) from the specified object
15. `dict()`: Returns a dictionary (Array)
16. `dir()`: Returns a list of the specified object's properties and methods
17. `divmod()`: Returns the quotient and the remainder when argument1 is divided by argument2
18. `enumerate()`: Takes a collection (e.g., a tuple) and returns it as an enumerate object
19. `eval()`: Evaluates and executes an expression
20. `exec()`: Executes the specified code (or object)
21. `filter()`: Use a filter function to exclude items in an iterable object
22. `float()`: Returns a floating-point number
23. `format()`: Formats a specified value
24. `frozenset()`: Returns a frozenset object
25. `getattr()`: Returns the value of the specified attribute (property or method)
26. `globals()`: Returns the current global symbol table as a dictionary
27. `hasattr()`: Returns True if the specified object has the specified attribute (property/method)
28. `hash()`: Returns the hash value of a specified object
29. `help()`: Executes the built-in help system
30. `hex()`: Converts a number into a hexadecimal value
31. `id()`: Returns the id of an object
32. `input()`: Allowing user input
33. `int()`: Returns an integer number
34. `isinstance()`: Returns True if a specified object is an instance of a specified object
35. `issubclass()`: Returns True if a specified class is a subclass of a specified object
36. `iter()`: Returns an iterator object
37. `len()`: Returns the length of an object
38. `list()`: Returns a list
39. `locals()`: Returns an updated dictionary of the current local symbol table
40. `map()`: Returns the specified iterator with the specified function applied to each item
41. `max()`: Returns the largest item in an iterable
42. `memoryview()`: Returns a memory view object
43. `min()`: Returns the smallest item in an iterable
44. `next()`: Returns the next item in an iterable
45. `object()`: Returns a new object
46. `oct()`: Converts a number into an octal
47. `open()`: Opens a file and returns a file object
48. `ord()`: Convert an integer representing the Unicode of the specified character
49. `pow()`: Returns the value of x to the power of y
50. `print()`: Prints to the standard output device
51. `property()`: Gets, sets, or deletes a property
52. `range()`: Returns a sequence of numbers, starting from 0 and incrementing by 1 (by default)
53. `repr()`: Returns a readable version of an object
54. `reversed()`: Returns a reversed iterator
55. `round()`: Rounds a number
56. `set()`: Returns a new set object
57. `setattr()`: Sets an attribute (property/method) of an object
58. `slice()`: Returns a slice object
59. `sorted()`: Returns a sorted list
60. `staticmethod()`: Converts a method into a static method
61. `str()`: Returns a string object
62. `sum()`: Sums the items of an iterator
63. `super()`: Returns an object that represents the parent class
64. `tuple()`: Returns a tuple
65. `type()`: Returns the type of an object
66. `vars()`: Returns the `__dict__` property of an object
67. `zip()`: Returns an iterator from two or more iterators

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
3. `str()`: Converts other data types to a string.
4. `replace()`: Replaces occurrences of a substring.
5. `find()`: Searches for a substring and returns its index.
6. `join()`: Joins elements of a list into a single string with a specified delimiter.
7. `split()`: Splits a string into a list based on a specified delimiter.
8. `strip()`: Removes whitespace from the beginning and end of a string.
9. `int()`
10. `bool()`
11. `title()`: Capitalizes the first letter of each word in a string.
12. `upper()`: Converts a string to uppercase.
13. `lower()`: Converts a string to lowercase.
14. `print()`

#### [Python Escape Characters](https://www.w3schools.com/python/gloss_python_escape_characters.asp)

| Code  | Result           |
|-------|------------------|
| \\\'  | Single Quote      |
| \\\\  | Backslash         |
| \\n   | New Line          |
| \\r   | Carriage Return   |
| \\t   | Tab               |
| \\b   | Backspace         |
| \\f   | Form Feed         |
| \\ooo | Octal value       |
| \\xhh | Hex value         |

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

###### [Python String find() Method](https://www.w3schools.com/python/ref_string_find.asp)
```python
txt = "Hello, welcome to my world."

print(txt.find("q"))   # Output: -1
print(txt.index("q"))  # Raises ValueError: substring not found
```




