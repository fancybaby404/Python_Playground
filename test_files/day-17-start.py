class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        # You can also provide a default value
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "julian")
user_2 = User("002", "macato")

user_1.follow(user_2)
print(f"User1_followers: {user_1.followers}")
print(f"User1_following: {user_1.following}")
print(f"User2_followers: {user_2.followers}")
print(f"User2_following: {user_2.following}")


class Car:
    def __init__(self, seats):
        self.seats = seats

    # --- Method ---
    def enter_race_mode(self):
        self.seats = 2


car_1 = Car(4)
#print(car_1.seats)

car_1.enter_race_mode()
#print(car_1.seats)
