def prime_number(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        
    return True
User_input = int(input("Enter your number you want to you its a prime number or not??."))

def new_func(User_input):
    print(f"Oh No!. {User_input} This is not a prime number.")

if prime_number(User_input):
    print(f"yeah! {User_input} This is a prime number.")
else:
    new_func(User_input)
