# from abc import ABC, abstractmethod

# class BankAccount(ABC):
#     def __init__(self, first_name, last_name, email, pin):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.pin = pin

# class Customer(BankAccount):
#     def __init__(self, first_name, last_name, email, pin):
#         super().__init__(first_name, last_name, email, pin)
#         self.account_number = self.generate_account_number()

#     @abstractmethod
#     def generate_account_number(self):
#         pass

#     @abstractmethod
#     def view_account_info(self):
#         pass

#     @abstractmethod
#     def transfer_funds(self, recipient_account, amount, pin):
#         pass

#     @abstractmethod
#     def reset_password(self, old_password, new_password):
#         pass

# # Agent class, no abstract methods specific to agents

# class Agent(BankAccount):
#     def __init__(self, first_name, last_name, email, pin):
#         super().__init__(first_name, last_name, email, pin)

#     def login(self, email, pin):
#         # Agent login implementation...

#     def reset_password(self, old_password, new_password):
#         # Agent reset password implementation...

#     def fund_customer_account(self, customer_account, amount):
#         # Agent fund customer account implementation...

#     def reset_customer_pin(self, customer_account, new_pin):
#         # Agent reset customer PIN implementation...

#     def delete_customer_account(self, customer_account):
#         # Agent delete customer account implementation...

# # Rest of your code...
