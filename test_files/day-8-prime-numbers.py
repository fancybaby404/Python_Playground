#Write your code below this line 👇
                            
def prime_checker(number):
    flag = None

    if number > 1:
        for i in range (2,number):
            #if there is a number other than itself that is divisible then it is not a prime
            if (number % i) == 0:
                flag = True
                break
        
    if not flag:
        print("It's a prime number")
    else:
        print("It's not a prime number")
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

