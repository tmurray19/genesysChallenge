# 5-in-a-Row Challenge - Taidgh Murray

## Assumptions
- I am trying only to using any packages native to Python, so no numpy
- Server will close when a game is won


## Game objective
- Players first choose colour
- Take turns dropping tokens down 6x9 grid
- First to form horizontal, vertical, or diagonal line of 5 wins

## Server
- Handles state and logic of game
- Lets users know who moves when
- HTTP based requests ideally
- Have server run first
- Then wait for conection from first socket
- Let first socket know it's looking for another player
- Then look for connection from second socket
- server interfaces between clients and game logic

## Client
- should only be asked for name, and where to place token
- asks for only column
- handle forceful close of client socket