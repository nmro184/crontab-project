
user_input = input("write your crontab expression - (seperate each field with a space\nnote - use either step - '/x' range - 'x-y' or a list - x,y,z\n" )
ALLOWED_MINUTES_RANGE = range(0,59)
def crontab_test(expression):
    flag = True
    parts = expression.split()
    if len(parts) != 5:
        flag = False
    print("valid" if flag else "not valid")

def valid_minutes(input):
    if len(input) <1 : #checking for * or a single number
        return False
    if input == '*':
        return True
    if len(input) == 1:
        if int(input) in ALLOWED_MINUTES_RANGE:
            return True   
        else:
            return False 
    else:
        if len(input) > 1:
            if len(input) == 2:#checking for step
                if '/' in input:
                    if input[1] in ALLOWED_MINUTES_RANGE:
                        return True
                    else:
                        return False
                else:
                    return False
            if len(input) == 3: #checking for a range/short list
                if '-' in input:
                    index = input.find('-')
                    if((input[0] in ALLOWED_MINUTES_RANGE) and (input[3] in ALLOWED_MINUTES_RANGE) and (input[0] < input[3])):
                        return True
                    else:
                        return False
                else:
                    if ',' in input:
                        if input[0] in ALLOWED_MINUTES_RANGE and input[3] in ALLOWED_MINUTES_RANGE:
                            return True
                        else:
                            return False
                    else:
                        return False      
            else: #checking for a long list
                i=0
                while i < len(input):
                    if i%2 == 0:
                        if int(input[i] not in ALLOWED_MINUTES_RANGE):
                            return False
                    else:
                        if input[i] != ',':
                            return False



