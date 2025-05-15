from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

class Library:
    def __init__(self):
        self.books = []
        self.checked_out = {}  # book -> member

    def add_book(self, book):
        self.books.append(book)

    def register_member(self, member):
        print(f"Member {member.name} registered with ID {member.member_id}.")

    def is_book_available(self, book):
        return book in self.books and book not in self.checked_out

    def checkout_book(self, book, member):
        if self.is_book_available(book):
            self.checked_out[book] = member
            member.borrowed_books.append(book)
            print(f"{member.name} checked out '{book.title}'.")
        else:
            print(f"'{book.title}' is not available.")

    def return_book(self, book, member):
        if book in member.borrowed_books:
            member.borrowed_books.remove(book)
            self.checked_out.pop(book, None)
            print(f"{member.name} returned '{book.title}'.")
        else:
            print(f"{member.name} does not have '{book.title}'.")



# Hard Assignment 1
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 4, 5)

shapes = [circle, rectangle, triangle]
for shape in shapes:
    print(f"{shape.__class__.__name__} area: {shape.area():.2f}")


#Hard Assignment 2
library = Library()
book1 = Book("Python Programming", "John Smith")
book2 = Book("Data Structures", "Jane Doe")

library.add_book(book1)
library.add_book(book2)

member = Member("Alice", "M001")
library.register_member(member)

library.checkout_book(book1, member)
print(library.is_book_available(book1))  # False
print(library.is_book_available(book2))  # True

library.return_book(book1, member)
print(library.is_book_available(book1))  # True