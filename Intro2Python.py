"""lottery_numbers = {13, 21, 22, 5, 8}
"""
"""
A player looks like this:

{
    'name': 'PLAYER_NAME',
    'numbers': {1, 2, 3, 4, 5}
}

Define a list with two players (you can come up with their names and numbers).
"""
"""
For each of the two players, print out a string like this: "Player PLAYER_NAME got 3 numbers right.".
Of course, replace PLAYER_NAME by their name, and the 3 by the amount of numbers they matched with lottery_numbers.
You'll have to access each player's name and numbers, and calculate the intersection of their numbers with lottery_numbers.
Then construct a string and print it out.

Remember: the string must contain the player's name and the amount of numbers they got right!
"""
"""players = [
    {'name':'Ishanth','numbers':{1,10,5}},
    {'name':'Hemanth','numbers':{13,21,5}},
]

name = players[0]['name']
match_num_player1 = lottery_numbers.intersection(players[0]['numbers'])
match_num_player2 = lottery_numbers.intersection(players[1]['numbers'])
print("Player "+players[1]['name']+" got "+ str(len(match_num_player2))+" right")
print(f"Player {name} got {len(match_num_player1)} right"  )"""




"""nearby_people = {'Rolf', 'Jen', 'Anna'}
user_friends = set()  # This is an empty set, like {}

# Ask the user for the name of a friend
ask_user = input("Enter your name: ")
# Add the name to the empty set
user_friends.add(ask_user)
print(user_friends)
# Print out the intersection between both sets. This gives us a set with those friends that are nearby.
near_by_friends = nearby_people.intersection(user_friends)
print(near_by_friends)
"""
"""integer_division = 9 // 2 #gives round values 
print(integer_division)
float_division = 9/2 #gives float values
print(float_division)

modulas operter % that will give remainder

age = 34
print(f"your age is {age}")
"""
"""Formating the strings are very good"""

"""my_name = "Hemanth"
greeting = "how are you my boy {name}"
final_greeting = greeting.format(name=my_name)
print(final_greeting)"""

"""my_name = "hemanth"
greeting = f"how are you {my_name}"
print(greeting)"""
"""
name = input("enter your name : ")
print(f"Hello {name}")
age = int(input("enter your age: "))
months=12* age
print(f"your age is {months} in months")"""
"""age = int(input("Enter your age: "))
side_job = True
print(age > 18 and age < 65 or )"""