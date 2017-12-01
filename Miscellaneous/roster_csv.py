import random
import csv


def call(filename):
    '''
    Among the names that are called least times,
    return one name randomly. Update database after each call.

    db_name: the name of database
    
    returns one name
    '''
    roster = display_all(filename)
    visits_list = []
    for student in roster:
        visits_list.append(roster[student])
    min_visits = min(visits_list)
    names = []
    for student in roster:
        if roster[student] == min_visits:
            names.append(student)

    name_to_update = random.choice(names)
    roster[name_to_update] += 1

    with open(filename, mode='w', newline='') as fp:
        writer = csv.writer(fp)
        for name, number in roster.items():
            writer.writerow([name, number])

    return name_to_update


def display_all(filename):
    '''
    display all names and values

    db_name: the name of database
    '''
    with open(filename, mode='r') as fp:
        reader = csv.reader(fp)
        roster = {row[0]: int(row[1]) for row in reader}
    return roster


def main():
    ROSTER_FILE = 'code_chat.csv'
    # print(display_all(ROSTER_FILE))
    print(call(ROSTER_FILE))
    # print(display_all(ROSTER_FILE))

if __name__ == '__main__':
    main()
