# Dictionaries: (Understand the basics of dictionaries in Python. ) Write a python program that takes in a dictionary of books such that
# it can implement CRUD functionalities on the data structure. 
# For example => 

books = {
        '1':{
        'author':"Jeffrey Brown",
        'title': 'Cosnic Cadet',
        'year':2023,
        'ISBN': 100
        }, 
          '2':{
        'author': "Jeremy Tinder",
        'title': "Black GhostApple Factory",
        'year':2006,
        'ISBN': 10023
        }, 
          '3':{
        'author': "Dean Haspiel",
        'title': "Boy in My Pocket",
        'year':2010,
        'ISBN': 1005676
        }, 
          '4':{
        'author': "Simon",
        'title': "The 120 days of Simon",
        'year':2022,
        'ISBN': 10022
        }, 
        "5":{
            "author": "James K.",
            "title": "American Elf 2001",
            "year": "2001",
            "ISBN": 101
        },
        '6':{
        'author': 'FaithK',
        'title': 'How to win',
        'year':2020,
        'ISBN': 100
        }, 
        '7':{
        'author': 'Kym',
        'title': 'How to Sleep',
        'year':2023,
        'ISBN': 10032
        },
      

}
# displaying books

# print(books)
for x, y in books.items():
  print(x, y)

# delete books
del books["4"]
for x, y in books.items():
  print(x, y)

# Find a books based on its ISBN number
daf = books.keys()
print(daf)

dat = books.values()
print(dat)
#Add a new book in the dictionary
# books[key]=value
# books[1] = {'author': 'Jeffrey Brown', 'title': 'Cosnic Cadet', 'year': 2023, 'ISBN': 1020}
books[8] = {'author': 'Admiral  Tibet', 'title': 'Do you believe it', 'year': 2015, 'ISBN': 110}
print(books)
# Retrieve a book based on Author 

# Update a title of the book
books["7"]["year"] = 2026
for x, y in books.items():
  print(x, y)