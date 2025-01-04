## What Did I Learn?

### In this challenge I learned:

1. We created a self.space list to initialize parking with three types of spaces
```python
def __init__(self, big, medium, small):
    self.space = [0, big, medium, small]
```

2. Park your car if there are spaces available
```python
def addCar(self, carType):
    if self.space[carType] > 0:
        self.space[carType] -= 1
        return True
    else:
        return False
```