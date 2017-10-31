from datetime import datetime
from Time import *


def days_until_birthday(birthday):
    """How long until my next birthday?"""


def double_day(b1, b2):
    """Compute the day when one person is twice as old as the other.

    b1: datetime birthday of the younger person
    b2: datetime birthday of the older person
    """


def datetime_exercises():
    """Exercise solutions."""

    # print today's day of the week
    today = datetime.today()
    print(today.weekday())
    print(today.strftime('%A'))

    # compute the number of days until the next birthday
    # (note that it usually gets rounded down)
    birthday = datetime(1997, 4, 1)
    print('Days until birthday', end=' ')
    print(days_until_birthday(birthday))

    # compute the day one person is twice as old as another
    b1 = datetime(2017, 12, 26)
    b2 = datetime(2017, 11, 02)
    print('Double Day', end=' ')
    print(double_day(b1, b2))


def main():
    # if a movie starts at noon...
    noon_time = Time()
    noon_time.hour = 12
    noon_time.minute = 0
    noon_time.second = 0

    print('Starts at', end=' ')
    print_time(noon_time)

    # and the run time of the movie is 109 minutes...
    movie_minutes = 109
    run_time = int_to_time(movie_minutes * 60)
    print('Run time', end=' ')
    print_time(run_time)

    # what time does the movie end?
    end_time = add_time(noon_time, run_time)
    print('Ends at', end=' ')
    print_time(end_time)

    print('Does it end after it begins?', end=' ')
    print(is_after(end_time, noon_time))

    print('Home by', end=' ')
    travel_time = 600      # 10 minutes
    home_time = increment(end_time, travel_time)
    print_time(home_time)

    race_time = Time()
    race_time.hour = 1
    race_time.minute = 34
    race_time.second = 5

    print('Half marathon time', end=' ')
    print_time(race_time)

    distance = 13.1       # miles
    pace = mul_time(race_time, 1 / distance)

    print('Time per mile', end=' ')
    print_time(pace)

    datetime_exercises()


if __name__ == '__main__':
    main()
