### Composition EXAMPLE

class EmailAuth:
    def login(self,name):
        print(f"Login {name} using EmailAuth")

class GithubAuth:

    def login(self,name):
        print(f"Login {name} using GithHubAuth")



class User:

    def __init__(self, name, auth_type):
        self.name = name
        self.auth_type =auth_type
    
    def login(self):
        self.auth_type.login(self.name)


user1 = User('Ram', GithubAuth())
user2 = User('Hari', GithubAuth())
user3 = User('Hari', EmailAuth())

user1.login()
user2.login()
user3.login()
