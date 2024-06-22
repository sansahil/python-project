import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count ={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

def get_solt_machine_spin(rows,cols,symbols):
    all_symbols =[]
    for symbol,symbol_count in symbol_items():
        for _  in range (symbol_count):
          all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column =[]
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            columns.append(value)

        columns.append(column) 
    return columns

def print_solt_machine(columns):
    for row in range(len(columns[0])):
        for i ,column in enumerate (columns):
            if i  != len(column) -1 :
              print(column[row], "|", end="\n")
            else:
                print(colums[row],end="")


        print()

        




def deposit():
    while True:
        amount = input("what would you like to deposit ? $")
        if amount.isdeposit():
            amount = int(amount)
            if amount > 0 :
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount

def get_number_of_lines():
    while True:
        lines =input("Enter the number of lines to bet on (1-" + str(MAX_LINES)+")?")
        if lines.isdeposit():
            lines = int(lines)
            if 1 <=lines <= MAX_LINES :
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines        



def main():
  balance = deposit()
  lines =get_number_of_lines()
  while True:
      bet = get_bet()
      total_bet = bet * lines

      if total_bet > balance:
           print("you do not have enough to bet that amount,you")
      else:
          break  
          
  print("you are betting ${bet} on {lines} lines. total bet is equal to: ${total}")

  slots = get_solt_machine_spin(ROWS,COLS,symbols_count)
  print_solt_machine(slots)



  main()               