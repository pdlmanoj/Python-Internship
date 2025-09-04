class Greet:
    def greet_user(self):
        print("Hello user")
        
class PlayMusic:
    def play_song(self):
        print("Playing song.....")
        

class Child(Greet, PlayMusic):
    pass


c1 = Child()

c1.greet_user()
c1.play_song()