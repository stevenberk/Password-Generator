keep_running = True
def run_password_generator():
    password_length = int(raw_input('How long does your password need to be? Enter a number between 8 and 30: '))
    if password_length < 7 or password_length > 31:
        print 'invalid entry'
        run_password_generator()
    else:

        # number_of_lower_case_letters = int(raw_input("How many lowercase letters should there be? Enter a number between 0 and %s: " %(password_length)))
        # if number_of_lower_case_letters > password_length:
        #     print "invalid"

        # number_of_upper_case_letters = int(raw_input("How many uppercase letters should there be? Enter a number between 0 and %s: " %(password_length - number_of_lower_case_letters)))

        # number_of_numbers = int(raw_input("How many numerical characters should there be? Enter a number between 0 and %s: " %(password_length - number_of_lower_case_letters - number_of_upper_case_letters)))

        # number_of_special_charactesr = int(raw_input("How many numerical characters should there be? Enter a number between 0 and %s: " %(password_length - number_of_lower_case_letters - number_of_upper_case_letters)))



        from random import randint

        all_characters = {
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
        62: "0",
        63: "!",
        64: "$",
        65: "%",
        66: "#",
        67: "*",
        68: "?",
        69: "@",
        70: "^"
        }   

        lower_case_letters = {
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

        numerical_digits = {
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "0"
        }

        special_characters = {
        1: "!",
        2: "@",
        3: "#",
        4: "$",
        5: "%",
        6: "^",
        7: "&",
        8: "*",
        9: "?",
        10: "."
        }

        new_password = ""

        for x in range(0, password_length):
            new_password+=all_characters[randint(1, 70)]
    

        print "Your password recommendation is:\n" + new_password
        print "Thank you for using the password generator"
while keep_running:
    keep_running = run_password_generator()
