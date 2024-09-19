import random

# Function to load questions from a text file
def load_questions(filename):
    """
    Load questions from the file and return a list of (question, answer) tuples.
    Each line in the file should have the format: question;answer
    """
    questions = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                question, answer = line.strip().split(';')
                questions.append((question, answer))
    except FileNotFoundError:
        print("Questions file not found.")
    return questions

# Function to save highscore to a text file
def save_highscore(score, filename='highscore.txt'):
    """
    Save the highscore to a file. If the new score is higher than the current highscore,
    it will overwrite the previous highscore.
    """
    try:
        with open(filename, 'r') as file:
            highscore = int(file.read().strip())
    except (FileNotFoundError, ValueError):
        highscore = 0

    if score > highscore:
        with open(filename, 'w') as file:
            file.write(str(score))
        print(f"New highscore: {score}!")
    else:
        print(f"Your score: {score}. Highscore remains: {highscore}.")

# Main function for the quiz game
def quiz_game():
    """
    Main logic of the quiz game. It loads the questions, asks the user to answer, and
    tracks the score. At the end, it saves the highscore.
    """
    questions = load_questions('questions.txt')
    if not questions:
        return

    score = 0
    random.shuffle(questions)

    for question, correct_answer in questions:
        user_answer = input(f"{question} ")
        if user_answer.strip().lower() == correct_answer.strip().lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {correct_answer}")

    print(f"Your final score: {score}/{len(questions)}")
    save_highscore(score)

# Run the quiz game
if __name__ == "__main__":
    quiz_game()
