class user:

    def __init__(self, name, phone_number, address, solde=0, call_history={}):
        self.name = name    
        self.phone_number = phone_number
        self.address = address
        self.solde = solde
        self.call_history = call_history

    def change_number(self, new_number):
        self.phone_number = new_number

    def check_solde(self):
        return self.solde

    def add_amount(self, amount):
        self.solde += amount


user1 = user("amine", "+213773654780", "cite magaria",)
user2 = user("dahmane", "+213663654780", "cite oran",)
user3 = user("abdo", "+213550604900", "cite rabia",)

print(user1.name)
print(user2.phone_number)
user2.change_number("+213552123698")
print(user2.phone_number)
print(user1.address)

print(user1.check_solde())
user1.add_amount(1000)
print(user1.check_solde())
