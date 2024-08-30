## What Did I Learn?

### In this challenge I found a more complex solution and looking at other users' solutions I realized that it could be simpler:

1. My solution
```python
counts = []
sentinel = False
for i, word in enumerate(words):
    for j in range(len(word)):
        if word[j] == x and not sentinel:
            counts.append(i)
            sentinel = True
    sentinel = False
return counts
```
My solution uses 2 functions and 1 sentinel variable


2. User's solution
```python
res = []
for i in range(len(words)):
    if x in words[i]:
        res.append(i)
return res
```
In his solution we only have one loop and it already stores it in the array without using a sentinel