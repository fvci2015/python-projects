import customtkinter as ctk 
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root=ctk.CTk()
root.geometry("400x400")

result=""
def CheckAnagram(str1,str2):
    global result
    if sorted(str1)==sorted(str2):
        result="Anagram"
    else:
        result="Not Anagram"


def validateAnagram():
    global result
    global stringEntry1
    global strinEntry2
    global anagramButton
    str1=stringEntry1.get().lower()
    str2=strinEntry2.get().lower()
    CheckAnagram(str1,str2)
    if result=="Anagram":
        anagramButton.configure(text=result,width=100,fg_color="green",text_color="black")
    else:
        anagramButton.configure(text=result,width=130,fg_color="red",text_color="black")

frame=ctk.CTkFrame(master=root)
frame.pack(pady=30,padx=10,fill="both",expand=True)

stringEntry1=ctk.CTkEntry(master=frame,placeholder_text="Enter the first string: ", width=350)
stringEntry1.pack(pady=15,padx=10)

strinEntry2=ctk.CTkEntry(master=frame,placeholder_text="Enter the second string: ",width=350)
strinEntry2.pack(pady=15,padx=10)

checkButton=ctk.CTkButton(master=frame,text="Check for Anagram",command=validateAnagram)
checkButton.pack(pady=25,padx=13)

anagramButton=ctk.CTkButton(master=frame,text="Result will be displayed here",width=200)
anagramButton.pack(pady=25,padx=15)
root.mainloop()
