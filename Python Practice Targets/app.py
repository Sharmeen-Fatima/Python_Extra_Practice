# TARGET PYTHON PRACTICE DAY ONE 24:FEB:2025

print(f"\n----------------------------First Day Python Practice----------------------------------\n")

Name = "Sharmeen Fatima"
print(f"Hello, Python Learners! 🚀. I'm {Name} Today is the first step in our coding journey.")


# Python second practice [Day 2] {25:FEB:2005}.

print(f"\n----------------------------Second Day Python Practice----------------------------------\n")

# Practice 25:Feb:2025

User_input = input("Type any sentance for python..")
word_breck = User_input.split()
sentance_word =len(word_breck)
print(f"{User_input}\n There are {sentance_word} words in this sentance.")

# "Bonus Practice"

def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])

input_text = input("Write any sentances who you need reverse word.")
output_text = reverse_words(input_text)
print(output_text) 

