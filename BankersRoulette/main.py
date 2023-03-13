names_string= input("Give Me Everybody's name , separated by a comma.\n")
names= names_string.split(",")


import random

X= len(names)

random_name=random.randint(0,X-1)

who_will_pay= names[random_name]


# the code below can also be used 
# who_will_pay= random.choice(names)


print(f"{who_will_pay} will pay the bill ")

