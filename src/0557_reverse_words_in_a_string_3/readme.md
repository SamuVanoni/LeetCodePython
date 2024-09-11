## What Did I Learn?

### In this challenge I learned how to transform a string into a list and a list into a string:

1. We start by transforming each word in the string into words in a list
```python
words = s.split()
```

2. Then we take each word from that list and store it in reverse in a new list
```python
for word in words:
    ans.append(word[len(word)::-1])
```

3. We finish by transforming the new list into a string
```python
return ' '.join(ans)
```