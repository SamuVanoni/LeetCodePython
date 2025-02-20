## What Did I Learn?

### In this challenge I learned:

1. Remembering how to make a frequency dict
```python
frequencies = {}
for num in arr:
    if num in frequencies:
        frequencies[num] += 1
    else:
        frequencies[num] = 1
```

2. Using set to gather repeated values
```python
# .set() => Join the repeated .values()
return len(set(frequencies.values())) == len(frequencies.values())
```