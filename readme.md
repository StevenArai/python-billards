

# Python Billiards  Course Design
English | [简体中文](README_zh-cn.md)
## Project Overview
This project is a Python billiards  course design, primarily implementing a simple billiards . The game interface uses the Pygame library, and the physics engine is powered by Pymunk.

## Features
- Cue stick ball strike
- Collision between balls
- Balls pocketing
- Player turn switching and transfer
- Free ball rule
- Game over condition

## Environment Requirements
- Python 3.12.8
- Pygame 2.6.0 (SDL 2.28.4)
- Pymunk 1.17.1

## Installing Dependencies
Run the following command in the project root directory to install the dependencies:
```
pip install pygame pymunk
```

## Running the Game
Run the following command in the project root directory to start the game:
```
python main.py
```

## Game Rules
- Balls are divided into solid balls, striped balls, black ball, and white ball.
- Collisions between balls will change their movement direction and speed.
- Players use the cue stick to strike the white ball, which in turn makes the colored balls pocket and switches the player turn.
- The game ends when one player pockets all the colored balls, and the other player loses.
- If the black ball is pocketed, the game ends immediately, and the player who pocketed the black ball loses.

## Notes
- The `main.py` code has been obfuscated and compressed to speed up the explanation. If you wish to read the source code, please refer to `raw.py`.
- Design documents of the game(PSD) are in the `design` folder, for reference.
