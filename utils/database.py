books=[]




def add_book(name, author):
    books.append(
         {
            "name": name,
            "author":author,
            "read":False
         })


def list_book():
    for book in books:
        read = "YES ✅" if book['read'] else "NO ❎"
        print(f"{book["name"]} by {book["author"]} , read: {read}" )




def mark_as_read_book(name):
     for book in books:
        if name == book["name"]: 
            book["read"]="YES ✅"
            print(f"Success! '{name}' has been marked as read.") 




def delete_book(name):
   global books
   books = [book for book in books if name != book["name"]]

#    for book in books :
#       if name == book["name"]:
#          books.remove(book)        
