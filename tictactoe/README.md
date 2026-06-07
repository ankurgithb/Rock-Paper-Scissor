# TIC TAC TOE
#### Video Demo:  <[https://youtu.be/e18lFeHXE7M?si=1T2XA7jyrmLQP_fj]>
#### Description:


Tic Tac Toe is a classic two-player game played on a 3×3 grid. The game involves two players taking turns to mark their respective symbols—“X” or “O”—on empty spaces of the grid. The objective is to place three of one’s symbols in a horizontal, vertical, or diagonal line. If all positions on the board are filled without any player achieving this goal, the game results in a tie.

The aim of this project is to implement a terminal-based Tic Tac Toe game in Python that allows two players to play interactively. The program provides a dynamic display of the game board, validates user input, detects winning conditions, and allows multiple games to be played consecutively.

⸻

2. Program Structure

The program is implemented using Python and consists of the following main components:
	1.	Module Import
The os module is imported to interact with the operating system for clearing the terminal screen, ensuring that the game display is updated after each move.
	2.	Game Initialization
The program uses a boolean variable play to control whether the user wants to continue playing. The game board is represented as a list of nine elements, each initialized to "-" to indicate empty spaces. Other key variables include:
	•	currentPlayer: Tracks whose turn it is, starting with "X".
	•	winner: Stores the winner of the game, initially set to None.
	•	gameRunning: Controls the inner game loop, ensuring the game continues until a win or tie.
	3.	Displaying the Board
A function gameboard(board) prints the current state of the 3×3 board in a readable format, using the board list indices. Visual separators are used to clearly demarcate rows and columns for the player.
	4.	Main Game Loop
The program uses a nested loop structure:
	•	Outer loop (while play): Controls multiple rounds of the game, allowing the user to play again after one game ends.
	•	Inner loop (while gameRunning): Handles a single game session, continuing until a player wins or the game ties.

⸻

3. Input Handling and Validation

During a player’s turn, the program prompts the user to input a move between 0 and 8, corresponding to the board positions. The program ensures robust input handling by:
	•	Using a try-except block to handle non-integer inputs.
	•	Checking if the input is within the valid range (0-8).
	•	Ensuring that the selected board position is empty before accepting the move.
	•	Providing clear feedback to the player in case of invalid input.

This mechanism prevents invalid or illegal moves and maintains the integrity of the game.

⸻

4. Game Logic

4.1 Switching Turns

After a valid move, the program switches the current player from "X" to "O" or vice versa using a simple conditional statement. This ensures alternate turns between the two players.

4.2 Winning Conditions

The program explicitly checks all possible winning combinations:
	•	Horizontal: Top, middle, and bottom rows.
	•	Vertical: Left, middle, and right columns.
	•	Diagonal: From top-left to bottom-right, and top-right to bottom-left.

If a winning combination is detected, the game ends, and the winner is announced.

4.3 Tie Condition

If all positions on the board are filled ("-" not present) without any player winning, the game is declared a tie. The program handles this scenario gracefully, ensuring accurate game outcomes.

⸻

5. User Interaction

The program provides an interactive and user-friendly interface:
	•	The terminal screen is cleared before each turn for a dynamic display of the board.
	•	The current player is displayed to indicate whose turn it is.
	•	Clear messages are printed when invalid moves are attempted or when a player wins or the game ties.
	•	At the end of each game, the program asks the player if they want to play again, supporting both y/n and yes/no inputs.

⸻

6. Program Flow
	1.	Initialize variables and board.
	2.	Display the empty board.
	3.	Prompt the current player for a move.
	4.	Validate and update the board.
	5.	Check for a win or tie.
	6.	Switch the current player.
	7.	Repeat steps 3–6 until the game ends.
	8.	Announce the result.
	9.	Ask the player whether to play again.
	10.	Repeat steps 1–9 if the player chooses to continue.

⸻

7. Key Features
	•	Robust Input Validation: Handles invalid input gracefully.
	•	Dynamic Board Display: Clears the terminal for real-time updates.
	•	Win/Tie Detection: Checks all possible winning combinations and tie conditions.
	•	Replay Feature: Allows multiple rounds without restarting the program.
	•	User-Friendly Messages: Provides clear instructions, feedback, and game status updates.

⸻

8. Limitations and Future Improvements

While the program is fully functional, there are opportunities to enhance it further:
	•	Use loops to check winning conditions dynamically instead of hardcoding each possibility.
	•	Implement a single-player mode with a basic AI opponent.
	•	Maintain a scoreboard to track wins across multiple rounds.
	•	Use colored output to improve readability, e.g., highlighting X and O.
	•	Improve input handling to allow more intuitive board coordinates (row/column instead of 0–8).

⸻

9. Conclusion

This project demonstrates the implementation of a classic Tic Tac Toe game in Python. The program successfully manages player turns, validates moves, detects winning conditions, handles ties, and allows repeated play. It emphasizes key programming concepts such as loops, conditionals, functions, input validation, and data structures (lists).

The project provides a foundation for learning more advanced game programming techniques, including AI, GUI integration, and dynamic rule handling. It also highlights the importance of user interaction and input validation in software development.

⸻

10. References
	•	Python Documentation: https://docs.python.org/3/￼
	•	Tic Tac Toe Game Concepts: https://en.wikipedia.org/wiki/Tic-tac-toe￼
