# 🎯 Quiz Game 📝

Welcome to the **Quiz Game**! This is a simple Python-based quiz game where users answer a series of questions and try to achieve the highest score possible. Test your knowledge and see if you can set a new highscore! 🏆

## 📂 Project Structure

Here's an overview of the files and their purposes in the project:

quiz_game/
│
├── .venv/                 # Virtual environment for the project dependencies
├── github/
│   └── workflows/
│       └── ci.yml        # Continuous integration workflow configuration
│
├── tests/
│   ├── test_main.py      # Unit tests for the main functionalities
│   ├── highscore.txt     # File to store the highscore
│
├── main.py               # Main script for the quiz game logic
├── questions.txt         # Text file containing quiz questions and answers
├── README.md             # Project documentation (you are here!)
├── requirements.txt      # Project dependencies
│
└── .venv/                # Virtual environment directory


## 🛠️ How It Works

### `main.py` 📄

- **Functions**:
  - `load_questions(filename)`: Loads questions from a specified file and returns a list of `(question, answer)` tuples.
  - `save_highscore(score, filename)`: Saves the highscore to a text file. If the new score is higher than the current highscore, it overwrites the previous highscore.
  - `quiz_game()`: Contains the main game logic. It loads questions, asks the user to answer, and tracks the score. At the end, it saves the highscore.

- **Usage**:
  Run `main.py` to start the quiz game. The game will ask a series of questions from `questions.txt`. Answer them correctly to achieve a high score!

### `tests/test_main.py` 🧪

- **Unit Tests**:
  - Tests for `load_questions()` ensure questions are loaded correctly from a file.
  - Tests for `save_highscore()` check if the highscore is updated correctly based on new scores.

## 📜 Questions File Format

The `questions.txt` file contains quiz questions and answers in the following format:

Question;Answer


For example:

Who is known as the 'King of Pop'?;Michael Jackson
Which British band released the album 'Abbey Road'?;The Beatles


## 🚀 Running the Game

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/quiz_game.git
    cd quiz_game
    ```

2. **Install Dependencies**:
    Ensure you have a virtual environment set up, then install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Game**:
    ```bash
    python main.py
    ```

4. **Answer the Questions**:
   Type your answers when prompted. At the end of the game, your score will be displayed and saved.

## 🧪 Running Tests

To run the unit tests, execute:

```bash
python -m unittest discover tests
```

### 📝 License
This project is open-source and available under the [MIT License](LICENSE).


## 💡 Contributions

Contributions are welcome! Feel free to open issues or submit pull requests to improve the game.

Enjoy playing the Quiz Game and try to beat the highscore! 🎉