from Person import Person


class BabsonPerson(Person):
    nextIdNum = 0
    # next ID number to assign

    def __init__(self, name):
        # initialize Person attributes
        Person.__init__(self, name)
        # new BabsonPerson attribute: a unique ID number
        self.idNum = BabsonPerson.nextIdNum
        BabsonPerson.nextIdNum += 1

    # sorting Babson people uses their ID number, not name!
    def __lt__(self, other):
        return self.idNum < other.idNum

    def speak(self, utterance):
        return (self.name + " says: " + utterance)


# p1 = BabsonPerson('Zhi Li')
# p2 = BabsonPerson('Alex Lim')
# p3 = BabsonPerson('Steve Bardi')
# p4 = Person('Chris Kennedy')
