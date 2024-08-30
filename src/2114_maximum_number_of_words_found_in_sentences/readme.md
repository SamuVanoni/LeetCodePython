## What Did I Learn?

### In this challenge I found a more complex solution and looking at other users' solutions I realized that it could be simpler (one line):

1. My solution
```python
count = 1
countMax = 0
for i in range(len(sentences)):
    for j in range(len(sentences[i])):
        if sentences[i][j] == " ":
            count += 1
    if count > countMax:
        countMax = count
    count = 1
return countMax
```
My solution uses less memory. We use 2 loops to go through each letter of each word in the list and if that letter is equal to Space we add the count.


2. User's solution
```python
return max(len(word.split()) for word in sentences)
```
The user's solution breaks the sentence into words (separated by space) and then counts how many words were generated after breaking.