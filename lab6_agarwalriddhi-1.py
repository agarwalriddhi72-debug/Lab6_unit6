"""
The program's name: User login system
Your name: Riddhi Agarwal
The purpose of the program: A login system that checks username and password using a dictionary, assigns security level, and gives 3 login attempts.
Starter code: None
Date: February 20, 2026
"""

#Create a dictionary of 4 key-value pairs
users: dict[str, str]= {
    "guest": "guest",
    "admin": "admin123",
    "user1": "password123",
    "student1": "student123"
}

#Ask user to provide their username
username: str = input("Please enter your username: ")

#Give user 3 attempts
attempts: int = 3

#Check if username exists in dictionary
if username in users:

    while attempts > 0:
        password: str = input("Please enter your password: ")

        #Check if password matches
        if password == users[username]:

            #Assign security level
            if username == "guest":
                security_level: str = "Guest access"
            else:
                security_level: str = "Security Level 1"

            print(f"Welcome, {username}. You have {security_level}.")
            break
