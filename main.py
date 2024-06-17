import inquirer

print("Welcome to the capital city quiz!")


start = [
    inquirer.List("playing", message="Do you want to play?", choices=["Yes", "No"])
]

play = inquirer.prompt(start)

if play["playing"] != "Yes":
    quit()

questions = [
    inquirer.List(
        "Q1",
        message="What is the capital of Poland",
        choices=[
            "Krakow",
            "Dresden",
            "Warsaw",
            "Vilnius",
        ],
    ),
    inquirer.List(
        "Q2",
        message="What year did the battle of Waterloo happen?",
        choices=["1793", "1805", "1815", "1836"],
    ),
    inquirer.List(
        "Q3",
        message="What year did the battle of Waterloo happen?",
        choices=["1793", "1805", "1815", "1836"],
    ),
    inquirer.List(
        "Q4",
        message="What year did the battle of Waterloo happen?",
        choices=["1793", "1805", "1815", "1836"],
    ),
    inquirer.List(
        "Q5",
        message="What year did the battle of Waterloo happen?",
        choices=["1793", "1805", "1815", "1836"],
    ),
    inquirer.List(
        "Q6",
        message="What year did the battle of Waterloo happen?",
        choices=["1793", "1805", "1815", "1836"],
    ),
]

answers = {"Q1": "Adolf Hitler", "Q2": "1815"}

question_time = inquirer.prompt(questions)

# print(question_time)

score = 0

for x in answers:
    # print(question_time[x])
    if question_time[x] == answers[x]:
        score += 1

print(score, f"out of {len(answers)}")
