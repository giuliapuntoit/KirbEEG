# KirbEEG

Content of this repository:
* `singleplayer.py` contains the code for running a single player KirbEEG game.
* `player2.py` contains the code for running 2-player KirbEEG game. 
* `gallery` folder contains sprites and audio sounds for the game. Sprites contain all images used to show the game, while sounds are used only when winning for now. 
* `players2` folder contains background used specifically for 2-player version.


## Quickstart

To run the game, download the entire folder. Be sure to have pygame installed in your computer, otherwise you can install it through:

```
pip install pygame
```

You can start the game running the command (2 players):

```
python player2.py
``` 

or (single player):

```
python singleplayer.py
```

You can control the game keyboards input. We use "space" and "up" for single player. For 2-player version, we use "a" to go up and "s" to go down for player 1, "b" to go up and "n" to go down for player 2, and "space" to start the game.

When started, the 2-player game should look like this:

<p align="center"><img src="./welcome.png" height="400"></p>

<p align="center"><img src="./2players.png" height="400"></p>
