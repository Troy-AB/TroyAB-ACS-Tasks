option_valid = False
while option_valid == False:
    option = int(input("enter your choice"))

    if option >= 1 or option <= 3:
        print("You have entered a correct option")
        option_valid = True
    else:
        print("you have entered an invalid option")
    #endif
#endwhile
