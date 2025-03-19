## What Did I Learn?

### In this challenge I learned:

1. In solution 1, we join all the words, separating them by a space.
```python
a = " ".join(words)
```

2. Then we exchanged '.' By '' and we use split () to separate the string into different words by spaces.
```python
return a.replace(separator," ").split()
```

1. In solution 2, for each word, we apply split (), and if the result is not empty, we add to the answer.
```python
for i in word.split(separator):
    if i: # Check if the split word is not empty.
        ans.append(i)
```