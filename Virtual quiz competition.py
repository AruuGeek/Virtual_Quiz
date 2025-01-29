print ("Welocme to My quiz game ! ")
playing = input("Are you ready to play: ")
if playing.lower() != "yes":
    quit()
print("lets play :)")

answer = input("which year was the first olympics : ")
if answer != "1896":
    print(" sorry you are wrong")
else:
    print (" congratulations you're correct")

answer = input("Who won the football world cup in 2022 ? : ")
if answer.lower() != "argentina":
    print(" sorry you are wrong")
else:
    print (" congratulations you're correct")

answer = input("Who was the captain of 1983 World cup winning Indian squad ?")
if answer.lower() != "kapil dev":
    print(" sorry you are wrong")
else:
    print (" congratulations you're correct")

answer = input("Which did India host their first Commonwealth Games ? ")
if answer != "2010":
    print(" sorry you are wrong")
else:
    print (" congratulations you're correct")

answer = input("Basketball icon Micheal Jordan played for which team in the NBA ?")
if answer.lower() != "chicago bulls":
    print(" sorry you are wrong")
else:
    print (" congratulations you're correct")

print ("thats a wrap !!!")
print(" Thanks for playing !")