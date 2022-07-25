import random
import time
def game():
	choices = ["rock","paper","scissors"]
	computer = random.choice(choices)
	player = None

	while player not in choices:
		player = input("choose any one: rock, paper, scissors?:-> ").lower()

	if player==computer:
		print("Computer: ",computer)
		print("Player: ",player)
		print("Tie")
	elif player=="rock":
		if computer=="scissors":
			print("Computer: ",computer)
			print("Player: ",player)
			print("you lose!")
		if computer=="paper":
			print("Computer: ",computer)
			print("Player: ",player)
			print("you win!")
	elif player=="paper":
		if computer=="scissors":
			print("Computer: ",computer)
			print("Player: ",player)
			print("you lose!")
		if computer=="rock":
			print("Computer: ",computer)
			print("Player: ",player)
			print("Tie")
	elif player=="scissors":
		if computer=="paper":
			print("Computer: ",computer)
			print("Player: ",player)
			print("you win!")
		if computer=="paper":
			print("Computer: ",computer)
			print("Player: ",player)
			print("you lose!")
game()
while True:			
	play_again = input("Do you want to play it again:(yes/no) :->").lower()
	if play_again == "yes":
		game()
	else:
		print("ok, see you later!!!")
		break