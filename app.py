from utils import database 


USER_CHOICE= """
Enter:
"a" to add a new book 
"l" to list all books
"r" to mark a book as read 
"d" to delete a book
"q" to quit
:
"""

def prompt_add_book():
   name=input("Enter book name: ")
   author=input("enter book author: ")
   database.add_book(name, author)



def prompt_list_book():
   books=database.list_book()   
   for book in books:
      read = "YES ✅" if book["read"]=="1" else "NO ❎"
      print(f"{book["name"]} by {book["author"]} , read: {read}"  )
         

def prompt_read_book():
        name=input("Enter the name of the book  you just finished reading : ")    
        database.mark_as_read_book(name)


def prompt_delete_book():
     name=input("Enter book name: ")
     database.delete_book(name)




operations = {
    "a": prompt_add_book,
    "l":prompt_list_book,
    "r":prompt_read_book,
    "d":prompt_delete_book
}

def menu():
  input_menu=input(USER_CHOICE).lower().strip()

  while input_menu!="q":
      if input_menu in operations:
         my_operation=operations[input_menu]
         my_operation() 
       
      else:
         print("invalid input!")            
       
      input_menu=input(USER_CHOICE).lower().strip()

       
menu()














