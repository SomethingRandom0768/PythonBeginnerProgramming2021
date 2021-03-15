import random
from random import choice

ticket_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,'a', 'b', 'c', 'd', 'e']

winning_ticket = []

for i in range(4):
    chosen_one = str(choice(ticket_list))
    winning_ticket.append(chosen_one)

print(f"Any lottery ticket with {winning_ticket} is the winner!")

# 9-15 Lottery Analysis starts here

my_ticket = []
number_ran = 0

while my_ticket != winning_ticket:
    number_ran += 1
    if len(my_ticket) > 4:
        my_ticket = []
    else:
        chosen_two = str(choice(ticket_list))
        my_ticket.append(chosen_two)

print(f"It took until {number_ran} tries to finally get the winning lottery ticket.")