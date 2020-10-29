import json
import random

original_questions = json.load(open('./src/data/Apprentice_TandemFor400_Data.json', 'r'))

def reset_questions(questions):
    """
    shuffles questions for order
    """
    random.shuffle(questions)

def display_possible_answers(question):
    """
    shuffles and displays all possible anwers
    """
    answers = question['incorrect'] + [question['correct']]
    random.shuffle(answers)
    answer_dict = {}
    for i, answer in enumerate(answers):
        answer_dict[str(i + 1)] = answer
        print(f"{i + 1}: {answer}\n")
    return answer_dict     

def ask_question(questions, round):
    """
    pops question off of list to ask
    displays all possible answers
    """
    question = questions.pop()
    print(f"\nQuestion number {round}:")
    print("-"*20)
    print(question['question'])
    print()
    
    answer_dict = display_possible_answers(question)

    return input("What is your answer?: ").strip(), answer_dict, question

def check_answer(answer, answer_dict, question):
    """
    Checks answer
    Returns True if answer is correct
    """
    print(f"\nThe answer is:  {question['correct']}")

    if answer_dict[answer] == question['correct']:
        print("You got it correct! :)")
        return True
    else:
        print("You got it incorrect! :(")
        return False

def ask_if_ready(stage_of_game):
    if stage_of_game == "beginning":
        ready = input("Are you ready to play some Trivia? y/n ").lower().strip()
    elif stage_of_game == "end_of_question":
        ready = input("\nAre you ready for the next question? y/n ").lower().strip()
    if ready == 'y':
        return True
    elif ready == 'n':
        print("Next time, then!")
        return False
    else:
        print("Invalid entry")
        return False


def play():

    if ask_if_ready("beginning"):
        round = 1
        current_score = 0
   
        questions = original_questions.copy()
        reset_questions(questions)

        while round <= 10:

            answer, answer_dict, question, = ask_question(questions, round)
            if check_answer(answer, answer_dict, question):
                current_score += 1
            if round < 10:
                if ask_if_ready("end_of_question"):
                    round += 1
                else: break

        print(f"\nYour final score is: {current_score}")

play()



