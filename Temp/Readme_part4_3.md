
## Two Dimensional (2D) Lists
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

## Zip
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

## Tuples
- Do the same operation as Lists.
- Tuples are unchangeable.
- However, instead of declaring using square brackets `[]` like Lists, it uses round brackets `()`.

### Example:
```python
# .count(): returns the number of times the specified element appears in the list
# .insert(): inserts the specified value at the specified position
# .sort(): sorts the list ascending by default
# .sorted(): returns a sorted list of the specified iterable object
```

## Built-in Function
```python
# Syntax for a built-in function
builtinfuncion(parameter)
```
