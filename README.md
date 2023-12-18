# Pacman AI Project

## Overview

This project involves implementing various search algorithms and heuristics to help Pacman navigate through mazes, find paths, and collect food efficiently. The code includes both search algorithms and search-based agents.

## Getting Started

1. Download the project code and extract the contents.

2. Run a game of Pacman using the following command:
   ```bash
   python3 pacman.py
Project Structure
The project is organized into several files:

search.py: Contains the implementation of search algorithms.
searchAgents.py: Houses search-based agents for Pacman.
pacman.py: The main file for running Pacman games.
game.py: Defines the logic of the Pacman world.
util.py: Provides useful data structures for search algorithms.
Files to Edit

Primarily, the work is on:

search.py: Implement search algorithms (DFS, BFS, UCS, A*) in this file.
searchAgents.py: Implement search-based agents, including heuristics, in this file.


Running Search Agents
You can test your search algorithms and agents using commands like:
bash
Copy code
python3 pacman.py -l tinyMaze -p SearchAgent -a fn=tinyMazeSearch
python3 pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
python3 pacman.py -l bigMaze -p SearchAgent -a fn=ucs
python3 pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
python3 pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
python3 pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5
python3 pacman.py -l trickySearch -p AStarFoodSearchAgent

Acknowledgments
The project is part of a series of assignments from Introduction to AI at University of Toronto. Special thanks to the course staff for their guidance.

Feel free to reach out for any questions or clarifications!
