
user_input = input("write your crontab expression - (seperate each field with a space\n")
def crontab_test(expression):
    flag = True
    parts = expression.split()
    if len(parts) != 5:
        flag = False
    print("valid" if flag else "not valid")

def valid_minutes(input):
    if len(input) <1 :
        return False
    if len(input) == 1:
        if input == '*':
            return True
        if int(input) in range(0,59):
            return True    
    else:
        return False
    if len(input) > 1:
        if len(input) == 2:
            return False
        if len(input) == 3:
            if '-' in input:
                index = input.find('-')
                if((int(input[index - 1]) in range(0,59)) and (int(input[index + 1]) in range(0,59)) and (int(input[index - 1]) < int(input[index + 1]))):
                    return True
                else:
                    return False
            else:
                if ',' in input:
                    return True #fix needed



