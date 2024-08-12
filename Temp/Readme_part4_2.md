
## List Method: .append()
```python
# adds an element to the end of a list
grades = [35, 50, 65, 85]
grades.append(67)
print(grades)  # Prints [35, 50, 65, 85, 67]
```

## Adding Multiple Items to a List
```python
grades = [35, 50, 65, 85, 67]
grades += [76, 78, 52]  # OR grades = grades + [76, 78, 52]
grades.extend([68, 72])  # square brackets are used here and above
print(grades)  # prints [35, 50, 65, 85, 67, 76, 78, 52, 68, 72]
```

## Accessing List Elements
- The first element in a list has an index of 0.
- Negative index can be used to access last element(s) of a list.
```python
students = ['Jing', 'Jim', 'Kerrie', 'Rakesh']
print(students[1])  # prints Jim
print(students[-1])  # prints Rakesh
```

### Element Index and Negative Index Example:
| Element | Index | Negative Index |
|---------|-------|----------------|
| 'Jing'  | 0     | -4             |
| 'Jim'   | 1     | -3             |
| 'Kerrie'| 2     | -2             |
| 'Rakesh'| 3     | -1             |

## Length of a List
The `len()` function returns the number of items in an object.
```python
students = ['Jing', 'Jim', 'Kerrie', 'Rakesh']
print(len(students))  # prints 4

guess = 'Howmansafayhschatersarehere can you guess? :-)'
print(len(guess))  # prints 46
```

## Remove List Elements
1. `grades.remove(value)`
2. `grades.pop(specific_index)`
3. `del grades[specific_index]`

### Example:
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
