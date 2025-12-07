# Number Guessing Game

This is a simple, text-based number guessing game written in Python. The player has to guess a randomly generated number within a given range. The game features an upgrade system that allows the player to improve their chances of winning.

The game is in Ukrainian.

## How to Run

1. Make sure you have Python 3.13 or higher installed.

2. Clone this repository.

3. Navigate to the project directory.

4. Run the game using the following command:

    ```bash

    python main.py

    ```

## Demo Video

[Link to video will be placed here]

## Gameplay

The goal of the game is to reach 100 points. You earn points by correctly guessing the number that the computer has chosen.

- At the beginning of each round, the computer picks a random number between 1 and 10.
- You have to enter a number to guess.
- If you guess correctly, you earn points, and a new round begins with a new number.
- If you guess incorrectly, you can try again.

## Upgrades

You can use the points you've earned to buy upgrades. To buy an upgrade, enter the corresponding negative number. The available upgrades are:

- **Bigger reward for winning:** Increases the number of points you get for a correct guess.
- **Smaller guessing range:** Reduces the range of possible numbers, making it easier to guess.
- **Chance to win even if you don't guess:** Gives you a chance to win the round even if your guess is incorrect.

Each upgrade has multiple levels, with each level providing a better bonus at a higher cost.
