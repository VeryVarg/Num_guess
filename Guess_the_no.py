import random
print(""" 
#######                         #####                                                       
    #    #   # #####  ######    #     #  ####  #    # ###### ##### #    # # #    #  ####     
    #     # #  #    # #         #       #    # ##  ## #        #   #    # # ##   # #    #    
    #      #   #    # #####      #####  #    # # ## # #####    #   ###### # # #  # #         
    #      #   #####  #               # #    # #    # #        #   #    # # #  # # #  ###    
    #      #   #      #         #     # #    # #    # #        #   #    # # #   ## #    #    
    #      #   #      ######     #####   ####  #    # ######   #   #    # # #    #  ####     
                                                                                             """)
c = random.randrange(1, 101)



def guess_no(rep):
    for a in range(rep, 0, -1):
        print(f"You have {a} chances left to guess")
        # print(c)
        u = int(input("make a guess"))
        if u == c:
            return print("You guessed it correct")
        if u > c:
            print("Your no. is too big")
        else:
            print("Your no. is too small")

def final_prog():
    repeat = input("choose the difficulty level")
    if repeat == 'hard':
        guess_no(5)
    elif repeat == 'easy':
        guess_no(10)
    else:
        print("please give valid input")
        final_prog()

final_prog()
