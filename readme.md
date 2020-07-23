# 5-in-a-Row Challenge - Taidgh Murray


## Game objective
- Players first choose colour
- Take turns dropping tokens down 6x9 grid
- First to form horizontal, vertical, or diagonal line of 5 wins

## Server
- Handles state and logic of game
- Lets users know who moves when
- HTTP based requests
- Have server run first
- Then wait for conection from first socket
- Let first socket know it's looking for another player
- Then look for connection from second socket

## Client
- should only be asked for name, and where to place token
- ask for column first, then row
- handle forceful close of client socket