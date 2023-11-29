from datetime import datetime


class Note:
    _pageofnotes = 0

    def __init__(self, memo, tags):
        Note._pageofnotes += 1
        self._id = Note._pageofnotes
        self._memo = memo
        self._creation_date = datetime.now().strftime('%d-%m-%Y')
        self._tags = tags

    @staticmethod
    def match (note, seach_filter):
        if seach_filter in note.tags or seach_filter in note.memo:
            return True
        return False

    def get_memo(self):
        return self._memo

    def set_memo(self, new_memo):
        self.memo = new_memo
    memo = property(get_memo, set_memo)

    def get_tags(self):
        return self._tags

    def set_tags(self, new_tags):
        self.tags = new_tags
    tags = property(get_tags, set_tags)

    def get_id(self):
        return self._id

    def set_id(self, new_id):
        self._id = new_id
    id = property(get_id, set_id)


class Menu():
    def __init__(self, books):
        self._books = books

    def showmenu(self):
        print("1. Show Note \n2. Add Note\n3. Edit Note\n4. Edit tags\n5.Exit")
        choose_menu = int(input("Please Enter Number 1-5 :"))
        if choose_menu == 1:
            self.search_note()
        elif choose_menu == 2:
            self.add_note()
        elif choose_menu == 3:
            self.modify_note()
        elif choose_menu == 4:
            self.modify_tags()
        elif choose_menu == 5:
            self.exit_manu()

    def show_note(self, id):
        for check in self._books.notes:
            if check.id == id:
                print("ID :", check.id, "\nMemo :", check.memo,
                      "\nTags :", check.tags, "\nTime :", check._creation_date)

    def search_note(self):
        search_note = input("Enter You search: ")
        search5 = self._books.search(search_note)
        for check in search5:
            self.show_note(check.id)

    def add_note(self):
        memo = input("Memo: ")
        tags = input("Tags: ")
        self._books.new_note(memo, tags)

    def modify_note(self):
        note_id = int(input("NoteID :"))
        memo = input("Memo :")
        self._books.modify_memo(note_id, memo)

    def modify_tags(self):
        note_id = int(input("Enter Note ID :"))
        tags = input("Tags :")
        self._books.modify_tags(note_id, tags)

    def exit_manu():
        exit()


class NoteBook():
    notes = []

    def search(self, filter):
        searchlist = []
        if (isinstance(filter, str)):
            for note in self.notes:
                if (Note.match(note, filter)):
                    searchlist.append(note)

            return searchlist

    def new_note(self, memo, tags):
        new_note_list = Note(memo, tags)
        self.notes.append(new_note_list)

    def modify_memo(self, note_id, memo):
        for check in self.notes:
            if note_id == check._id:
                check._memo = memo

    def modify_tags(self, note_id, tags):
        for check in self.notes:
            if note_id == check._id:
                check._tags = tags


It_is_a_Book = NoteBook()

while True:
    Runmenu = Menu(It_is_a_Book)
    Runmenu.showmenu()
