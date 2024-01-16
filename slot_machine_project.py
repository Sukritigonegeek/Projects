import random #to generate values randomly for the slot machine
# how many items in each reel(vertical) and how many lines(horizontal).


MAX_LINES= 3 #global constatnt to tell max how many lines we will be usingin the game.In case the number of lines is increased, we can just change this line and the code wont have to changed.
MIN_lINES= 1
MAX_BET= 100
MIN_BET=1

ROWS = 3 #reels
COLS = 3

symbol_count= {
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

def slot_machine_spin(rows, cols, symbols):   #these 3 parameters we will be passing in this function
    # generating what symbols are going to be in each column based on the frequency of symbol we have in symbolcount
    # essentially randomly picking no of rows inside each column
    # randomly pick one symbol from the list of all possible symbols and then choose again deducting the previously chosen value from the list 
    # not an efficient algorithm, but since the data is small it's fine
    all_symbols= [] #list
    for symbol, symbol_count in symbols.items(): # for loop to add however many symbols we have in the all symbols list
        for _ in range(symbol_count):
            all_symbols.append(symbol)
# meaning suppose symbol A has symbol count 2, it will append A twice in the list
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols) #current_symbols is a copy of all symbols (made using the : symbol), after removing the chosen value, the remaining list will be sored and will continue like this 
            current_symbols.remove (value) # removing the value from the current symbol list
            column.append(value) # adding that same value to the coumn

        columns.append(column)

    return columns   

# we are using a 3x3 slot machine and you get a line when you get 3 in a row, to win.
def deposit():
    while True: #creating a while loop to get the deposit amount
        amount= input("Enter Deposit Amount $ ")
        if amount.isdigit():  #using the digit clause before the >0 clause so that there's no word value entered
            amount= int(amount)
            if amount > 0:
                break #breaking the loop once the entered value is not a word and is greater than 0
            else:
                print("Amount has to be greater than 0")
        else:
            print ("Please enter a valid number")
    
    return amount
#how much they want to bet (bet amount) and how many lines they would bet so that we can multiply both

def number_of_lines():
    while True: #creating a while loop to get the number of lines
        lines= input("Enter the number of lines to be bet on (1-" + str(MAX_LINES)+ ")? ") #to show it as 1 to maxline value
        if lines.isdigit():  #using the digit clause before the >0 clause so that there's no word value entered
            lines= int(lines)
            if 0 < lines <= MAX_LINES:
                break #breaking the loop once the entered value is not a word and is wihin 0 and maxline value
            else:
                print("Enter valid values")
        else:
            print ("Please enter a valid number")
    
    return lines       


def get_bet():
    while True: #creating a while loop to get the deposit amount
        bet_amount= input("Enter Bet Amount on each line $ ")
        if bet_amount.isdigit():  #using the digit clause before the >0 clause so that there's no word value entered
            bet_amount= int(bet_amount)
            if MIN_BET < bet_amount <= MAX_BET:
                break #breaking the loop once the entered value is not a word and is greater than 0
            else:
                print(f"Bet Amount has to be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print ("Please enter a valid number")
    
    return bet_amount


def main(): #Using the main code under a function so that if the player wants to play again we can just recall this function
    balance= deposit()
    lines= number_of_lines()
    while True:
        bet_amount= get_bet()
        total_bet= bet_amount * lines
        if total_bet > balance:
            print(f"Your total bet amount ${total_bet} is greater than your account Balance. Your account balance is ${balance}.")
        else:
            break
                 
    print(f"You are betting ${bet_amount} on {lines} lines. Your total bet will be ${total_bet}.")

    # print(balance, lines, bet_amount)

main()


