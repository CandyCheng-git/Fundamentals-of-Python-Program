
# Fundamentals of Programming – Summary 

## Comments
```python
# character enables a comment  
# Comment on a single line

name = "Alice"  # variable name has the value of Alice  
```
### Week 1

## print() Function
The `print()` function prints a message to the console or output.
```python
# Prints blank line  
print()  

# Prints message "Cheatsheet"
print("Cheatsheet")
```
### Week 1

## Syntax
Covers Strings, Boolean, Lists, and so on.

### Week 1

## Strings
Strings contain characters enclosed by single quotes `' '` or double quotes `" "`.
```python
# Single quotes
single = 'Single'  

# Double quotes  
double = "Double"  
```
### Week 1

## String Concatenation
The plus sign `+` can add two `str` types or Strings (and not just numeric types).
```python
single = 'Single'
double = "Double"
# String Concatenation  
concatenate = single + double  # becomes "SingleDouble"
```

## Integer (and Float)
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

## Variables
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

## Arithmetic Operations
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

## Modulo Operator (%)
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

## Plus Equals
A shortcut to update a variable value can be done by using the plus equals sign `+=`.
```python
# Plus Equals (int)  
count = 0  
count += 1  # equivalent to count = count + 1  
  
# Plus Equals (str)  
data = "Plus "  
data += " Equals"  # equivalent to data = data + " Equals" 
```

## Errors
PyCharm will (a) display the error type; and (b) information where the error has occurred.
```python
# If unsure, use type() function 
# ^^^^^^  
SyntaxError: invalid syntax  
```

## NameError
NameError is produced when variable(s) were not defined.
```python
# NameError  
print(result)
```

## SyntaxError
SyntaxError is produced when Python syntax is not followed.
```python
# SyntaxError  
result = 'Wrong quotes"
```

## ZeroDivisionError
ZeroDivisionError occurs when a number (denominator) is divided by a 0 or 0.0.
```python
# ZeroDivisionError  
numerator = 50  
denominator = 0  
result = numerator / denominator
print(result)  
```
