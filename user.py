class User:
    name = 'No name'
    lastname = 'No last name'


    def __init__(self, first_name, last_name):
        self.name = first_name
        self.lastname = last_name
        
    def sayname(self):
        print(self.name)


    def saylastname(self):
        print(self.lastname)


    def firts_last_name(self):
        print(self.name, self.lastname)


newUser = User('Степа', 'Карибов')
newUser.sayname()
newUser.saylastname()
newUser.firts_last_name()

