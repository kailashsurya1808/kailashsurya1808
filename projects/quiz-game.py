questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Chennai", "C. New Delhi", "D. Kolkata"],
        "answer": "C"
    },
    {
        "question": "Which language are we learning?",
        "options": ["A. Python", "B. HTML", "C. CSS", "D. SQL"],
        "answer": "A"
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "A. Central Processing Unit",
            "B. Computer Personal Unit",
            "C. Central Program Utility",
            "D. Control Processing User"
        ],
        "answer": "A"
    }
]

score = 0

print("🧠 Welcome to the Quiz Game!")

for question in questions:
    print("\n" + question["question"])

    for option in question["options"]:
        print(option)

    user_answer = input("Your answer: ").strip().upper()

    if user_answer == question["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Incorrect!")

print("\n🎯 Quiz finished!")
print(f"Your score: {score}/{len(questions)}")