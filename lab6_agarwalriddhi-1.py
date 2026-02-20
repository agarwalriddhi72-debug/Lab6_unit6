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
