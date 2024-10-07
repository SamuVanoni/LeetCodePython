## What Did I Learn?

### In this challenge I learned more about logic:

1. After identifying how to make the pattern, we created a function to make it
```python
def find(w):
    l = []
    m = defaultdict(int)
    i = 0
    for c in w:
        if c in m:
            l.append(m[c])
        else:
            i += 1
            m[c] = i
            l.append(m[c])
    return l
```
    - This function creates a letter -> integer dictionary.
    - If the letter is already "registered" we add its respective integer value to the list.
    - If it is not "registered" -> sum 1, add it to the dictionary and place the numerical value in the array.