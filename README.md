# Tic-Tac-Toe - Alpha-Beta Pruning AI

A compact Tic-Tac-Toe game implemented in Python with a simple AI that uses Minimax and Alpha-Beta pruning. Built with Pygame and NumPy. This repo contains a playable GUI, a clear AI implementation, and room for improvements and experiments.

---

## Demo / Screenshots

### AI plays as Circle

![AI as Circle](https://github.com/user-attachments/assets/ec074965-2d28-442b-bcc2-44ed6db0c80e)

### Resetting the Game (`R` key)

![Reset example](https://github.com/user-attachments/assets/0613f371-0537-4622-a714-694b8f72ed85)

### Another Game in Action

![Another game](https://github.com/user-attachments/assets/1a572483-1cdf-4930-99b0-7166cc81fb43)

### Human Starts First (self.player = 1)

![Human starts first](https://github.com/user-attachments/assets/62785557-60c4-44e5-b2f0-a18d62bb990b)

---

## Features

* Play Tic-Tac-Toe with a GUI powered by Pygame.
* AI opponent implemented with Minimax and Alpha-Beta pruning.
* Two AI behaviors:

  * Level 0 - Random moves.
  * Level 1 - Full Minimax + Alpha-Beta pruning.
* Keyboard controls to change mode, restart, and switch AI level.
* Clean, compact code base - easy to extend.

---

## Quick start

1. Create and activate a virtual environment (recommended):

```bash
python -m venv venv
# macOS / Linux
source venv/bin/activate
# Windows
venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install pygame numpy
```

3. Run the game:

```bash
python py-ttt-neat.py
```

---

## Controls

* Left mouse click - place your mark (when it is the human's turn).
* `g` - toggle game mode between PvP and AI.
* `r` - restart the game.
* `0` - set AI to random mode.
* `1` - set AI to Minimax + Alpha-Beta mode.

> Note: By default, the AI is player 2 and starts first. If you set `self.player = 1` in the code, the human starts first.

---

## How the AI works (high level)

The AI uses the Minimax algorithm with Alpha-Beta pruning to choose optimal moves. A simple evaluation function is used:

* `+1` if player 1 wins.
* `-1` if player 2 (AI) wins.
* `0` for a draw or non-terminal position at leaf depth.

Pseudocode used by the implementation:

```text
function minimax(board, maximizingPlayer, alpha, beta):
    if terminal(board):
        return evaluation(board), None

    if maximizingPlayer:
        bestEval = -inf
        for each legal move:
            make move
            eval, _ = minimax(board, False, alpha, beta)
            undo move
            bestEval = max(bestEval, eval)
            alpha = max(alpha, eval)
            if alpha >= beta: break   # prune
        return bestEval, bestMove

    else:  # minimizing player
        bestEval = +inf
        for each legal move:
            make move
            eval, _ = minimax(board, True, alpha, beta)
            undo move
            bestEval = min(bestEval, eval)
            beta = min(beta, eval)
            if alpha >= beta: break   # prune
        return bestEval, bestMove
```

Because Tic-Tac-Toe is small, the AI currently explores to game end for exact play. That gives perfect play when using Minimax.

---

## Important implementation notes

* Files of interest:

  * `py-ttt-neat.py` - main game logic, Pygame UI, and AI implementation.
  * `CONSTANTS_TTT.PY` - sizes, colors, and drawing constants.

* `Board.final_state()` returns `0` for no win, `1` if player 1 wins, and `2` if player 2 wins.

* The Minimax implementation uses deep copies of the board to simulate moves. This is simple and safe but slower than using make/undo in-place moves.

---

## Known issues & quick fixes

* **Gamemode toggle small bug**

  * Current code in `Game.change_gamemode()` assigns `'ai '` (with a trailing space) in one branch. Later checks test for `== 'ai'`, which can prevent the AI from resuming after toggling.
  * Quick fix: replace the line in `py-ttt-neat.py`:

```py
# original
self.gamemode = 'ai ' if self.gamemode == 'pvp' else 'pvp'

# fixed
self.gamemode = 'ai' if self.gamemode == 'pvp' else 'pvp'
```

* **Restart logic**

  * The code in the main loop stores `board = game.board` and `ai = game.ai` and later, on restart, reassigns these old references back. A cleaner restart is to re-create the `Game` instance. For example:

```py
# replace the restart branch in KEYDOWN
if event.key == pygame.K_r:
    game = Game()
    board = game.board
    ai = game.ai
```

This avoids stale references and makes `restart()` unnecessary.

---

## Performance and complexity notes

* The branching factor for Tic-Tac-Toe starts at 9, then 8, then 7, and so on. The number of possible move sequences when the board is filled is `9! = 362,880`.
* Many games end earlier due to a win, so the actual number of explored nodes is smaller. Alpha-Beta pruning reduces the number of evaluated nodes, especially if good move ordering is used.

---

## Suggestions for improvements

* Replace `deepcopy` with in-place make/undo move. This reduces memory overhead and speeds up recursion.
* Add iterative deepening plus a transposition table (hash table) for caching repeated positions.
* Add a depth limit and a heuristic evaluation to support larger boards or to reduce thinking time.
* Add a command line option to choose who starts first and to set the AI player.
* Add automated tests for the core board logic and minimax correctness.
* Add a small CI workflow to run linting and tests.

---

## Project structure

```
├── py-ttt-neat.py          # main game + AI
├── CONSTANTS_TTT.PY        # drawing constants
├── assets/                 # add screenshots or gifs here
└── README.md
```

---

## Contributing

If you want to contribute:

1. Fork the repo.
2. Create a branch for your change.
3. Add tests where appropriate.
4. Send a pull request describing the change.

All improvements are welcome - small PRs that fix bugs or tidy code are perfect.

---

## License

This project is free to use. A suggested license is MIT. Create a `LICENSE` file containing the MIT text if you want to publish this project publicly.

---

## Contact

For questions, suggestions, or improvements, feel free to open an issue or submit a pull request.


THIS IS A SAMPLE GAME WHERE THE AI IS CIRCLE 

![image](https://github.com/user-attachments/assets/ec074965-2d28-442b-bcc2-44ed6db0c80e)

when i press R (RESET)

![image](https://github.com/user-attachments/assets/0613f371-0537-4622-a714-694b8f72ed85)

ANOTHER GAME

![image](https://github.com/user-attachments/assets/1a572483-1cdf-4930-99b0-7166cc81fb43)

WHEN self.player = 1 , the user/human starts playing 

![image](https://github.com/user-attachments/assets/62785557-60c4-44e5-b2f0-a18d62bb990b)
