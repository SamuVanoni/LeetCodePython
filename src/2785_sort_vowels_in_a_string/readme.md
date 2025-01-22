## What Did I Learn?

### In this challenge I learned:

1. Creating a list to assemble the response. If it is a consonant it enters the original order, if it is a vowel it enters the ordered order.
```python
result = []
count = 0
for l in s:
    if l in base:
        result.append(vowels[count])
        count += 1
    else:
        result.append(l)
```

2. Transforming the list into string
```python
return ''.join(result)
```