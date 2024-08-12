
## Range
```python
numbers = [0, 1, 2, 3, 4, 5]
```

### Example:
```python
# 0 to 5
range(6)

# 0 to 999
range(1000)
```

## Reference - Range
Check [W3Schools](https://www.w3schools.com/python/ref_func_range.asp) for more information.

### Example:
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

## Slicing Lists
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

## Sets
Using curly brackets `{}`:
1. Set items are unchangeable.
   - The exception: add and remove items allowed.
2. Set items are unordered – items can’t be indexed as there’s no structure.
```python
# prints {65, 50, 35, 85}
grades_set = {35, 50, 65, 85, 85, 85}
print(grades_set)
```

## Dictionary
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
