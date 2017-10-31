class Time:
    """
    Represents the time of day.

    attributes: hour, minute, second
    """


def int_to_time(seconds):
    """Makes a new Time object.

    seconds: int seconds since midnight.
    """

    minutes, second = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)

    return Time(hour, minute, second)


start = Time(9, 45, 0)

start.print_time()
print(start.time_to_int())

end = start.increment(2000)
end.print_time()
print(end.is_after(start))

traffic = Time(0, 30, 0)

expected_time = Time(10, 15, 0)

traffic.print_time()
expected_time.print_time()
print(start.is_as_expected(traffic, expected_time))

default_time = Time()
default_time.print_time()
