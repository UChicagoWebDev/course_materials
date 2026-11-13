# Lab 7: React Tic Tac Toe

**DUE: Friday, November 13 by 8:30pm**

We are going to work through (most of) a tutorial from the React documentation: https://reactjs.org/tutorial/tutorial.html. This folder provides some starter code so that we don't have to use an online IDE or a React build toolchain.

From this folder, run:

`python3 -m http.server`

That will let you see your Tic Tac Toe application at `http://localhost:8000`

## Rubric
1 point each for:
- Create pure functional components for Square and Board
- Use `useState` to hold which quares are marked
- Lift the state up to the Board component.
- Pass square values and handler functions as props.
- Clicking on an empty square puts the player's letter inside.
- Play alternates between X and O
- Display which player has the next move
- Do not overwrite squares that a player has already marked
- Display the winner
- Do not accept new moves on a completed game board

We're going to skip the "time travel" section, but feel free to review or complete it on your own.