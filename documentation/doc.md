# Abandoned Space Station

Lukas Richter, TIK24

## Table of Contents

- [Abandoned Space Station](#abandoned-space-station)
  - [Table of Contents](#table-of-contents)
  - [Project structure and Features](#project-structure-and-features)
    - [Requirements and Dependencies](#requirements-and-dependencies)
    - [Architecture](#architecture)
    - [User Interface](#user-interface)
    - [Program Flow](#program-flow)
  - [Metrics](#metrics)

## Project structure and Features
The game "Abandoned Space Station" is a logic game played in the console. The player must explore the zones, or cells, of a space station. The space station is represented as a grid of zones. In the zones, there may be traps. In order to explore the zones, the player can select zones that he wants to scan.

However, if there is a trap in the zone, the player will be killed and the game will be over. Otherwise, the scan will reveal the number of traps in the adjacent zones, i.e. diagonally and orthogonally neighboring zones. The player must logically deduce the positions of the traps and select the zones to scan accordingly.
The game ends when the player has successfully scanned all safe zones without triggering any traps. In this case, the player wins the game.

### Requirements and Dependencies
The project is written in Python 3.13.1 and uses the following modules:
- `unittest` for testing purposes
- `random` for generating random numbers (used in the Board generation)
- `os` for file operations (mainly used to create the PYTHONPATH)
- `sys` for system operations (used for setting the PYTHONPATH in order to use the project's modules)


### Architecture

### User Interface

### Program Flow

## Metrics

