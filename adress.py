class Address:
    def __init__(self, index, city, street, home, flat):
        self.index = index
        self.city = city
        self.street = street
        self.home = home
        self.flat = flat

        

class Mailing:
    def __init__(self, to, frome, cost, track):
        self.to = to
        self.frome = frome
        self.cost = cost
        self.track = track

        to = Address ("1123411", "Капаровк", "дорожная" "54", "11")
        frome = Address ("1234565432", "Кудрянск", "парадная" "514", "54")
        cost = 16738
        track = ("12345")
        
        print(to,frome,cost, track)