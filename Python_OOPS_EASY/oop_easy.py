class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)



class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

    def reset(self):
        self.value = 0




#EASY ASSIGNMENT 1

rect = Rectangle(5, 10)
print(rect.area())       # Output: 50
print(rect.perimeter())  # Output: 30

# EASY ASSIGNMENT 2

counter = Counter()
counter.increment()
counter.increment()
print(counter.value)  # Output: 2
counter.decrement()
print(counter.value)  # Output: 1
counter.reset()
print(counter.value)  # Output: 0
