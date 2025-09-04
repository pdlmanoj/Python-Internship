class User:
    
    def __init__(self,name):
        self.name = name
        self._profile_picture = None
        
    
    @property
    def profile_picture(self):
        if self._profile_picture is None:
            print("Profile picture loading .....")
            
            self._profile_picture = f"{self.name}_pic.png"
        
        return self._profile_picture
    
    
user = User("Manoj")
print("User Created.")

## profile picture only load or accessed when it first accessed

print(user.profile_picture)