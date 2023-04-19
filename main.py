#Des

Secret_word="Rania"
User_Guess=""
User_Guess_Count=0
User_Guess_Limit=3
Out_of_Guess=False

while Secret_word!=User_Guess and not Out_of_Guess:
    if User_Guess_Count<User_Guess_Limit:
        User_Guess = input("Please Enter Secret Word :")
        User_Guess_Count +=1
    else:
        Out_of_Guess=True

if Out_of_Guess:
    print("Sorry You loss")
else:
    print("Congratulations you win")

