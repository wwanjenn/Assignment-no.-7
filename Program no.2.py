# Program 2: Password validator
# Create a program that check if password is valid
# The password is valid if all criteria are met:
# a. Greater than 15 letters
# b. Have at least one capital letter
# c. Have at least one number
# d. Have at least one special char (!@#$%^&*()_+ etc)
# ex.
# input: P@ssw0rd+P@ssw0rd
# ouput: Valid

# STEPS
# 1 PRINT TITLE AND GUIDLINES
print('Password Validator!')
print('Criteria:')
print('a. Greater than 15 characters')
print('b. Have at least one capital letter')
print('c. Have at least one number')
print('d. Have at least one special character')
# 2 INPUT
password = input('Password: ')
# 3 LOOP
for p in range(len(password)):
# 4 15 LETTERS
    if len(password) >= 15:
        feedbackCharactersVa = 'Password has 15 or more characters'
    else:
        feedbackCharactersIn = 'Password needs at least 15 or more characters'
# 5 1 CAPITAL LETTER
    if password.islower() == True:
        feedbackUpperCaseVa = 'Password has at least one capital letter'
    else:
        feedbackUpperCaseIn = 'Password needs at least one capital letter'
    
# 6 1 NUMBER
    if password[p] == '1' or password[p] == '2' or password[p] == '3' or password[p] == '4' or password[p] == '5' or password[p] == '6' or password[p] == '7' or password[p] == '8' or password[p] == '9' or password[p] == '0':
        passwordNum = passwordNum + 1
# 7 1 SPECIAL CHAR
    elif password[p] in range('`~!@#$%^&*()-_=+[{]}:;,<.>/?'):
        passwordSpe = passwordSpe + 1 
# 8 CALCULATE

# 9 OUTPUT

      