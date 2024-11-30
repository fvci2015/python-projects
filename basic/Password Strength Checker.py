import customtkinter as ctk
password_strength=""    

def checkPass(passstr):
    global password_strength
    passlen=len(passstr)
    isLower=False
    isUpper=False
    isSpecial=False
    isNumeric=False
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


def validatePass():
    global password_strength
    global passEntry
    password=passEntry.get()
    global strengthLabel
    checkPass(password)
    strengthLabel.configure(text="Password strength is: "+password_strength)
    if password_strength=="Weak":
        strengthLabel.configure(text_color='red')
    elif password_strength=="Moderate":
        strengthLabel.configure(text_color='yellow')
    else:
        strengthLabel.configure(text_color='green')





ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root=ctk.CTk()
root.geometry("700x450")

frame=ctk.CTkFrame(master=root)
frame.pack(pady=30,padx=10,fill="both",expand=True)

passEntry=ctk.CTkEntry(master=frame,placeholder_text="Enter your password")
passEntry.pack(pady=20,padx=5,fill="both")

strengthcheck=ctk.CTkButton(master=frame,text="CheckPasswordStrength",command=validatePass)
strengthcheck.pack(pady=20,padx=5,fill="both")

strengthLabel=ctk.CTkLabel(master=frame,text="")
strengthLabel.pack(pady=20,padx=5)
root.mainloop()