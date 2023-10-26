*** Settings ***
Documentation     I want to print the output of the game stats to UI.
I want to pass on user input to the right classes.
I want to retreieve the information from the classes.
I want to terminate game when user desires to end the game.
I want to start game when user initializes.


Test Template     Move character
Library           MoveLibrary.py

*** Test Cases ***                  StartingX     StartingY     StartingMoveCount     Direction     EndingX     EndingY     EndingMoveCount
Move in the middle of the board 