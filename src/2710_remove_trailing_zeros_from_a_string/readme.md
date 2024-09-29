## What Did I Learn?

### In this challenge I leraned more about logic:

1. I made a loop that counts how many 0s are at the end of the string
```python
for i in range(len(num) - 1, -1, -1):
    if num[i] == '0':
        count += 1
    else:
        break
```

2. I make a loop that goes until the length of the string - 0
```python
for i in range(len(num) - count):
    ans += num[i]
```