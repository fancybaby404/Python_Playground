class LastTweet:
    pass

a = LastTweet() # Calling the class
a.message = "140 characters"

print(a.message)
#print(Tweet.message)

# This doesnt work because it is not defined inside the class but instead it is defined in the
# object of the Tweet() which is called 'a'

b = LastTweet()
b.message = 'Something different'
print(b.message)

# dunder methods (methods with double underscore)

class Tweet:
    def __init__(self): # Constructor
        print('Hi')

# a = Tweet() # <- This wont work if the def init does not have a self

class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight
    def introduce_self(self):
        print(f"My name is {self.name}, I am color {self.color}, and my weight is {self.weight}")
    
r1 = Robot("John", "red", 50)
r1.introduce_self() #prints out

class Dog:
    def __init__(self, name, breed, weight):
        self.name = name
        self.breed = breed
        self.weight = weight
    def introduce_self(self):
        print(f"I am a dog, my name is {self.name} and i am a {self.breed}")
    def weight_minus(self):
        self.weight - 50
        print(self.weight)

dog1 = Dog("Oreo", "Shih tzu", 50)
dog1.introduce_self()
dog1.weight_minus()

dog2 = Dog("Brando", "iForgot", 100)
dog2.introduce_self()
dog1.weight_minus()

