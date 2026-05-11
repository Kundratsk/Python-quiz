"""
Quiz Game Score System
OOP Exercise for Beginners

Author: Python beginner
Date: 2026
"""

import json
import os
from datetime import datetime


class Player:
    """
    Class representing a single player.

    Attributes:
        name (str): Player name
        score (int): Player score
        date (str): When the game was played
    """

    def __init__(self, name):
        """
        Constructor - creates a new player.

        Args:
            name (str): Player name
        """
        self.name = name
        self.score = 0
        self.date = datetime.now().strftime("%d.%m.%Y %H:%M")

    def add_points(self, points):
        """
        Adds points to the player score.

        Args:
            points (int): Number of points to add
        """
        self.score += points

    def __str__(self):
        """
        String representation of the player.
        Called when using print(player).
        """
        return f"{self.name}: {self.score} points ({self.date})"

    def to_dict(self):
        """
        Converts player to dictionary for saving.

        Returns:
            dict: Player data dictionary
        """
        return {
            "name": self.name,
            "score": self.score,
            "date": self.date
        }


class Question:
    """
    Class representing a single quiz question.

    Attributes:
        question (str): Question text
        options (list): Answer options (A, B, C, D)
        correct_answer (str): Correct answer (A, B, C or D)
    """

    def __init__(self, question, options, correct_answer):
        """
        Constructor - creates a new question.

        Args:
            question (str): Question text
            options (list): 4 answer options
            correct_answer (str): Correct answer (A, B, C or D)
        """
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

    def check_answer(self, user_answer):
        """
        Checks if the answer is correct.

        Args:
            user_answer (str): User's answer

        Returns:
            bool: True if correct, False otherwise
        """
        return user_answer.upper() == self.correct_answer


class Quiz:
    """
    Class containing quiz questions and logic.

    Attributes:
        questions (list): List of Question objects
    """

    def __init__(self):
        """
        Constructor - initializes quiz questions.
        """
        self.questions = [
            Question(
                "What is the capital of Estonia?",
                ["A) Tartu", "B) Tallinn", "C) Pärnu", "D) Narva"],
                "B"
            ),
            Question(
                "What is 5 + 7?",
                ["A) 10", "B) 11", "C) 12", "D) 13"],
                "C"
            ),
            Question(
                "Which planet is closest to the Sun?",
                ["A) Mars", "B) Venus", "C) Mercury", "D) Jupiter"],
                "C"
            ),
            Question(
                "Which animal is the fastest land animal?",
                ["A) Lion", "B) Cheetah", "C) Antelope", "D) Rabbit"],
                "B"
            ),
            Question(
                "What year did Estonia gain independence?",
                ["A) 1918", "B) 1920", "C) 1944", "D) 1991"],
                "A"
            )
        ]

    def get_question(self, index):
        """
        Gets a question by index.

        Args:
            index (int): Question number

        Returns:
            Question: Question object
        """
        return self.questions[index]

    def get_total_questions(self):
        """
        Returns total number of questions.

        Returns:
            int: Number of questions
        """
        return len(self.questions)


class ScoreBoard:
    """
    Class for storing leaderboard data.

    Attributes:
        players (list): List of Player objects
        filename (str): File name for saving data
    """

    def __init__(self, filename="scoreboard.json"):
        """
        Constructor - initializes scoreboard.

        Args:
            filename (str): File name
        """
        self.players = []
        self.filename = filename
        self.load_from_file()

    def add_player(self, player):
        """
        Adds a player to leaderboard.

        Args:
            player (Player): Player object
        """
        self.players.append(player)
        self.save_to_file()
        print(f"Player '{player.name}' added to leaderboard!")

    def display_top_players(self, limit=10):
        """
        Displays top players.

        Args:
            limit (int): Number of top players to show
        """
        if len(self.players) == 0:
            print("\nNo players in leaderboard!")
            return

        sorted_players = sorted(self.players, key=lambda p: p.score, reverse=True)

        print("\n" + "="*60)
        print("LEADERBOARD (TOP 10)")
        print("="*60)

        for i, player in enumerate(sorted_players[:limit], 1):
            medal = "1." if i == 1 else "2." if i == 2 else "3." if i == 3 else f"{i}."
            print(f"{medal} {player.name}: {player.score} points ({player.date})")

        print("="*60 + "\n")

    def save_to_file(self):
        """
        Saves players to JSON file.
        """
        data = [player.to_dict() for player in self.players]

        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load_from_file(self):
        """
        Loads players from JSON file.
        """
        if not os.path.exists(self.filename):
            return

        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)

                for item in data:
                    player = Player(item['name'])
                    player.score = item['score']
                    player.date = item['date']
                    self.players.append(player)

            print(f"Loaded {len(self.players)} players!")
        except json.JSONDecodeError:
            print("Error reading file!")


def play_game():
    """
    Main game function.
    """
    print("\n" + "="*60)
    print("WELCOME TO THE QUIZ GAME")
    print("="*60 + "\n")

    quiz = Quiz()
    scoreboard = ScoreBoard()

    player_name = input("Enter your name: ").strip()

    if not player_name:
        player_name = "Anonymous player"

    player = Player(player_name)

    print(f"\nHello, {player.name}!")
    print(f"Answer {quiz.get_total_questions()} questions.")
    print("Each correct answer gives 20 points!\n")

    for i in range(quiz.get_total_questions()):
        question = quiz.get_question(i)

        print(f"\n{'-'*60}")
        print(f"Question {i + 1}/{quiz.get_total_questions()}: {question.question}")
        print(f"{'-'*60}")

        for option in question.options:
            print(option)

        while True:
            answer = input("Your answer (A/B/C/D): ").strip()
            if answer.upper() in ['A', 'B', 'C', 'D']:
                break
            print("Please choose A, B, C or D!")

        if question.check_answer(answer):
            player.add_points(20)
            print("Correct answer! +20 points")
        else:
            print(f"Wrong answer! Correct was: {question.correct_answer}")

    print("\n" + "="*60)
    print("GAME OVER")
    print("="*60)
    print(f"\nYour score: {player.score} points")
    print(f"Maximum possible score: {quiz.get_total_questions() * 20}")

    scoreboard.add_player(player)
    scoreboard.display_top_players()


def main():
    """
    Main menu.
    """
    while True:
        print("\n" + "="*60)
        print("QUIZ GAME MENU")
        print("="*60)
        print("1. Play game")
        print("2. View leaderboard")
        print("3. Exit")

        choice = input("Choose (1-3): ").strip()

        if choice == "1":
            play_game()
        elif choice == "2":
            scoreboard = ScoreBoard()
            scoreboard.display_top_players()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
