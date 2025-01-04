## What Did I Learn?

### In this challenge I learned a new form to solve problems:

1. In it we create a list that will have elements removed and added as needed, and if there are no elements in it yet, we add 1 to the count.
```python
if ch == '[': # If = '[' add to stack
    stack.append(ch)
else:
    if stack: # If = ']' and there is already '[' in the stack, remove 1 element
        stack.pop()
    else: # Count one if you don't have a stack
        count += 1
```