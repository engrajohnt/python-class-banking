
from customer import Customer
from agent import Agent
from database import db

def create_customer_account():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter email: ")
    pin = input("Set PIN: ")
    
    customer = Customer(first_name, last_name, email, pin)
    db.add_customer(customer)
    db.save_data()

def create_agent_account():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter email: ")
    pin = input("Set PIN: ")
    
    agent = Agent(first_name, last_name, email, pin)
    db.add_agent(agent)
    db.save_data()

def login_as_customer(customer):
    if customer.login():
        account_number = customer.generate_account_number()
        print("Customer Name:", customer.first_name, customer.last_name)
        print("Customer Email:", customer.email)
        print("Account Number:", customer.account_number)
        print("Generated Account Number:", account_number)
        
        print("\n1.View account info \n2.Transfer funds \n3.Reset password \n4.Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            customer.view_account_info()
        elif choice == 2:
            customer.transfer_funds()
        elif choice == 3:
            customer.reset_password()
        elif choice == 4:
            print("Goodbye! Contact EngrJohnTegabankingservice.org for more info.\n")
    else:
        print("Invalid email or PIN.")

def login_as_agent(agent, email=None, pin=None):
    if not email and not pin:
        email = input("Enter email: ")
        pin = input("Enter PIN: ")

    if agent.login(email, pin):
        while True:
            print("\n1.Fund customer account\n2.Reset customer PIN\n3.Reset agent password\n4.Delete customer account\n5.Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                agent.fund_customer_account()
            elif choice == 2:
                agent.reset_customer_pin()
            elif choice == 3:
                agent.reset_password()
            elif choice == 4:
                agent.delete_customer_account()
            elif choice == 5:
                print("Goodbye! Contact EngrJohnTegabankingservice.org for more info.\n")
            else:
                print("Invalid choice.")

    else:
        print("Invalid email or PIN.")

def main():
    while True:
        print("Welcome to Engr JohnTegaBanking service")
        print("1. Create Customer Account")
        print("2. Create Agent Account")
        print("3. Login")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            create_customer_account()
        elif choice == 2:
            create_agent_account()
        elif choice == 3:
            email = input("Enter email: ")
            pin = input("Enter PIN: ")

            customer = db.find_customer_by_email(email)
            agent = db.find_agent_by_email(email)
            if customer:
                login_as_customer(customer)
            elif agent:
                login_as_agent(agent, email, pin)
            else:
                print("Invalid email or account not found.")

        elif choice == 4:
            print("Goodbye! Contact EngrJohnTegabankingservice.org for more info.\n")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



