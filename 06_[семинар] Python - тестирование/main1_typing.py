def indent_right(s: str, width: int) -> str:
    return " " * (max(0, width - len(s))) + s

class Book:
    title: str
    author: str

    def __init__(self, title: str, author: str, cost: int) -> None:
        self.title = title
        self.author = author
        self.cost = cost

b = Book(title='Fahrenheit 451', author='Bradbury', cost='3,14')