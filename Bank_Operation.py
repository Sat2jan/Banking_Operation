#Bank Operation using OOPs

class Bank:  #parent class
    bankname = "State bank of India"
    branch = "Jamui, Bihar"
    
    #Create Account (works as a constructor)
    def __init__(self, username,pan, address): #we have to create a constructor here:
        self.username = username  #this are the three instance variables.
        self.pan = pan
        self.address = address
        self.balance= 0.0 #set the account balance to 0.0 
        print(f"Hello {self.username} Congratulations your account has been created Sucesfully!")

    #Deposit : For deposit we will create a instance method
    def deposit(self,amount):   #this are the child classes 
        self.balance=self.balance+amount
        print(f"{amount} deposited successfully")
        
    #Withdrawl
    
    def withdrawl(self,amount):
        if amount<self.balance:
            self.balance=self.balance-amount
            print(f"{amount} withdrawl successfully")
        else:
            print("Insufficient Balance...")
            
    #Ministatement
    def ministatement(self):
        print(f"Your account balance is {self.balance} ")
        
    
print(f"Welcome to {Bank.bankname} , {Bank.branch}")      #Here we have used the bank name as a title....
#here we are collecting user data for account creation
username = input("Enter your Name: ")
pan = input("Enter your PAN card number: ")
address = input("Enter your address: ")

b = Bank(username,pan,address) #here we are creating the object

while True:  #here we have created Infinite Loop
    print("\nPlease select any Option: ")
    print("1. Deposit\n2.Withdrawl\n3.Ministatement\n4.Stop")
    option = input("Enter your choices: ")
    
    if option.isdigit():
        option = int(option)
    
        if option==1: #here we have called the deposit function so that the user which has deposited the amount would show there...
            #here we give option 1 so that it calls the 1 condition of the funciton.
            amount = float(input("Enter Deposited Amount: "))
            b.deposit(amount)
            
        elif option==2:
            amount = float(input("Enter a withdrawl amount: "))
            b.withdrawl(amount)
            
        elif option==3:
            b.ministatement()
            
            
        elif option==4:
            print("Thanks for using State Bank of India....")
            break
        else:
            print("Invalid Option.. Please select a valid Option")
            
            
            
        