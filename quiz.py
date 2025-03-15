import json
import random
import threading
import sys

# Load questions from JSON file
def load_questions():
    with open("questions.json", "r") as file:
        return json.load(file)

# Function to handle user input with a timer
def get_user_input(timeout):
    user_answer = [None]
    
    def input_with_timeout():
        user_answer[0] = input("Your answer: ")

    thread = threading.Thread(target=input_with_timeout)
    thread.start()
    thread.join(timeout)

    if thread.is_alive():
        print("\n⏳ Time's up! Moving to the next question.")
        thread.join()  # Ensure the thread stops
        return None  # No input was given
    return user_answer[0]

# Ask questions with a timer
def ask_questions(questions):
    score = 0

    for question in questions:
        print("\n" + question["question"])
        for i, option in enumerate(question["options"], start=1):
            print(f"{i}. {option}")

        user_answer = get_user_input(10)  # 10-second timer

        if user_answer is None:
            print(f"❌ The correct answer was: {question['answer']}")
        elif user_answer.lower() == question["answer"].lower():
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is: {question['answer']}")

    print(f"\nYour final score is {score}/{len(questions)}!")

# Main function
if __name__ == "__main__":
    questions = load_questions()
    random.shuffle(questions)  # Shuffle questions
    ask_questions(questions)