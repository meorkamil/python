class Book:

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def show_details(self):
        print(self.title)
        print(self.pages)

    def original_pages(self):
        return self.pages


class Entry(Book):

    def add_pages(self, no_pages):
        current_pages = super().original_pages()
        total_pages = current_pages + no_pages
        return total_pages       
    


harry = Entry("Harry Potter", 250)
harry.show_details()
print(harry.add_pages(50))