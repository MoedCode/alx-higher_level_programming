#!/usr/bin/python3
class USER:
    pass


user1 = USER()
user2 = USER()
user1.Fname = "mohamed"
user1.Lname = "mahmoud"
user1.email = "mohamed_mahmoud@comany.com"
# print(f"{user1}, {user2}")


class Employees:

    def __init__(self, firsto, lasto, pay):
        self.firsto = firsto
        self.lasto = lasto
        self.pay = pay
        self.email = firsto + '.' + lasto + '@company'
        self.__Password = firsto + '123'

    def fullname(self):
        return f'{self.firsto} {self.lasto}'

    def THIS(self):
        return f'employ{self} \n First Name: {self.firsto} \
            Second Name: {self.lasto} email: {self.email} '


# Create instances of the Employees class
employee0 = Employees("MohamedSan", "proCedo", 50000)
employee1 = Employees("John", "Doe", 60000)

# Access and print employee0's email

print(employee0.__Password)
print(Employees)
