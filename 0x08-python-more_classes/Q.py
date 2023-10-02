#!/usr/bin/python3
class User:
    id = 1


u = User()
print(User.id)
User.id = 98
print(User.id)

print(u.id)
u.id = 5
print(u.id)
