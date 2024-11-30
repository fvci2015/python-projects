result=""
def CheckAnagram(str1,str2):
    global result
    if sorted(str1)==sorted(str2):
        result="Anagram"
    else:
        result="Not anagram"
def validateAnagram():
    global result
    str1=input("Enter the first string: ")
    str2=input("Enter the second string: ")
    CheckAnagram(str1,str2)
    print("The strings are:",result)

if __name__=="__main__":
    validateAnagram()
    
