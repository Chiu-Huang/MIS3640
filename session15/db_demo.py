import dbm
import random

ROSTER = ('Istvan Bardi',
            'Zachary Bedrosian',
            'Josephine Boenawan',
            'Gianca Devina',
            'Winfred Fields',
            'Tarika Gadh',
            'Dagim Girma',
            'Paul Han',
            'Julia Harrigan',
            'Stephanie Herrera',
            'Ching Chiu Huang',
            'Christopher Kennedy',
            'Xiang Li',
            'Alex Lim',
            'Xuhe Lu',
            'Lauren Mendez',
            'Julian Mullins',
            'Austin Pearl',
            'Andrew Piispanen',
            'Regine Fae Serafico',
            'Malachi Stoll',
            'Theresia Susanto',
            'Huateng Zhang')
GRADES = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-']

db = dbm.open('db_student', 'c')

for student in ROSTER:
    db[student] = random.choice(GRADES)

for key in db:
    print(key, db[key])


db.close()