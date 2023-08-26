
from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, first_name, last_name, email, pin):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.pin = pin

class Agent(BankAccount):
    def __init__(self, first_name, last_name, email, pin):
        super().__init__(first_name, last_name, email, pin)

    def login(self, email, pin):
        # Authenticate agent
        if email == self.email and pin == self.pin:
            print("Agent login successful. Welcome back, {}!".format(self.first_name))
        else:
            print("Invalid credentials. Agent login failed.")


    def reset_password(self, old_password, new_password):
        # Reset agent password 
        if old_password == self.pin:
            self.pin = new_password
            print("Agent password reset successful.")
        else:
            print("Invalid old password. Agent password reset failed.")

    def fund_customer_account(self, customer_account, amount):
        # Fund a customer's account 
           # Assuming you have access to customer accounts here
        # and can increase their balance by the given amount
        print("Funding customer account: {} with amount: {}".format(customer_account, amount))

    def reset_customer_pin(self, customer_account, new_pin):
        # Reset a customer's PIN 
        # Assuming you have access to customer accounts here
        # and can update the customer's PIN
        print("Resetting customer PIN for account: {} to new PIN: {}".format(customer_account, new_pin))

    def delete_customer_account(self, customer_account):
        # Delete a customer's account 
         # Assuming you have access to customer accounts here
        # and can delete the customer's account
        print("Deleting customer account: {}".format(customer_account))
