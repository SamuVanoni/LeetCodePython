## What Did I Learn?

### In this challenge I lerned more about:

1. Storing values ​​in the dictionary with the key being the last letter of the word
```python
for i in words:
    dic[i[-1]] = i[:-1]
```

2. Joining the dictionary into a string organizing by key
```python
return ' '.join([dic[j] for j in sorted(dic)])
```