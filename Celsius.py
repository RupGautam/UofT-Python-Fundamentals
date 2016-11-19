def convert_to_celsius(fahrenheit):
    '''(number) -> number
    Return the number of celsius degree equivalent to fahrenheit degree.
    >>> convert_to_celsius(32)
    0.0
    >>> convert_to_celsius(212)
    100.0
    '''
    return (fahrenheit - 32) / 2
def colder_temperature(temp1, temp2):
    ''' (number,number) -> number
    Return the colder of the two temperature, temp1 (degree Celsius)
    and temp2 (degree Fahrenheit), in degree Celsius.
    '''
    temp2_celsius = convert_to_celsius(temp2)
    return min(temp1, temp2_celsius)

def usa_city_temperature(us_city):

    us_temp = convert_to_celsius(us_city)
    return (us_temp)

    

