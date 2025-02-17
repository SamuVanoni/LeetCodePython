## What Did I Learn?

### In this challenge I learned:

1. How to create a dict with the number of times each number appears
```python
frequencies = {}
for num in nums:
    if num in frequencies:
        frequencies[num] += 1
    else:
        frequencies[num] = 1
```

2. Discovering the highest frequency (using the Max function to compare 2 numbers).
```python
max_frequency = 0
for frequency in frequencies.values():
    max_frequency = max(max_frequency, frequency)
```

3. Seeing how many times the greatest frequency is repeated in the dict
```python
frequency_of_max_frequency = 0
for frequency in frequencies.values():
    if frequency == max_frequency:
        frequency_of_max_frequency += 1
```