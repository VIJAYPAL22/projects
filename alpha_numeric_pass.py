# to get the pass
# check alpha num
# char more that 8 and less than 20
pwd = input("enter your password ")
if(pwd.isalnum()  and not pwd.isalpha() and not pwd.isdigit()):
    if(len(pwd)>8 and len(pwd)<20):
        print("Your pass is okay")
    else:
        print("Sorry your password is not okay. it should be more than 8 and less than 20 characters")
else:
    print("Your password is not okay it should hold both alpha and numeric values")