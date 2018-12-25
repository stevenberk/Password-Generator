from random import randint
from random import shuffle 
keep_running = True
def run_password_generator():

    number_of_special_characters = int(raw_input("Welcome to the password generator. You will need answer a few questions about your password requirements. First, How many special characters does your password need? Enter a number: "))
        
    number_of_numbers = int(raw_input("How many numerical characters does your password need? Enter a number: "))

    number_of_upper_case_letters = int(raw_input("How many uppercase letters does your password need? Enter a number: "))

    number_of_total_characters = int(raw_input("So far your password has %s characters. How many total charactes does your password need? Enter a number greater than %s: " %(number_of_special_characters + number_of_upper_case_letters + number_of_numbers, number_of_special_characters + number_of_upper_case_letters + number_of_numbers)))
    if number_of_total_characters < number_of_special_characters + number_of_upper_case_letters + number_of_numbers:
        print "Invalid entry, please start over"
        run_password_generator()
    else:

        alphabetical_letters = {
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

        pre_shuffle_password = ""

        for x in range(0, number_of_special_characters):
            pre_shuffle_password += special_characters[randint(1, 10)]
        
        for x in range(0, number_of_numbers):
            pre_shuffle_password += numerical_digits[randint(1, 10)]
    
        for x in range(0, number_of_upper_case_letters):
            pre_shuffle_password += alphabetical_letters[randint(1, 26)].upper()
        
        for x in range(0, (number_of_total_characters - number_of_numbers - number_of_special_characters - number_of_upper_case_letters)):
            pre_shuffle_password += alphabetical_letters[randint(1, 26)]

        password_character_list = []

        for x in pre_shuffle_password:
            password_character_list += x
     
        shuffle(password_character_list)  
       
        new_password = ""
        for x in password_character_list:
            new_password += x

        print "Your password recommendation is:\n" + new_password
        print "Thank you for using the password generator"
while keep_running:
    keep_running = run_password_generator()
