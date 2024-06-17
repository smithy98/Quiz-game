import inquirer

print("Welcome to the history quiz!")


start = [
    inquirer.List("playing", message="Do you want to play?", choices=["Yes", "No"])
]

play = inquirer.prompt(start)

if play["playing"] != "Yes":
    quit()

questions = [
    inquirer.List(
        "Q1",
        message="Who invaded Poland in 1939, starting WW2?",
        choices=["Adolf Hitler", "Napoloen Bonapart", "Queen Elizabeth"],
    ),
    inquirer.List(
        "Q2",
        message="What year did the battle of Waterloo happen?",
        choices=["1793", "1805", "1815", "1836"],
    ),
]

question_time = inquirer.prompt(questions)

print(questions)
