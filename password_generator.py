def run_password_generator():
    password_length = int(raw_input('How long does your password need to be? Enter a number between 8 and 30: '))
    if password_length > 7 and password_length < 31:
        print str(password_length) + " is good"
    else: 
        print 'invalid entry'

    # are_numbers_allowed = True

    # password_can_have_numbers = int(raw_input('Can your password have numbers? Press 1 for Yes, press 2 for No: '))
    # if password_can_have_numbers == 1:
    #     print "numbers okay"
    #     are_numbers_allowed = True
    # if password_can_have_numbers == 2:
    #     print "no numbers"
    #     are_numbers_allowed = False
   
    from random import randint

    letters = {
        1: "a",
        2: "b",
        3: "c",
        4: "d",
        5: "e",
        6: "f",
        7: "g",
        8: "h",
        9: "i",
        10: "j",
        11: "k",
        12: "l",
        13: "m",
        14: "n",
        15: "o",
        16: "p",
        17: "q",
        18: "r",
        19: "s",
        20: "t",
        21: "u",
        22: "v",
        23: "w",
        24: "x",
        25: "y",
        26: "z"
    }   

    new_password = ""

    for x in range(0, password_length):
        new_password+=letters[randint(1, 26)]

    print new_password
run_password_generator()