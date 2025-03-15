print("Welcome to the Quiz App!")

questions = {
    "What is the capital of France?": "Paris",
    "What is 5 + 7?": "12",
    "Who developed Python?": "Guido van Rossum"
}

score = 0
for question, answer in questions.items():
    user_answer = input(question + " ")
    if user_answer.strip().lower() == answer.lower():
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong! The correct answer is:", answer)

print(f"\nYour final score is {score}/{len(questions)}!")
