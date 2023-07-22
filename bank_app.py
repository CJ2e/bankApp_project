class Bank:
    options = ['Show Balance', 'Deposit', 'Withdraw',
               'View Transactions']

    def __init__(self):
        with open('transactions.txt', 'r') as f:
            last_line = f.readlines()[-1]
        balance_str = last_line.split('Balance: ')[-1].strip()
        self.balance = round(float(balance_str), 2)

    def showOptions(self):
        print('----------------------')
        for i in range(len(self.options)):
            print(f'To {self.options[i]}, please enter {i}')
        print('----------------------')

    def withdraw(self, amt):
        try:
            amt = float(amt)
        except ValueError:
            amt = 0
        if amt > 0 and amt <= self.balance:
            if amt:
                self.balance -= amt
                self.log_transaction(f"Widthrew {amt}")

    def deposit(self, amt):
        try:
            amt = float(amt)
        except ValueError:
            amt = 0
        if amt > 0:
            if amt:
                self.balance += amt
                self.log_transaction(f"Deposited {amt}")

    def displayBalance(self):
        print(f"Balance: {round(self.balance, 2)}")

    def log_transaction(self, transaction_str):
        with open('transactions.txt', 'a') as f:
            f.write(f"{transaction_str}, Balance: {round(self.balance, 2)}\n")

    def show_log(self):
        with open('transactions.txt', 'r') as f:
            count = 0
            for line in f:
                count += 1
                print(f"{count}: {line.strip()}")
        f.close()


bank = Bank()
while True:
    bank.showOptions()
    try:
        usr_opt = input('Enter your option: ')
    except KeyboardInterrupt:
        print("\nThanks for banking with Python301!\n")
        break
    if usr_opt in ['0', '1', '2', '3']:
        if usr_opt == '0':
            bank.displayBalance()
        elif usr_opt == '1':
            amt = input('Enter depoist amount: ')
            bank.deposit(amt)
        elif usr_opt == '2':
            amt = input('Enter withdraw amount: ')
            bank.withdraw(amt)
        elif usr_opt == '3':
            bank.show_log()
    else:
        print('Invalid input. Try again')
