# soccer_league

# Description

A simple Python, command-line application that will calculate the ranking table for a soccer league.

The following rules are applied : 

- In this league, a draw (tie) is worth 1 point and a win is worth 3 points. A loss is worth 0points. 
If two or more teams have the same number of points, they should have the same
rank and be printed in alphabetical order (as in the tie for 3rd place in the sample
data).

SAMPLE INPUT:

Lions 3, Snakes 3

Tarantulas 1, FC Awesome 0

Lions 1, FC Awesome 1

Tarantulas 3, Snakes 1

Lions 4, Grouches 0

EXPECTED OUTPUT

1. Tarantulas, 6 pts

2. Lions, 5 pts

3. FC Awesome, 1 pt

3. Snakes, 1 pt

5. Grouches, 0 pts


# Requirements

Python 3.7.0 or 3.7.x

No additional dependencies or pip requirements.txt

# Run with sample data

- Assumption : all files are in the same directory

- A text file is provided with samples of game results : teams.txt

- Use the relevant "python" command (based on your settings) to run the script, reading the text file from the "command line":

  ```
  python start.py < teams.txt
  
  ```
  
  Terminal Output :
  
  ```
  
  1. Tarantulas,  6 pts
  2. Lions,  5 pts
  3. FC Awesome,  1 pt
  4. Snakes,  1 pt
  5. Grouches,  0 pts
  
  ```

# Run Tests

- the following command can be used to run the test file:

```
python -m unittest test_league.py

```
