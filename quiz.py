import json
import random

# Load questions from JSON file
def load_questions():
    with open("questions.json", "r") as file:
        return json.load(file)

# Save leaderboard scores to JSON file
def update_leaderboard(player_name, score):
    try:
        with open("leaderboard.json", "r") as file:
            leaderboard = json.load(file)
    except FileNotFoundError:
        leaderboard = {}

    leaderboard[player_name] = score

    with open("leaderboard.json", "w") as file:
        json.dump(leaderboard, file, indent=4)

# Display leaderboard
def display_leaderboard():
    try:
        with open("leaderboard.json", "r") as file:
            leaderboard = json.load(file)
            print("\n🏆 Leaderboard:")
            for player, score in sorted(leaderboard.items(), key=lambda x: x[1], reverse=True):
                print(f"{player}: {score}")
    except FileNotFoundError:
        print("\n🏆 Leaderboard is empty.")

# Main function to run the quiz
def run_quiz():
    questions = load_questions()
    random.shuffle(questions)  # Shuffle questions for variation

    score = 0  # Initialize score

    print("\n🎉 Welcome to the Quiz App! 🎉\n")

    for question in questions:
        print(question["question"])
        for index, option in enumerate(question["options"], start=1):
            print(f"{index}. {option}")

        answer = input("\nYour answer (enter the number): ")

        # Validate user input and check answer
        try:
            answer_index = int(answer) - 1
            if question["options"][answer_index].lower() == question["answer"].lower():
                print("✅ Correct!\n")
                score += 1
            else:
                print(f"❌ Wrong! The correct answer is: {question['answer']}\n")
        except (ValueError, IndexError):
            print("⚠ Invalid input! Please enter a valid option number.\n")

    print(f"\n📊 Your final score is {score}/{len(questions)}!")

    # Update and display leaderboard
    player_name = input("\nEnter your name for the leaderboard: ")
    update_leaderboard(player_name, score)
    display_leaderboard()

# Ensure script runs only when executed directly
if __name__ == "__main__":
    run_quiz()