import requests
import json
import pprint
import random
import os


# Generate API here for questions
url = "https://opentdb.com/api.php?amount=1&category=18"
# url = "https://opentdb.com/api.php?amount=1"
endGame = ""
score_correct = 0
score_incorrect = 0
# valid_answer = False

while endGame != 'quit':
    r = requests.get(url)
    if(r.status_code != 200):
        endGame = input("Sorry, there was a problem. Try again or type 'quit' to exit.")
    else:
        valid_answer = False
        answer_number = 1
        result_text = json.loads(r.text)
        category = result_text['results'][0]['category']
        question = result_text['results'][0]['question']
        correct_answer = result_text['results'][0]['correct_answer']
        answers = result_text['results'][0]['incorrect_answers']
        answers.append(correct_answer)
        random.shuffle(answers)

        print("--------------------------------------------------------------")
        print(question)
        # print(html.unescape(question) + "\n")

        for answer in answers:
            print(str(answer_number) + "_ " + answer)
            answer_number += 1

        while valid_answer == False:
            user_answer_no = input("\nType the no of correct answer: ")
            try:
                user_answer_no = int(user_answer_no)
                if user_answer_no > len(answers) or user_answer_no <= 0:
                    print("Invalid Answer")
                valid_answer = True
            except:
                print("Invalid!")
        
        user_answer = answers[int(user_answer_no)-1]

        if user_answer == correct_answer:
            print("\nCongratulations!!! Your answer is correct: " + correct_answer)
            score_correct += 1
        else:
            print("\nSorry, Your answer '" + user_answer + "' is wrong! Correct answer is: '" + correct_answer + "'")
            score_incorrect += 1

        print("\nYour score is : ")
        print("Correct answers : " + str(score_correct))
        print("Incorrect answers : " + str(score_incorrect))
        print("--------------------------------------------------------------")

        endGame = input("\nPress Enter to play again or type 'quit'.").lower()
        os.system('clear')
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

print("\nThanks for playing!!!")
