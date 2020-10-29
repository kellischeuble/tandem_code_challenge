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
        answer_dict[str(i)] = answer
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
    print(f"The answer is {question['answer']}")
    if answer_dict[answer] == question['answer']:
        print("You got it correct! :)")
    else:
        print("You got it incorrect! :(")
    
def display_correct_answer(question, correct):
    """
    Prints out question
    Prints out correct answer
    Prints out messages saying if they got it correct
    """

def ask_if_ready():
    return True
    ready = input("Are you ready to play some Trivia? y/n ").lower().strip()
    if ready == 'y':
        return True
    elif ready == 'n':
        print("Next time, then!")
        return False
    else:
        print("Invalid entry")
        return False


def play():

    if ask_if_ready():
        round = 1
   
        questions = original_questions.copy()
        reset_questions(questions)

        while round <= 10:

            question, answer, answer_dict = ask_question(questions, round)
            check_answer(answer, answer_dict, question)



            round += 1

play()



