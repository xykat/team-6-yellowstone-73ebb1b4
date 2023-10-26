*** Settings ***
Documentation     I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
Test Template     Move character
Library           MoveLibrary.py

*** Test Cases ***                  StartingX     StartingY     StartingMoveCount     Direction     EndingX     EndingY     EndingMoveCount
Move in the middle of the board     0             0             1                     NORTH         0           1           2
Move on the edge of the board       0             0             5                     SOUTH         0           0           6
User1                               0             0             0                     NORTH         0           1           1
ERIN1                                0             0             0                    SOUTH         0           0           1
RICK1                                0             0             0                    EAST          1           0           1
JP1                                  0             0             0                    WEST          0           0           1
User2                                5             5             10                    NORTH         5           6           11
ERIN2                                5             5             10                   SOUTH         5           4           11
RICK2                                9             9             15                   EAST          9           9           16
JP2                                  5             9             19                   WEST          4           9           20      
RICK3                                7             8             5                    SOUTH         7           7           6     

*** Keywords ***
Move character
    [Arguments]    ${startingX}    ${startingY}    ${startingMoveCount}    ${direction}    ${endingX}    ${endingY}    ${endingMoveCount}
    Initialize character xposition with  ${startingX}
    Initialize character yposition with  ${startingY}
    Initialize character moveCount with  ${startingMoveCount}
    Move in direction  
                  ${direction}
    Character xposition should be        ${endingX}
    Character yposition should be        ${endingY}
    Character moveCount should be        ${endingMoveCount} 