import json
import random
import time

# Load questions from JSON file
def load_questions():
    with open("questions.json", "r") as file:
        return json.load(file)

# Function to ask questions
def ask_question(question_data):
    print(f"\n{question_data['question']}")
    for idx, option in enumerate(question_data["options"], start=1):
        print(f"{idx}. {option}")

    start_time = time.time()  # Start timer
    answer = input("Your answer (1-4): ")
    elapsed_time = time.time() - start_time  # Calculate response time

    if elapsed_time > 10:  # 10 seconds limit
        print("⏳ Time's up! ❌")
        return False

    try:
        selected_option = int(answer) - 1
        if question_data["options"][selected_option] == question_data["answer"]:
            print("✅ Correct!")
            return True
        else:
            print(f"❌ Wrong! The correct answer is: {question_data['answer']}")
            return False
    except (ValueError, IndexError):
        print("⚠ Invalid input! Answer should be 1, 2, 3, or 4.")
        return False

# Main function to run the quiz
def run_quiz():
    questions = load_questions()
    random.shuffle(questions)  # Shuffle questions

    score = 0
    for question in questions:
        if ask_question(question):
            score += 1

    print(f"\n🎯 Your final score is {score}/{len(questions)}!")

# Start quiz
if __name__ == "__main__":
    print("\n🎉 Welcome to the Quiz App! 🎉")
    print("You have 10 seconds to answer each question. Good luck!\n")
    run_quiz()