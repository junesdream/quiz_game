import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import load_questions, save_highscore

class TestQuizGame(unittest.TestCase):

    def setUp(self):
        """
        Setup that runs before every test. It creates a test question file and a highscore file.
        """
        # Create a temporary question file for testing
        with open('test_questions.txt', 'w') as file:
            file.write("Who is the 'King of Pop'?;Michael Jackson\n")
            file.write("Which band released 'Abbey Road'?;The Beatles\n")

        # Create a temporary highscore file for testing
        with open('test_highscore.txt', 'w') as file:
            file.write("5")

    def tearDown(self):
        """
        Cleanup that runs after every test. It removes the test files.
        """
        # Remove the test files after testing
        os.remove('test_questions.txt')
        os.remove('test_highscore.txt')

    def test_load_questions(self):
        """
        Test if the load_questions method correctly reads questions from the file.
        """
        questions = load_questions('test_questions.txt')
        expected_questions = [
            ("Who is the 'King of Pop'?", 'Michael Jackson'),
            ("Which band released 'Abbey Road'?", 'The Beatles')
        ]
        self.assertEqual(questions, expected_questions)

    def test_save_highscore_new_highscore(self):
        """
        Test if save_highscore correctly updates the highscore when a new highscore is reached.
        """
        save_highscore(10, 'test_highscore.txt')
        with open('test_highscore.txt', 'r') as file:
            highscore = int(file.read().strip())
        self.assertEqual(highscore, 10)

    def test_save_highscore_no_update(self):
        """
        Test if save_highscore does not update when the new score is lower than the highscore.
        """
        save_highscore(3, 'test_highscore.txt')
        with open('test_highscore.txt', 'r') as file:
            highscore = int(file.read().strip())
        self.assertEqual(highscore, 5)

if __name__ == '__main__':
    unittest.main()
