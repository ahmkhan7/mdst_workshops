"""
MDST Workshop 1 - Python Basics Starter Code
"""

# Add any imports you need here:
import random
import base64

def part1(num):
    if (num % 2 == 0):
        print("even")
    else:
        print("odd")
        

def part2():
    x = random.randrange(1, 10)
    print(x)
    while(True):
        user_in = input("Guess the number: ")
        if (user_in > x):
            print ("Too high")
        elif (user_in < x):
            print("Too low")
        elif (user_in == x):
            print("Correct")
            return
        elif user_in == "exit":
            return
        else:
            print("Invalid input")
            return
            


def part3(string):
    for i in range (0, len(string)):
        if (string[i] != string[len(string) - 1 - i]):
            print("Not palindrome")
            return
        
    print("Is palindrome")


def part4a(filename, username, password):
    encrypted_username = base64.b64encode(username)
    encrypted_password = base64.b64encode(password)
    f = open(filename, "w")
    f.write(encrypted_username + "\n")
    f.write(encrypted_password)
    """
    Encrypt your username and password using base64 module
    Store your encrypted username on the first line and your encrypted password
    on the second line.
    """

def part4b(filename, password=None):
    f = open(filename)
    x = base64.b64decode(f.readline())
    print(x)
    x = base64.b64decode(f.readline())
    print(x)
    """
    Create a function to read the file with your login information.
    Print out the decrypted username and password.
    If a password is specified, update the file with the new password.
    """


if __name__ == "__main__":
    part1(3)  # odd!
    part1(4)  # even!
    part2()
    part3("ratrace")  # False
    part3("racecar")  # True
    part4a("secret.txt", "naitian", "p4ssw0rd")
    part4b("secret.txt")
    part4b("secret.txt", password="p4ssw0rd!")
    part4b("secret.txt")
