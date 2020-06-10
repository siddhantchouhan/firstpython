while True:
    #This program's goal is to tell if the users input is a palindrome.
    #Getting the input from user.
    inpuTStr = input("Enter your word here: ")
    #This command ignores spaces from the users input.
    temp = inpuTStr.replace(" ", "")
    temp1 = temp.replace(",", "")
    temp2 = temp1.replace(".", "")
    temp3 = temp2.replace("!", "")
    temp4 = temp3.replace("?", "")
    temp5 = temp4.replace("'", "")
    NewInputString = temp5.replace('"', "")
    

    #Getting the length of user input.
    lenstr = len(NewInputString)
    #print(lenstr)

    #Converting input into uppercase before comparision.
    upperString = NewInputString.upper()

    #For loop to compare first to last character of string with corresponding character from end of the string.
    #Palindrome string are the string which can be read the same backwards.
    for i in range(lenstr):
        if upperString[lenstr-i-1] == upperString[i]:
            compchar = i
            #print(compchar)
        else:
            compchar=0
            break
        

   # print('comparision up to this character ', compchar)

    if compchar == lenstr-1:
        print("This is palindrome ")
    else:
        print("Not an palindrome ")
