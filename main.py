import inquirer
import json
from random import randrange

print("Welcome to the capital city quiz!")

with open("capital_cities.json", "r") as read_file:
    data = json.load(read_file)

start = [
    inquirer.List("playing", message="Do you want to play?", choices=["Yes", "No"])
]

play = inquirer.prompt(start)

if play["playing"] != "Yes":
    quit()

answers = {}

for _ in range(10):
    rand_num = randrange(len(data["Capital city"]))
    answers[data["Capital city"][rand_num]["CountryName"]] = data["Capital city"][
        rand_num
    ]["CapitalName"]

questions = []

for key, value in answers.items():
    questions.append(
        inquirer.Text(
            f"{key}",
            message=f"What is the capital of {key}",
        )
    )

question_time = inquirer.prompt(questions)

score = 0

for key, value in question_time.items():
    if answers[key] == value:
        score += 1


print(score, f"out of {len(answers)}")
