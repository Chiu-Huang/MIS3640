def add_character_points():
    attribute = raw_input("\nWhich attribute? Strength, Health, Wisdom or Dexterity?\n")

    if attribute in my_character.keys():
        amount = int(raw_input("By how much?"))

        if (amount > my_character['points']) or (my_character['points'] <= 0):
            print ("Not enough points!")
        else:
            my_character[attribute] += amount
            my_character['points'] -= amount
    else:
        print ("\nThat attribute doesn't exist!\n")


def print_character():
    for attribute in my_character.keys():
        print (attribute, " : ", my_character[attribute])


##### MAIN FUNCTION #####

my_character = {'name': '', 'strength': 0, 'health': 0, 'wisdom': 0, 'dexterity': 0, 'points': 20}
running = True

print ("Create a character! You have points to assign to strength, health, wisdom, and dexterity.")

my_character['name'] = raw_input("What is your character's name? ")

while running:
    print ("\nYou have ", my_character['points'], " points left.\n")
    print ("1. Add points\n2. Remove points\n3. See current attributes\n4. Exit\n")

    choice = raw_input("Choice:")

    if choice == "1":
        add_character_points()
    elif choice == "3":
        print_character()
    elif choice == "4":
        running = False         
    else:
        pass