
import random
import string
from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, first_name, last_name, email, pin):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.pin = pin

class Customer(BankAccount):
    def __init__(self, first_name, last_name, email, pin):
        super().__init__(first_name, last_name, email, pin)
        self.account_number = self.generate_account_number()

    @abstractmethod
    def generate_account_number(self):
        pass

    @abstractmethod
    def view_account_info(self):
        pass

    @abstractmethod
    def transfer_funds(self, recipient_account, amount, pin):
        pass

    @abstractmethod
    def reset_password(self, old_password, new_password):
        pass


class Customer(BankAccount):
    def __init__(self, first_name, last_name, email, pin):
        super().__init__(first_name, last_name, email, pin)
        self.account_number = self.generate_account_number()

    def generate_account_number(self):
        # Generate a unique account number 
        characters = string.digits
        length=10
        
        # Generate a random account number using the defined characters
        account_number = ''.join(random.choice(characters) for _ in range(length))
        
        return account_number

  

    def login(self, email=None, pin=None):
        if email is None and pin is None:
            email = input("Enter email: ")
            pin = input("Enter PIN: ")

        # Authenticate customer 
        if email == self.email and pin == self.pin:
            print("Login successful. Welcome back, {}!".format(self.first_name))
            return True
        else:
            print("Invalid credentials. Login failed.")
            return False

    def reset_password(self, old_password, new_password):
        # Reset customer password 
        if old_password == self.pin:
            self.pin = new_password
            print("Password reset successfully.")
        else:
            print("Invalid old password. Password reset failed.")


    def view_account_info(self):
        # Display account information 
        print("Account Information:")
        print("Name:", self.first_name, self.last_name)
        print("Email:", self.email)
        print("Account Number:", self.account_number)


    def transfer_funds(self, recipient_account, amount, pin):
        # Transfer funds to another account 
        if pin != self.pin:
            print("Invalid PIN. Transfer failed.")
            return

        if amount <= 0:
            print("Invalid amount. Transfer failed.")
            return

        #  fund transfer process 
        print("Transferring {} to recipient account: {}".format(amount, recipient_account))
