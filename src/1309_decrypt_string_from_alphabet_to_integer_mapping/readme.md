## What Did I Learn?

### In this challenge I learned how to remove the last two letters from the string:

1. If the letter = '#' we remove the last two letters stored in the answer and put the one we want
```python
 if letter == '#':
    ans = ans[:-2]
    number = int(str(s[i-2]) + str(s[i-1])) + ord('a') - 1
    ans += chr(number)
```

2. If it is a number, we store the respective letter in the answer
```python
else:
    number = int(s[i]) + ord('a') - 1
    ans += chr(number)
```