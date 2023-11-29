class Note ():
    id_note = 1 
    def __init__(self, memo, creation_date,tags):
        self.memo = memo
        self.creation_date = creation_date
        self.tage = tags
        Note.id_note += 1

    @staticmethod
    def __str__(memo, tage, creation_date) :
        return f'{memo,tage,creation_date}'
    
    @staticmethod
    
    def Match (memo, tags):
        for memo in 

