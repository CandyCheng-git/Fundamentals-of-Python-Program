
## Boolean - False
```python
# Empty, False, 0 None
```

## Boolean – True
```python
# Any number (beside 0), True, String (that is not empty)
```

## Equals and Not Equals
```python
test = ""
print(bool(test))  # False
'13' == 13  # False
```

## If Statement
```python
day = 'Monday'  # Enter day here
if day == 'Monday':
    print('attend the Workshop')
```

## Ask for User Input
```python
print('Enter your age: ')
age = input()  # stores String
age = int(age)  # converts to int
```

## Logical Operators
1. `and`
2. `or`
3. `not`

### Example
```python
print(not True)  # prints False
print(not False)  # prints True
```

## Else Statement
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

## Loops
1. **Indefinite**: where the number of times a loop is executed depends on the number of times a condition is met.
2. **Definite**: where the number of times a loop will be executed is declared in advance.

### Example
```python
grades = [35, 50, 65, 85]
print(grades[0])  # 35
print(grades[1])  # 50
print(grades[2])  # 65
print(grades[3])  # 85
```

## For Loops
A type of definite iteration that will know how many times to iterate the loop because our grades list contains a collection of elements or items with a predefined length.
```python
for g in grades:
    print(g)
```

## One Line For Loops
```python
grades = [35, 50, 65, 85]
for g in grades: print(g)
```

## Using Range in For Loops
```python
for temp in range(11):
    # Iterates 11 times, from 0 to 10
    print('I must attend my workshops')
```

### Example
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

## While Loops
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

## Loop Control - Break
```python
grades = [35, 50, 65, 85]
for grade in grades:
    print(grade)
    if grade < 50:
        break
# prints 35 because the break is after the print function
```

## Loop Control - Continue
```python
grades = [35, 50, 65, 85]
for grade in grades:
    if grade < 50:
        continue
    print(grade)
# prints 50, 65, 85
```

## Loop Control - Else
```python
grades = [35, 50, 65, 85]
for grade in grades:
    print(grade)
else:
    print('Completed the grades for loop.')
```

## Nested Loops
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

## List Comprehension
```python
new_list = [name for name in students if 'i' in name]
```

### Example
```python
new_list = [i for i in range(11)]
new_list = [i for i in range(11) if i > 5]
```

