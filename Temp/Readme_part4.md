
## User Defined Functions
```python
def function_name(first_parameter):
    pass
```

## Functions - Arguments
```python
def print_hello(name):
    print('Welcome ' + name + ' to print_hello function')

print_hello('Mark')  # OR print_hello(name = 'Mark')
# prints Welcome Mark to print_hello function
```

## Functions - Multiple Parameters and Multiple Arguments
```python
def print_hello(name, surname):
    print('Welcome ' + name + ' ' + surname + ' to print_hello function')

# prints Welcome Mark Smith to print_hello function
print_hello('Mark', 'Smith')
# OR print_hello(name = 'Mark', surname = 'Smith')
# OR print_hello(surname = 'Smith', name = 'Mark')
```

## Functions - Returns and Multiple Returns
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

## Currency Exchange Function Example
```python
def exchange_usd_to_aud(usd_amount, exchange_rate):
    return usd_amount * exchange_rate

aud_amount = exchange_usd_to_aud(100, 1.433)
print('100 US dollars would give: ' + str(aud_amount) + ' AUD dollars')
# prints 100 US dollars would give: 143.3 AUD dollars
```

## Weather Report Function Example
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

## Types of Arguments
1. **Positional arguments**: arguments that are called by their position in the function definition.
2. **Keyword arguments**: arguments that are called by their name.
3. **Default arguments**: arguments that are given default values.

### Example:
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

## More Complex Example:
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

## Built-in Functions
```python
print()
```
