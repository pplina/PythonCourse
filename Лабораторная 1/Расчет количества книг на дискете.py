# TODO Найдите количество книг, которое можно разместить на дискете

diskette_capacity_bytes = 1.44 * 1024 * 1024

pages_per_book = 100
lines_per_page = 50
characters_per_line = 25
bytes_per_character = 4

book_size_bytes = pages_per_book * lines_per_page * characters_per_line * bytes_per_character
books_on_diskette = diskette_capacity_bytes // book_size_bytes

print("Количество книг, помещающихся на дискету:", round(books_on_diskette))
