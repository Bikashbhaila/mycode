#!/usr/bin/env python3

import requests

BASE_API_URL = "https://opentdb.com/api.php?"
user_choices = {}

# get user choices and create URI based on the choice
def getUserChoices():
    diff_levels = ["easy", "medium", "hard"]
    diff_level = ""
    num_questions = 0
    try:
        while num_questions < 3 :
            num_questions = int(input("How many questions? >> "))
            if num_questions >= 3:
                while diff_level not in diff_levels:
                    diff_level = input(f"Please select diff level: {diff_levels}\n>> ").strip().lower()
    
                    user_choices["num_questions"] = str(num_questions)
                    user_choices["diff_level"] = diff_level
    except ValueError as response:
        print(response)
        print("Non-numerical value entered for questions")
        exit()


def startQuiz():
    user_score = 0
    API_URL = BASE_API_URL + "amount=" + user_choices["num_questions"] + "&difficulty=" + user_choices["diff_level"]
    print(API_URL)
    response = requests.get(API_URL)
    trivia_dict = response.json().get("results")
    for trivia in trivia_dict:
        user_answer = input(trivia["question"].strip() + "\n>> ").strip().lower()
        if user_answer == trivia["correct_answer"].lower():
            user_score += 1
            print("CORRECT.. Great work!!!")
        else:
            print("WRONG!!! The correct answer is: ", trivia["correct_answer"])
    print(f"Your FINAL SCORE is", user_score, "out of", user_choices["num_questions"])

def main():
    
    while True:
        getUserChoices()
        startQuiz()

        wantRestart = input("Do you want to play again? [Yes/No]\n>> ").lower()
        if wantRestart == "yes":
            print("Sure, good luck this time")
            continue
        else:
            print("Thanks for playing")
            break

if __name__ == "__main__":
    main()

