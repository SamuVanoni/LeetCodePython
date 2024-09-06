## What Did I Learn?

### In this challenge I learned more about logic:

1. We start the problem by creating a mapping:
```python
translation = {
    "(": ")",
    "[": "]",
    "{": "}"
}
```

2. Then we add every opening character to an array:
```python
if char in translation:
    stack.append(char)
```

3. Then we deal with errors on other occasions:
```python
elif char in translation.values(): # If closing character
    if not stack or translation[stack.pop()] != char:
        return False
else: # If another character
    return False
```
If the stack is empty or if the element that closes is different from the one that opens, we return false