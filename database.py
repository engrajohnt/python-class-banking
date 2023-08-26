import json
from customer import Customer
from agent import Agent

class Database:
    def __init__(self):
        self.customers = []
        self.agents = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def find_customer_by_email(self, email):
        for customer in self.customers:
            if customer.email == email:
                return customer    
        return None
    
    def add_agent(self, agent):
        self.agents.append(agent)

    def find_agent_by_email(self, email):
        for agent in self.agents:
            if agent.email == email:
                return agent    
        return None
    

    def save_data(self):
        data = {
            "customers": [customer.__dict__ for customer in self.customers],
            "agents": [agent.__dict__ for agent in self.agents]
        }
        with open('data.json', 'w') as file:
            json.dump(data, file)

    def load_data(self):
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                for customer_data in data["customers"]:
                    customer = Customer(
                        first_name=customer_data["first_name"],
                        last_name=customer_data["last_name"],
                        email=customer_data["email"],
                        pin=customer_data["pin"]
                    )
                    self.customers.append(customer)
                # Similarly, you can add code to load agents if you have them in your JSON data
                for agent_data in data["agents"]:
                    agent = Agent(
                        first_name=agent_data["first_name"],
                        last_name=agent_data["last_name"],
                        email=agent_data["email"],
                        pin=agent_data["pin"]
                    )
                    self.agents.append(agent)
        except FileNotFoundError:
            pass  # Handle the case where the data file does not exist


db = Database()
db.load_data()
