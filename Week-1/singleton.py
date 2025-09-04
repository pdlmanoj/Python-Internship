class Singleton:
    _instance = None
    
    
    def __new__(cls, *args, **kwargs):
        
        if cls._instance is None:
            print("Creating a new instance...")
            cls._instance = super().__new__(cls)
        
        return cls._instance
    
    


a = Singleton()
b = Singleton()

print(a)
print(b)

print(a is b)
