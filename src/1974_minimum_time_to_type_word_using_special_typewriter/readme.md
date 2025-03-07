## What Did I Learn?

### In this challenge I learned:

1. Variable storing the previous letter selected
```python
pre = "a"
```

2. For each letter in Word, we calculate the difference with the previous letter (pre) and take the minimum value to add to the answer (going or coming back)
```python
for i in word:
    L = abs((ord(i)-ord(pre)))
    sum1 += min(L,26-L)
    pre = i
```

3. We returned the sum of the differences between the letters + the size of the word
```python
return sum1 + len(word)
```