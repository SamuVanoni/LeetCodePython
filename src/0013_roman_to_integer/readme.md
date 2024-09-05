## What Did I Learn?

### In this challenge I learned more about logic:

1. We start the problem by creating a dictionary:
```python
translations = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
```

2. Then we handle exceptions:
```python
s = s.replace("IV", "IIII").replace("IX", "VIIII")
s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
```

3. And finally, we exchange the key for the value in the dictionary and add it to a variable:
```python
for char in s:
    number += translations[char]
```