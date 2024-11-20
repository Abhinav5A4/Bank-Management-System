class Account:
    def __init__(self,a_no,a_name,atm_pin):
        self.a_no=a_no
        self.a_name=a_name
        self.atm_pin=atm_pin
        self.balance=0
class Bank:
    def __init__(self):
        self.accounts=[]
    def createaccount(self,a_no,a_name,atm_pin):
        c=Account(a_no,a_name,atm_pin)
        self.accounts.append(c)
        print('Account number:',a_no,'| Account Name:',a_name,'| ATM PIN:',atm_pin)
    def deleteaccount(self,a_no):
        for acc in self.accounts:
            if acc.a_no == a_no:
                print(a_no,a_name,'Account deleted')

                self.accounts.remove(acc)
                return
        else:
            print('Account does not exist')
    def deposit(self,a_no,amount):
        for acc in self.accounts:
            if acc.a_no == a_no:
                acc.balance+=amount
                print('Account No:',a_no,"| Amount added:",amount)
                return
        else:
            print('Account does not exist')
    def withdraw(self,a_no,atm_pin,amount):
        for acc in self.accounts:
            if acc.a_no==a_no:
                if acc.atm_pin==atm_pin and amount<=acc.balance:
                    acc.balance-=amount
                    print('Account No:',a_no,'| Amount debited:',amount)
                    return
        else:
            print('Insufficient balance')        
ac=Bank()
while True:
    print('\nselect one option:')
    print("1.Create an Account\n 2.Delete an Account\n 3.Deposit Money\n 4.Withdraw Money\n 5.Display the list\n 6.Exit()")
    option=int(input())
    if option==1:
        a_no=int(input('Enter Account Number:'))
        a_name=input('Enter account holder name:')
        atm_pin=int(input('Enter ATM pin:'))
        ac.createaccount(a_no,a_name,atm_pin)
    elif option==2:
        a_no=int(input('Enter Account Number:'))
        ac.deleteaccount(a_no)
    elif option==3:
        a_no=int(input('Enter Account Number:'))
        amount=int(input('Enter the amount:'))
        ac.deposit(a_no,amount)
    elif option==4:
        a_no=int(input('Enter Account Number:'))
        atm_pin=int(input('Enter ATM pin:'))
        amount=int(input('Enter the amount:'))
        ac.withdraw(a_no,atm_pin,amount)
    elif option==5:
        print("List of account Holders")
        for acc in ac.accounts:
            print(acc.a_name,end=' ')
    elif option==6:
        exit()