class Customer:
    def __init__(self,name, address):
        self.name = name
        self.address = address
        
    def __str__(self):
        return f"{self.name} -> {self.address}"
    
    def __repr__(self):
        return f"Customer(name='{self.name}', address='{self.address}')"
    
    def edit_customer_info(self, name, city, postal_code, state):
        self.name = name
        self.address.edit_address(city,postal_code,state)
        return "Customer Information edit successfully"
    

class Address:
    def __init__(self, city, postal_code,state):
        self.state = state
        self.city = city
        self.postal_code = postal_code

    def __str__(self):
        return f"Address: {self.city}, {self.postal_code} {self.state}"
    
    def edit_address(self, city,postal_code, state):
        self.city = city
        self.state = state
        self.postal_code = postal_code


add1 = Address('kathmandu', '44333', 'Bagmati')
        
c1 = Customer('Hari', add1)
print(c1)

print(c1.edit_customer_info('Ram', 'kushma', '55555', 'Gandaki'))
print(c1)

