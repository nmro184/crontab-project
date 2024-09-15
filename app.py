
ALLOWED_MINUTES_RANGE = range(0,60)
ALLOWED_HOURS_RANGE = range(0,24)
ALLOWED_DAY_OF_MONTH_RANGE = range(1,32)
ALLOWED_MONTH_RANGE = range(1,13)
ALLOWED_DAY_OF_WEEK_RANGE = range(0,7)




def main():
    user_input = input("write your crontab expression - (seperate each field with a space)\nnote - use either step - '/x' range - 'x-y' or a list - x,y,z\n" )
    if valid_crontab_input(user_input):
        print (input_translator(user_input))
    else:
        print('invalid input')
    return

    

def valid_crontab_input(expression):
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

def crontab_translator(input:list):
    return minutes_translator(input[0])

def minutes_translator(input):
    output_string =''
    if input.isdigit():
        output_string += f'at minute {input}'
    
    if '*' in input:
        output_string += f'every minute'

    if '/' in input:
        output_string += f'every {input[1:]} minutes'

    if '-' in input:
        output_string += f'between minutes {input}'
    
    if ',' in input:
        output_string += f'at minutes {input}'
    
    return output_string

def hours_translator(input):
    output_string =''
    if input.isdigit():
        output_string += f'of hour {input}'
    
    if '*' in input:
        output_string += f'every hour'

    if '/' in input:
        output_string += f'every {input[1:]} hours'

    if '-' in input:
        output_string += f'of hours {input}'
    
    if ',' in input:
        output_string += f'of hours {input}'
    
    return output_string

def days_of_month_translator(input):
    output_string =''
    if input.isdigit():
        output_string += f'of the {input} of '
    
    if '*' in input:
        output_string += f''

    if '/' in input:
        output_string += f'every {input[1:]} days'

    if '-' in input:
        output_string += f'between the {input} of'
    
    if ',' in input:
        output_string += f'on days {input}'
    
    return output_string

def number_to_month(number):
    months = ["", "January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"]
    
    if number in range(1-13):
        return months[number] 
    
    else: return ''

def month_translator(input):
    output_string =''
    if input.isdigit():
        output_string += number_to_month(input)
    
    if '*' in input:
        output_string += f'any month'

    if '/' in input:
        output_string += f'every {input[1:]} months'

    if '-' in input:
        months = input.split('-')
        month1 = number_to_month(months[0])
        month2 = number_to_month(months[1])
        output_string += f'{month1} to {month2}'
    
    if ',' in input:
        months = input.split(',')
        for month in months:
            output_string += number_to_month(month) + " "

    return output_string

def number_to_weekday(number):
    days = ["", "Monday", "Tuesday", "Wednesday", "Thursday", 
            "Friday", "Saturday", "Sunday"]
    
    if int(number) in range(1-31):
        return days[int(number)] 
    
    else: return ''

def weekday_translator(input):
    output_string =''
    if input.isdigit():
        output_string += number_to_weekday(input)
    
    if '*' in input:
        output_string += f'any day of the week'

    if '/' in input:
        output_string += f'every {input[1:]} day of the week'

    if '-' in input:
        days = input.split('-')
        day1 = number_to_weekday(days[0])
        day2 = number_to_weekday(days[1])
        output_string += f'{day1} to {day2}'
    
    if ',' in input:
        days = input.split(',')
        for day in days:
            output_string += number_to_weekday(day) + " "

    return output_string

def input_translator(input):
    output_string =''
    inputs = input.split()
    output_string += minutes_translator(inputs[0])
    output_string += hours_translator(inputs[1])
    output_string += days_of_month_translator(inputs[2])
    output_string += month_translator(inputs[3])
    output_string += weekday_translator(inputs[4])

    return output_string


main()