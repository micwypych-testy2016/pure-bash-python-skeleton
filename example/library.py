
def fizz_buzz(value):
    s = ''
    if value % 3 == 0:
       s = 'Fizz'
    if value % 5 == 0:
       s = 'Buzz'
    if value % 3 != 0 and value % 5 != 0:
       s = str(value)
    return s
