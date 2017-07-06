Question = input("Do you want to eat 'food' or 'dessert'?")


if Question==("dessert"):
    Dessert=input("churros or ice cream?")
    if Dessert=="churros":
        Filling=input("What kind of filling? (caramel,chocolate,vanilla)")
        if Filling=="caramel":
            choice3=input("Are you thirsty?")
            if choice3=="yes":
                choice4=input("lemonade or water?")
                if choice4=="lemonade":
                    print("lemonade")
                elif choice4=="water":
                    print("Enjoy your water!")

        elif Filling=="chocolate":
            print("You forgot you had diabetes and you go into shock. GAME OVER.")

        elif Filling=="vanilla":
            print("LOLOLOL. You burnt your tongue. GAME OVER.")
    elif Dessert=="ice cream":
            print("Dude you ate too fast and you got a brain freeze. Congratulations you played yourself. GAME OVER.  ")


if Question== ("food"):
    choice = input("'pizza' or 'taco'?")
    if choice == "pizza":
        choice2 =input("There is a long line. 'wait' or 'leave'?")
        if choice2 == ("wait"):
            choice3 = input("You got your pizza but it is really hot. Do you want to 'eat', or 'wait'?")
            if choice3 ==("wait"):
                choice4 = input("After you're done, you want more. Buy another slice? yes or no ")
                if choice4 ==("yes"):
                    print("You just spent your gas money. Now you're stranded in the middle of nowhere. They never found your body SMH. GAME OVER.")
                elif choice4 ==("no"):
                    choice5 = input(" On your way home you find a puppy. 'take home' or 'leave' it?")
                    if choice5 ==("take home"):
                        print("Congrats. You have a new best friend, go home.")
                    elif choice5 ==("leave"):
                            print("WoW... You are a terrible, animal haiting person. Be proud.")
            elif choice3 ==("eat"):
                print("It's so hot that you get 2nd degree burns and spend the rest of your night in the hospital. GAME OVER.")
        elif choice2 ==("leave"):
            print("Everything is closed now. Go home hungry.")
    elif choice== "taco":
        choice6 = input("You were going to order steak but their out. Order 'something else' or 'leave'?")
        if choice6 ==("something else"):
            choice7=input("They put hot sauce on your taco and you found out they dropped it on the ground, write them a strongly worded 'email' or set one of their cars on 'fire'?")
            if choice7 ==("email"):
                    choice8= input("They didnt respond, but a lawyer said you have grounds to sue. Do you want to? yes/no")
                    if choice8 == ("yes"):
                        print("Congrats. You got sick becasue of that taco and won your case, now you're loaded. Go enjoy your money. GAME OVER.")
                    elif choice8 ==("no"):
                        print("Wow you should have sued.")
            elif choice7 ==("fire"):
                    print("Hey you may be spending some time in jail, so GAME OVER for you, go find a lawyer.")

        elif choice6==("leave"):
            print("If your going to be inflexible then you should just go home, hungry.")
