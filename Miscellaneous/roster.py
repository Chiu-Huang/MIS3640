roster = ['Istvan Bardi',
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
            'Huateng Zhang']



import random
def call_three(roster):
    """
    print three names randomly

    roster: a list of strings
    """
    # for i in range(1):
        # print(random.choice(roster))
    print(random.sample(roster, 3))

call_three(roster)
