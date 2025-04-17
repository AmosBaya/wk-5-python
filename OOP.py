class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def best_seller(self):
        print(f"{self.title} is a best seller!")

    def available(self):
        print(f"{self.title} is available!")

Book1 = Book("True Revival", "Ellen G White", 100)
Book2 = Book("Desire of Ages", "Ellen G White", 1000)

print(Book1.title)
print(Book1.author)
print(Book1.pages)
Book1.best_seller()
print(Book2.title)
print(Book2.author)
print(Book2.pages)
Book2.available()

# inheritance + polimophism
class Magazine(Book):
    def best_seller(self):
        print(f"{self.title} is not a best seller!")
    

class Newspaper(Book):
    def best_seller(self):
        print(f"{self.title} is not a best seller!")

    def copies_available(self, copies):
        print(f"{self.title} has {copies} copies available.")

class Journal(Book):
    def best_seller(self):
        print(f"{self.title} is yet to be a best seller!")


magazine = Magazine("Fashion", "Margaret Atwood", 50)
newspaper = Newspaper("Kenya Navy scandle", "Jicho Pevu", 20)
journal = Journal("Science", "Albert Einstein", 200)

print(magazine.title)
print(magazine.author)
print(magazine.pages)
magazine.best_seller()

print(newspaper.title)
print(newspaper.author)
print(newspaper.pages)
newspaper.copies_available(1000)
newspaper.best_seller()

print(journal.title)
print(journal.author)
print(journal.pages)
journal.best_seller()
