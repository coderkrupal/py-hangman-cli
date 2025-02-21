# Hangman game using python
import random
words = [
    "PYTHON",
    "VARIABLE",
    "FUNCTION",
    "ALGORITHM",
    "LOOP",
    "DEBUG",
    "STRING",
    "ARRAY",
    "OBJECT",
    "GITHUB",
    "INTERNET",
    "NETWORK",
    "COMPUTER",
    "HARDWARE",
    "SOFTWARE",
    "KEYBOARD",
    "MONITOR",
    "ELECTRIC",
    "DIGITAL",
    "ROBOT",
    "PLANET",
    "THUNDER",
    "WILDLIFE",
    "MOUNTAIN",
    "HURRICANE",
    "JOURNEY",
    "PUZZLE",
    "HISTORY",
    "SHADOW",
    "FREEDOM",
]

# dictionary key for each incorrect chance

hangman_stages = {
    6:( """
      -----
      |   |
          |
          |
          |
          |
    =========
    """),
    5:("""
      -----
      |   |
      O   |
          |
          |
          |
    =========
    """),
    4:("""
      -----
      |   |
      O   |
      |   |
          |
          |
    =========
    """),
    3:("""
      -----
      |   |
      O   |
     /|   |
          |
          |
    =========
    """),
    2:("""
      -----
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """),
    1:("""
      -----
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """),
    0:("""
      -----
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    GAME OVER!
    """)
}

def hangman_wronguass():
    pass

def hangman_man(wrongguass):
    print("============================")
    print(hangman_stages[wrongguass])
    print("============================")
        
def hangman_hint(hint):
     print(' '.join(hint))  

def display_asnwer(answer):
    print(' '.join(answer))

def hangman_main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guass = 6
    while wrong_guass  > 0:
        hangman_man(wrong_guass)
        hangman_hint(hint)
        letter = input("\nEnter a character: ").upper() 
        if letter in answer:
            for i in range(len(answer)):
                if answer[i] == letter:
                    hint[i] = letter
        else:
            wrong_guass -= 1 
            
        if '_' not in hint:
            print("congratualtion ! you guessed correct word:",answer)
            break
        if wrong_guass == 0:
            print("-------------you lost game----------")
        

if __name__ == "__main__":
    hangman_main()
