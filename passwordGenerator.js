const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
  })

  let numberOfCapitalLetters = 0;
  let numberOfSpecialCharacters = 0;
  let numberOfNumbers = 0;
  let passwordLength = 0;
  
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
            passwordLengthQuestion()
        }
        else{
            console.log("That is not a valid input")
        }
        // readline.close()
      })
}

let passwordLengthQuestion = () =>{
    readline.question('How long does your password need to be?', (number) => {
        if (parseInt(number, 10)){
            passwordLength += parseInt(number, 10)
            runGenerator()
        }
        else{
            console.log("That is not a valid input")
        }
        readline.close()
      })
}

  alphabeticalLetters = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h",
    8: "i",
    9: "j",
    10: "k",
    11: "l",
    12: "m",
    13: "n",
    14: "o",
    15: "p",
    16: "q",
    17: "r",
    18: "s",
    19: "t",
    20: "u",
    21: "v",
    22: "w",
    23: "x",
    24: "y",
    25: "z"
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

let runGenerator = () =>{
    let runningPassword = ""
    let numberArray = []
    for(let i = 0; i < numberOfCapitalLetters; i++){
        function getRandomInt(max) {  
            numberArray.push(Math.floor(Math.random() * Math.floor(max)));
        }
        getRandomInt(26)
        
        
    }
    numberArray.map(x => runningPassword += alphabeticalLetters[x].toUpperCase())
    console.log(runningPassword)
    
}
