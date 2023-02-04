from userlesson import User
from card import Card
alex = User("Alex")

alex.sayName()
alex.setAge(33)
alex.sayAge()
alex.sayEmail("Mepsuf@amfw.com")
alex.sayFriend("Mark")

card = Card("1234 1748 1847 1747", "11/28", "Alex F")
alex.addCard(card)
alex.getCard().pay(1000)