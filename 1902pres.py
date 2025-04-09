class Book:
    def __init__(self,title,type,author,counts):
        self.book_title=title
        self.book_type=type
        self.book_author=author
        self.counts=counts

    def reading(self):
        print("------------------------------------------------------------------------------------------------------------")
        print("Now you are in reading method.")
        print(f"Your Reading the book {self.book_title}.")
    
    def display(self):
        print("------------------------------------------------------------------------------------------------------------")
        print("Now your in display method.")
        print(f"The Book Details are as follows\nTitle:{self.book_title}\nType:{self.book_type}\nAuthor:{self.book_author}\nNumber of Pages:{self.counts}")
    
    def count(self):
        print("------------------------------------------------------------------------------------------------------------")
        print("Now your in count method.")
        print(f"the number of pages present in the book {self.book_title} is {self.counts}")


n=int(input("enter the number of books : "))
lst=[]
for i in range(n):
    print("------------------------------------------------------------------------------------------------------------")
    print(f"enter the details of book {i+1}.")
    title=input("Enter the Title of book: ")
    type=input("Enter the type of the book: ")
    author=input("Enter the Author name: ")
    pages=int(input("Enter the number of pages present in this book: "))
    str=Book(title,type,author,pages)
    lst.insert(i,str)
    # print("--------------------------------------------------------------")
    # str.display()
    # str.reading()
    # str.count()
    # print("--------------------------------------------------------------")



# print(lst)
for i in lst:
    i.display()
    i.count()
    i.reading()
