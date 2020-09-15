#Given a integer,return the integer with reversed digit
#the integer could be positive or negatibe

def reverse_digit(x):
    string = str(x)
    if string[0] == '-':
        print('-' + string[:0:-1])
    else:
        print(string[::-1])

reverse_digit(1234)
reverse_digit(-1234)