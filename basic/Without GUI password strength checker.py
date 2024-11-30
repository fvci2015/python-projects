password_strength=""

def checkPass(passstr):
    global password_strength
    passlen=len(passstr)
    isLower=False
    isUpper=False
    isNumeric=False
    isSpecial=False
    inputchar="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    for i in range(passlen):
        if passstr[i].islower():
            isLower=True
        if passstr[i].isupper():
            isUpper=True
        if passstr[i].isdigit():
            isNumeric=True
        if passstr[i] not in inputchar:
            isSpecial=True
    if (isLower and isUpper and isNumeric and isSpecial and passlen>=8):
      password_strength="Strong"
    elif(isLower or isUpper) and (isSpecial or isNumeric) and passlen>=6:
        password_strength="Moderate"
    else:
        password_strength="Weak"
        
def validatepass():
    global password_strength
    passstr=input("Enter the password: ")
    checkPass(passstr)
    print("The password strength is: ",password_strength)

if __name__=="__main__":
    validatepass()
