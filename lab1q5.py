#Define a function is_password_strong that takes as argument a password and determines
#whether the password is strong or weak. It returns True if the password is strong and False
#otherwise. A password is strong if (1) it contains at least 8 characters, (2) it contains at least
#one digit, and (3) it contains at least one uppercase letter.



has_digit=False
has_upper=False
def is_password_strong(pw):

    

    for ch in pw:
        if ch.isdigit():      # check if character is 0–9
            has_digit = True
        if ch.isupper():      # check if character is uppercase
            has_upper = True

    if (len(pw)>7) and has_digit==True and has_upper==True:
        return True
    else:
        return False
    
password=str(input("enter a strong password "))

print(is_password_strong(password))

if (is_password_strong(password))==True:
    print(" it is a strong password")
else:
    print("it is a weak password")





