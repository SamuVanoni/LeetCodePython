## What Did I Learn?

### In this challenge I learned:

1. If we do not find the letter in one of the words, we marked as false and let's go to the next letter
```python
if not letter in words[i]:
    find = False
    break
```

2. "Excluding" 1 letter of the string
```python
words[i] = words[i].replace(letter, "", 1)
```
