# import random
# from turtle import Turtle, Screen
# my_sc=Screen()
# my_sc.setup(height=500,width=500)
# # tim=Turtle(shape="turtle")
# # tim.color("red")
# # tim.penup()
# # tim.goto(-250,0)

# # timmy=Turtle(shape="turtle")
# # timmy.color("green")
# # timmy.penup()
# # timmy.goto(-250,30)
# color = ["red","green","purple","orange","lime","blue"]
# Y_position = [0,30,-30,60,-60,90]
# all_turtle = []
# for i in range(0,6):
#     timmy2=Turtle(shape="turtle")
#     timmy2.color(color[i])
#     timmy2.penup()
#     timmy2.goto(x=-250,y=Y_position[i])
#     all_turtle.append(timmy2)
# user_bet = my_sc.textinput(title="make your bet" , prompt="which color will win the race? enter color:")
# if user_bet:
#     race_is_on= True
# while race_is_on:
#     for turtle in all_turtle:
#         if turtle.xcor()>230:
#             race_is_on = False
#             winner_color = turtle.pencolor()
#             if winner_color == user_bet:
#                 print(f"you've won, the {winner_color} won the race")
#             else:
#                 print(f"you've lost, the {winner_color} won the race")
#         rand_distance = random.randint(0,10)
#         turtle.forward(rand_distance)
# my_sc.exitonclick()
import random
from turtle import Turtle, Screen

# Setting up the screen
screen = Screen()
screen.setup(width=600, height=500)
screen.bgcolor("black")  # Background color for better aesthetics
screen.title("Turtle Race Game")

# List of turtle colors and their starting Y-positions
colors = ["red", "green", "purple", "orange", "blue", "yellow"]
y_positions = [0, 30, -30, 60, -60, 90]
all_turtles = []

# Creating turtles dynamically and positioning them at the starting line
for i in range(len(colors)):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(x=-250, y=y_positions[i])  # Starting position
    all_turtles.append(turtle)  # Adding turtle to the list

# Asking user for their bet
user_bet = screen.textinput(title="Make Your Bet", prompt="Which color turtle will win the race? Enter a color:")

# Starting the race if a bet is placed
if user_bet:
    race_is_on = True
else:
    race_is_on = False

# Race logic
while race_is_on:
    for turtle in all_turtles:
        # Checking if a turtle crosses the finish line (right side of the screen)
        if turtle.xcor() > 250:
            race_is_on = False
            winning_color = turtle.pencolor()
            # Declaring the result based on user's bet
            if winning_color == user_bet:
                print(f"Congratulations! You won! The {winning_color} turtle is the winner!")
            else:
                print(f"Sorry, you lost. The {winning_color} turtle won the race.")
            break  # Exiting the loop when a winner is found

        # Moving the turtles randomly forward
        rand_distance = random.randint(1, 10)  # Random speed between 1 and 10
        turtle.forward(rand_distance)

# Clicking on the screen closes the game
screen.exitonclick()