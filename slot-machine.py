import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

symbols_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbols_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")  # end parameter avoids new line
            else:
                print(column[row], end=" ")
        print()


def deposit():
    while True:
        amount = input("Enter a deposit amount: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid number.")
    return amount


def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 0 < lines < MAX_LINES + 1:
                break
            else:
                print("Amount must be greater than 0 and less than or equal to 3.")
        else:
            print("Please enter a valid number.")
    return lines


def get_bet():
    while True:
        amount = input("How much would you like to bet on each line? ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(
                    f"Amount must be greater than {MIN_BET} and less than or equal to {MAX_BET}.")
        else:
            print("Please enter a valid number.")
    return amount


def game(balance):
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f'You have deposited: ${balance}')
    print(
        f"You are betting on {lines} lines with ${bet} per line and a total bet of ${total_bet}.")

    slots = get_slot_machine_spin(ROWS, COLS, symbols_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbols_value)
    print(f"You won ${winnings}.")
    if winning_lines:
        print(f"You won on lines:", *winning_lines)
    else:
        print("You did not win on any lines.")
    print(f"Your net balance is ${winnings - total_bet + balance}.")

    return winnings - total_bet


def main():
    balance = deposit()
    while True:
      print("Your current balance is $" + str(balance))
      spin = input("Press enter to play (q to quit).")
      if spin.lower() == "q":
          break
      balance += game(balance)

    print(f"You left with ${balance}")


main()
