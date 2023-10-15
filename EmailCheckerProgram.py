# Email checker program conditions
#
# Checks if an email address meets the following criteria:
# - More than 6 letters
# - First letter is an alphabet
# - One and only one '@' sign
# - '.' sign in the third and second-to-last positions
# - Lowercase only
# - No uppercase letters
# - No spaces

email = input("Enter Your Email: ")
k, l, d = 0, 0, 0

if len(email) >= 6:
    if email[0].isalpha():
        if '@' in email and email.count('@') == 1:
            if email[-4] == '.' or email[-3] == '.':
                for i in email:
                    if i.isspace():
                        k = 1
                    elif i.isalpha() and i.isupper():
                        l = 1
                    elif i.isdigit():
                        continue
                    elif i in ['_', '.', '@']:
                        continue
                    else:
                        d = 1

                if k == 1 or l == 0 or d == 1:
                    print("Throw Error")
                else:
                    print("error 04")
            else:
                print("error 03")
        else:
            print("error 02")
    else:
        print("error 01")
else:
    print("error 01")