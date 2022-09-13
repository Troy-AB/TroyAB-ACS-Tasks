valid_option = False
while valid_option == False:
    print("Please enter your choice")
    option = input()

    if option == 1 or option == 2 or option == 3:
        valid_option = True
        print("You have selected option number ", option)
    else:
        print("You have entered an invalid option")
    #endif
#endwhile

