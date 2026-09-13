# Simple Text Classifier 🤖

positive_words = ["good", "great", "excellent", "happy", "awesome", "love"]
negative_words = ["bad", "terrible", "sad", "hate", "awful", "poor"]

text = input("Enter a sentence: ").lower()

words = text.split()

positive_score = 0
negative_score = 0

for word in words:
    if word in positive_words:
        positive_score += 1
    elif word in negative_words:
        negative_score += 1

if positive_score > negative_score:
    result = "Positive"
elif negative_score > positive_score:
    result = "Negative"
else:
    result = "Neutral"

print(f"\nClassification: {result}")
print(f"Positive score: {positive_score}")
print(f"Negative score: {negative_score}")