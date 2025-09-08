class EmailAuth:

    def __init__(self):
        pass

    def login(self, name, email):
        print(f"{name} with {email} loged using Email Authentication")

class PhoneAuth:
    def login(self,name,email):
        print(f"{name} with {email} loged using Phone Authentication")

class Subscription:
    def activate_subscription(self, name):
        print(f"Subscription activated for {name}")


class User:
    def __init__(self, name, email, auth_type, subscription):

        self.name = name
        self.email = email
        self.auth_type = auth_type
        self.subscription = subscription

    def login(self):
        self.auth_type.login(self.name, self.email)
    
    def subscribe(self):
        self.subscription.activate_subscription(self.name)


user1 = User('Ram', 'ram@gmail.com', PhoneAuth(), Subscription())
user2 = User('Gita', 'gita@gmail.com', EmailAuth(), Subscription())

user1.login()
user1.subscribe()

user2.login()
user2.subscribe()
    