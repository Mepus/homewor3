class Smartphone:
    marka = 'марка телефона'
    mode = 'модель телефона'
    number = 'абонентский номер'


    def __init__(self, markPhone, modePhone, numberPhone):
        self.marka = markPhone
        self.mode = modePhone
        self.number = numberPhone
        print(self.marka)
        print(self.mode)
        print(self.number)
        
        