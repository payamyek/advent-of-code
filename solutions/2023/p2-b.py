from typing import List, Dict, Tuple
from aocd import data, submit

MAX_RED_CUBES = 12
MAX_GREEN_CUBES = 13
MAX_BLUE_CUBES = 14

RED_CUBE = "red"
GREEN_CUBE = "green"
BLUE_CUBE = "blue"


def min_cube_colours(turns: List[Dict[str, int]]) -> Dict[str, int]:
    min_colours = {RED_CUBE: 0, GREEN_CUBE: 0, BLUE_CUBE: 0}

    for turn in turns:
        for k, v in turn.items():
            min_colours[k] = max(v, min_colours[k])
    return min_colours


def parse_game_turn(game: str) -> Tuple[int, List[Dict[str, int]]]:
    turns = [turn.split(",") for turn in game.split(":")[1].strip().split(";")]
    parsed_turns = []

    for turn in turns:
        parsed_turn = {}
        for cube in turn:
            if cube.endswith(RED_CUBE):
                parsed_turn[RED_CUBE] = int(cube.split()[0])
            elif cube.endswith(GREEN_CUBE):
                parsed_turn[GREEN_CUBE] = int(cube.split()[0])
            elif cube.endswith(BLUE_CUBE):
                parsed_turn[BLUE_CUBE] = int(cube.split()[0])
        parsed_turns.append(parsed_turn)
    return parsed_turns


sum = 0

for game in data.splitlines():
    turn = parse_game_turn(game)

    min_colours = min_cube_colours(turn)
    sum = sum + min_colours.get(RED_CUBE) * min_colours.get(
        BLUE_CUBE
    ) * min_colours.get(GREEN_CUBE)

submit(sum)
