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
        26: "z",
        27: "A",
        28: "B",
        29: "C",
        30: "D",
        31: "E",
        32: "F",
        33: "G",
        34: "H",
        35: "I",
        36: "J",
        37: "K",
        38: "L",
        39: "M",
        40: "N",
        41: "O",
        42: "P",
        43: "Q",
        44: "R",
        45: "S",
        46: "T",
        47: "U",
        48: "V",
        49: "W",
        50: "X",
        51: "Y",
        52: "Z",
        53: "1",
        54: "2",
        55: "3",
        56: "4",
        57: "5",
        58: "6",
        59: "7",
        60: "8",
        61: "9",
        62: "0"
    }   

    new_password = ""

    for x in range(0, password_length):
        new_password+=letters[randint(1, 62)]
    

    print new_password
run_password_generator()