import inquirer

print("Welcome to the history quiz!")


question = [
    inquirer.List("playing", message="Do you want to play?", choices=["Yes", "No"])
]

play = inquirer.prompt(question)
#test
