
class Book:

    def __init__(self,title,author,genre):

        self.title=title
        self.author=author
        self.genre=genre

    def __eq__(self, value): 

        if self.title==value.title and self.author==value.author:
            return True
        else: return False

    def __str__(self):
        return f"title : {self.title} \n author : {self.author} \n genre : {self.genre} "
    
class BookLimitError(Exception):
    pass
    
class User:

    def __init__(self):
        self.__borrowed_books=[]

    def borrow_book(self,book):
        
        try:
            if len(self.__borrowed_books)>=3:
                raise BookLimitError ("Borrowing limit exceed!")
            else:
                if book in self.__borrowed_books:
                    print("\n ALready in the borrowed list")
                else:
                    self.__borrowed_books.append(book)
                    print("\n book borrowed ")

        except BookLimitError as e:
            print(e)

    def return_book(self,book):

        if book not in self.__borrowed_books:
            print("\n book not borrowed yet!")
        else:
            self.__borrowed_books.remove(book)
            print("\n book returned")

    def show_borrowed_books(self):

        if not self.__borrowed_books:
            print("there is no book borrowed yet!")
        else:
            for books in self.__borrowed_books:
                print(books)

class Library:

    def __init__(self):
        self.__booklst=[]

    def add_book(self,book):

        if book in self.__booklst:
            print("Already in the library")
        else:
            self.__booklst.append(book)
            print("book added to library")

    def search_book(self,keyword):

        keyword=keyword.lower()
        result=[]

        for book in self.__booklst:

            if ( keyword in book.title.lower() or keyword in book.author.lower() or keyword in book.genre.lower() ):
                result.append(book)
            if result:
                for books in result:
                    print(books)
            else:
                print("book not found!")

    def __add__(self,book):

        if book in self.__booklst:
            print("Already in the library")
        else:
            self.__booklst.append(book)
            print("book added to library")
        
        return self

    def __len__(self):
        return len(self.__booklst)
    
    def __contains__(self,book):
        return book in self.__booklst
    
    def __str__(self):

        if self.__booklst==[]:
            return "no book yet!"

        else:
            str_book=[]
            for book in self.__booklst:
                str_book.append(str(book))

            return "\n".join(str_book)

def main():

    lib=Library()
    abc=User()

    while True:

        print("\n LIBRARY MENU \n")
        print("1- add book")
        print("2- show all books")
        print("3- search book")
        print("4- check book in library")
        print("5- borrow book from library")
        print("6- return book to library")
        print("7- show borrowed books from library")
        print("8- total number of books in library")
        print("9- exit")

        choice=int(input("\n enter your choice : "))

        if choice==1:

            title=input("enter title : ")
            author=input("enter author : ")
            genre=input("enter genre : ")
            book=Book(title,author,genre)
            lib+book

        elif choice==2:

            print("\n Library collection \n")
            print(lib)

        elif choice==3:
            
            keyword=input("enter title / author / genre to search : ")
            print("\n searching book!")
            lib.search_book(keyword)

        elif choice==4:

            title=input("enter title : ")
            author=input("enter author : ")
            genre=input("enter genre : ")
            book=Book(title,author,genre)
            if book in lib:
                print("\n book found..")
            else:
                print("\n book not found!")

        elif choice==5:

            title=input("enter title : ")
            author=input("enter author : ")
            genre=input("enter genre : ")
            book=Book(title,author,genre)
            if book in lib:
                abc.borrow_book(book)
            else:
                print("\n book not found in the library!")

        elif choice==6:

            title=input("enter title : ")
            author=input("enter author : ")
            genre=input("enter genre : ")
            book=Book(title,author,genre)
            if book in lib:
                abc.return_book(book)
                
        elif choice==7:

            print("\n borrowed books : \n")
            abc.show_borrowed_books()

        elif choice==8:

            print("\n total no. of books in library : ",len(lib))

        elif choice==9:

            print("exiting.....")
            print("GOODBYE!")
            break
            
        else:
            print("Invalid selection!!!")


if __name__=="__main__":

    main()



