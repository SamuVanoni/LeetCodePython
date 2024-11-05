## What Did I Learn?

### In this challenge I learned more about logic (easy):

1. We start by separating the sentence into words
```python
words = sentence.split()
```

2. Then we see if each of these words has the beginning = a searchWord
```python
for i, word in enumerate(words):
    if word.startswith(searchWord):
        return i + 1
```