
ALLOWED_MINUTES_RANGE = range(0,60)
ALLOWED_HOURS_RANGE = range(0,24)
ALLOWED_DAY_OF_MONTH_RANGE = range(1,32)
ALLOWED_MONTH_RANGE = range(1,13)
ALLOWED_DAY_OF_WEEK_RANGE = range(0,7)

def crontab_test(expression):
    parts = str(expression).split()
    if len(parts) != 5:
        return False
    result = (
        valid_minutes(parts[0]) and
        valid_hours(parts[1]) and
        valid_day_of_month(parts[2]) and
        valid_month(parts[3]) and
        valid_day_of_week(parts[4])
    )
    print(result)
    return result

def astrix_or_digit_test(input , range):
    if '*' in input:
        if input == '*':
            return True
        else:
            return False
        
    if input.isdigit():
        if int(input) in range:
            return True
        else:
            return False
    return False

def step_test(input , range):
    if '/' in input:
        if input.startswith('/') and (int(input[1:]) in range):
            return True
        else:
            return False
    return False

def range_test(input,range):
    if '-' in input:
        parts = input.split('-')
        if((int(parts[0]) in range) and (int(parts[1]) in range) and (int(parts[0]) < int(parts[1]))):
            return True
        else:
            return False
    return False

def list_test(input,range):
    if ',' in input:
        parts = input.split(',')
        for part in parts:
            if int(part) not in range:
                return False
        return True
    return False

def valid_input(input , range):
    return astrix_or_digit_test(input ,range) or step_test(input ,range) or range_test(input ,range) or list_test(input ,range)

def valid_minutes(input):
    return valid_input(input , ALLOWED_MINUTES_RANGE)

def valid_hours(input):
    return valid_input(input , ALLOWED_HOURS_RANGE)

def valid_day_of_month(input):
    return valid_input(input , ALLOWED_DAY_OF_MONTH_RANGE)

def valid_month(input):
    return valid_input(input , ALLOWED_MONTH_RANGE)

def valid_day_of_week(input):
    return valid_input(input , ALLOWED_DAY_OF_WEEK_RANGE)


user_input = input("write your crontab expression - (seperate each field with a space)\nnote - use either step - '/x' range - 'x-y' or a list - x,y,z\n" )
crontab_test(user_input)