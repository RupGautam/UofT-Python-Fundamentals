def convert_to_minutes(num_hrs):
    ''' (int) -> int
    Return the number of minutes there are in num_hrs hours.

    >>> convert_to_minutes(2)
    120
    '''
    result = num_hrs * 60
    return result

hours_asleep = 5
minutes_asleep = convert_to_minutes(hours_asleep)
print ("I'm still tired.")
