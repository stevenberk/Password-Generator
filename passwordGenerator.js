const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
  })

  let numberOfCapitalLetters = 0;
  let numberOfSpecialCharacters = 0;
  let numberOfNumbers = 0;
  
  readline.question('How many capital letters does your password need?', (number) => {
    if (parseInt(number, 10)){
        numberOfCapitalLetters += parseInt(number, 10)
        specialCharacterQuestion()
    }
    else{
        console.log("That is not a valid input")
    }
    // readline.close()
  })

let specialCharacterQuestion = () =>{
  readline.question('How many special characters does your password need?', (number) => {
    if (parseInt(number, 10)){
        numberOfSpecialCharacters += parseInt(number, 10)
        numberOfNumbersQuestion()
    }
    else{
        console.log("That is not a valid input")
    }
    // readline.close()
  })
}

let numberOfNumbersQuestion = () =>{
    readline.question('How many numberical characters does your password need?', (number) => {
        if (parseInt(number, 10)){
            numberOfNumbers += parseInt(number, 10)
        }
        else{
            console.log("That is not a valid input")
        }
        readline.close()
      })
}


  alphabeticalLetters = {
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

    numericalDigits = {
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

    specialCharacters = {
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