class KB_Bank():
    def __init__(self):
        
        self.pin = {
                    # name : enrolled pin number

                    }
        self.data = {
                    # {pin : {account : balance}}

                    }
        
    def check_pin(self, name, input_pin):
        ''''
        A bank API wouldn't give the ATM the PIN number,
        but it can tell you if the PIN number is correct or not.
        '''
        true_pin = self.pin[name]
        if true_pin == input_pin:
            return True
        else:
            return False
        
    def enroll_new_customer(self, name, pin, account, init_balance):
        if name in self.pin:
            print(f'name {name} is already enrolled customer.')
        else:
            self.pin[name] = pin
            self.data[pin] = {account : init_balance}
            print(f'Enrollment complete.')
            print(f'name : {name}, account : {account}, initial balance : {init_balance}')
    
    def add_new_account(self, name, pin, new_account, init_balance):
        self.data[pin][new_account] = init_balance
        print(f'Adding new account complete.')
        print(f'name : {name}, account : {new_account}, initial balance : {init_balance}')
        
    
        

class Controller:
    def __init__(self, banks:list):
        self.banks = {bank_name : bank_object for bank_name, bank_object in banks}
        '''
        Insert Card 
        => PIN number 
        => Select Account 
        => See Balance/Deposit/Withdraw
        '''
        
    def see_balance(self, customer_bank, input_pin, selected_acc):
        print(f'Balance : {customer_bank.data[input_pin][selected_acc]}')


            
    def deposit(self, customer_bank, input_pin, selected_acc):
        deposit_q = int(input(f'how much do you want to deposit : '))
        
        customer_bank.data[input_pin][selected_acc] += deposit_q
        
        
    def withdraw(self, customer_bank, input_pin, selected_acc):
        withdraw_q = int(input(f'how much do you want to withdraw : '))
        if withdraw_q <= customer_bank.data[input_pin][selected_acc]:
            customer_bank.data[input_pin][selected_acc] -= withdraw_q
        else:
            print(f'Error : not enough balance')
        
        
    # insert
    def __call__(self, bank_name, name):
        
        input_pin = int(input(f'{name}, enter your pin : '))
        
        customer_bank = self.banks[bank_name]
        
        if customer_bank.check_pin(name, input_pin):
            print(f'Welcome {name}.\n')
            
            # select account
            print(f'Your accounts')
            for acc in customer_bank.data[input_pin].keys():
                print(acc)
            selected_acc = int(input('Select account : '))
            if selected_acc not in customer_bank.data[input_pin]:
                print(f'Error : no valid account')
                return None
            
            # select task
            task = input('What task do you want? see_balance/deposit/withdraw : ')
            
        else:
            print(f'PIN Error. Try again.')
            return None

        
        if task == 'see_balance':
            self.see_balance(customer_bank, input_pin, selected_acc)

        elif task == 'deposit':
            self.deposit(customer_bank, input_pin, selected_acc)
            self.see_balance(customer_bank, input_pin, selected_acc)
            
        elif task == 'withdraw':
            self.withdraw(customer_bank, input_pin, selected_acc)
            self.see_balance(customer_bank, input_pin, selected_acc)
            
        else:
            prinf(f'Error : task error')
            



