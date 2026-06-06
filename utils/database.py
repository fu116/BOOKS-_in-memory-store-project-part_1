books_file="books.txt"
# books=[]


def add_book(name, author):
    with open(books_file, 'a') as file:
       file.write(f'{name},{author},0\n')
   #  books.append(
   #       {
   #          "name": name,
   #          "author":author,
   #          "read":False
   #       })

def list_book():
    with open(books_file , "r") as file:
        books=file.readlines()
        strip_books=[book_info.strip() for book_info in books if book_info.strip()]
        split_books=[book.split(",") for book in strip_books]
        

    return [ 
             {"name": I[0].strip(), 
              "author": I[1].strip(), 
              "read": I[2].strip()
              }
       
            for I in split_books
        ]

   #  for book in books:
   #      read = "YES ✅" if book['read'] else "NO ❎"
   #     print(f"{book["name"]} by {book["author"]} , read: {read}"  )




def mark_as_read_book(name):
     books=list_book()
     for book in books:
        if name == book["name"]: 
            book["read"]="1"
            print(f"Success! '{name}' has been marked as read  ✅.") 
     _save_all_books(books)


def _save_all_books(books):
    with open(books_file , "w") as file:
        for book in books:
            file.write(f"{book['name'].strip()},{book['author'].strip()},{book['read'].strip()}\n")
   #   for book in books:
   #      if name == book["name"]: 
   #          book["read"]=" YES ✅"
   #          print(f"Success! '{name}' has been marked as read.") 


def delete_book(name):
    books=list_book()
    books=[ book for book in books
             if name != book["name"]]
    _save_all_books(books)


   # global books
   # books = [book for book in books if name != book["name"]]
    
    
