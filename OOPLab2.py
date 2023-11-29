class Author ():
    def __init__(self, name):
        self.name = name


class Catalog ():
    _Booklist = []

    def Search(self, search):
        self.search = search
        for i in Catalog._Booklist:
            if isinstance(self.search, int):
                if i._isbn == self.search:
                    print(i)
                elif i._dds_number == self.search:
                    print(i)
            elif isinstance(self.search, str):
                if i.title == self.search:
                    print(i)
                elif i.authors == self.search:
                    print(i)

    def Deletebook(self, deletebook):
        self.deletebook = deletebook
        if isinstance(self.deletebook, int):
            index = 0
            for book in self._Booklist:
                if (book._isbn == self.deletebook):
                    self._Booklist.pop(index)
                index += 1


class Book ():
    isbn = 1

    def __init__(self, authors, title, subject, dds_number):
        self._isbn = Book.isbn
        self.authors = authors
        self.title = title
        self.subject = subject
        self._dds_number = dds_number
        Book.isbn += 1
        # Catalog._Booklist.append([self._isbn,self.authors,self.title,self.subject,self._dds_number])
        # print (self._Booklist)

    def __str__(self):
        return f'{ self._isbn,self.authors,self.title,self.subject,self._dds_number}'

    def get_dds_number(self):
        return self._dds_number

    def set_dds_number(self, new_dds_number):
        if isinstance(new_dds_number, int):
            self._dds_number = new_dds_number

    dds_number = property(get_dds_number, set_dds_number)


# -----------------------------------------------------------------------------------
# ส่วนชื่อผู้สร้างหนังสือ
author1 = Author("Wanburhan")
author2 = Author("Chidsanupong")
author3 = Author("Pongpipat")
author4 = Author("Narunart")
author5 = Author("Kulthida")
# --------------------------------------------------------------------------------
# ส่วนเล่มหนังสือ
book1 = Book(author1.name, "How To Save Sex", "เพศศึกษา", 45)
# print (book1)
book2 = Book((author1.name, author2.name),
             "กลัวเมียกลัวหมาดีกว่า", "ปรัชญาเอาตัวรอด", 99)
# print(book2)
book3 = Book(author2.name, "How to Login To you Heart", "ปรัชญาความรัก", 14)
# print (book3)
book1.dds_number = 50
# print (book1)
# book4 = Book()
# book5 = Book()
# book6 = Book()

# ------------------------------------------------------
Catalog._Booklist.append(book1)
Catalog._Booklist.append(book2)
Catalog._Booklist.append(book3)

for i in Catalog._Booklist:
    print(i._isbn, i.authors, i.title, i.subject, i.dds_number)

# --------------------------------------------------------------------
# ส่วนค้นหา
Han = Catalog()
print("#############################################################")
print("\t\t หนังสือที่คุณค้นหาคือ\n")
Han.Search("Wanburhan")
print("\n\t     Good Luck Ang Have Fun")
print("#############################################################")
# ----------------------------------------------------------------
# ส่วนการลบหนังสือ
Han.Deletebook(1)
# print (Catalog._Booklist[0],Catalog._Booklist[1])
