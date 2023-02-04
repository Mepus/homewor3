class User:
    age = 0

    def __init__(self, name, ):
        print("я создался")
        self.username = name
        
    def sayName(self,):
        print("Меня зовут ", self.username)

    def sayAge(self):
        print(self.age)

    def setAge(self, newAge):
        self.age = newAge

    def sayEmail(self, email):
        self.sayEmail = email
        print(self.sayEmail)

    def sayFriend(self, friend):
        self.sayFriend = friend
        print("Друг ", friend)

    def addCard(self, card):
        self.card = card

    def getCard(self):
        return self.card