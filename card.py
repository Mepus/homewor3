class Card:
    number = '0000 0000 0000 0000'
    validDate = '01/99'
    holder = 'unknow'

    def __init__(self, number, date, holder):
        self.holdef = holder 
        self.number = number
        self.validDate = date


    def pay(self, amount):
        print("скарты ", self.number, "списали", amount)
        