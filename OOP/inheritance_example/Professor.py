import random
from BabsonPerson import BabsonPerson

class Professor (BabsonPerson):
    def __init__(self, name, course):
        BabsonPerson.__init__(self, name)
        self.course = course
    
    def speak (self, utterance):
        newUtterance = "in course" + self.course +"we say"
        return BabsonPerson.speak(self, newUtterance + utterance)
    
    def lecture (self, topic):
        return self.speak ("it's obvious that " + topic)

def main():
    s1 = Professor('ABC', "MIS3650")
    print(s1.speak('where is the quiz?'))

if __name__ == '__main__':
    main()