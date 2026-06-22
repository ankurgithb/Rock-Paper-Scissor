Rock Paper Scissors Game

A simple command-line Rock Paper Scissors game built with Python.

Features

* Play against the computer
* Random computer moves using Python’s random module
* Score tracking for both player and computer
* First to 3 wins the match
* Input validation for incorrect choices

How It Works

The player chooses one of the following:

* stone
* paper
* scissors

The computer randomly selects its choice.

Rules

* Stone beats Scissors
* Scissors beats Paper
* Paper beats Stone
* Same choices result in a tie

The first player to reach 3 points wins the game.

Requirements

* Python 3.x

No external libraries are required.

Run the Game

python rps.py

Example Gameplay

choices: ['stone', 'paper', 'scissors']
Enter a choice: stone
Victory!
computer choice: scissors
player score: 1

Project Structure

rock-paper-scissors/
│
├── rps.py
└── README.md

Future Improvements

* Add a graphical interface with Streamlit
* Add best-of-5 and best-of-7 modes
* Track match history
* Add difficulty levels
* Deploy online using Streamlit Cloud or Hugging Face Spaces

Author

Created as a Python practice project to learn programming fundamentals, game logic, and user interaction.
