from typing import List, Dict, Tuple
from aocd import data, submit

MAX_RED_CUBES = 12
MAX_GREEN_CUBES = 13
MAX_BLUE_CUBES = 14

RED_CUBE = "red"
GREEN_CUBE = "green"
BLUE_CUBE = "blue"


def possible_game(turns: List[Dict[str, int]]) -> bool:
    for turn in turns:
        if turn.get(RED_CUBE) is not None and turn.get(RED_CUBE) > MAX_RED_CUBES:
            return False
        elif (
            turn.get(GREEN_CUBE) is not None and turn.get(GREEN_CUBE) > MAX_GREEN_CUBES
        ):
            return False
        elif turn.get(BLUE_CUBE) is not None and turn.get(BLUE_CUBE) > MAX_BLUE_CUBES:
            return False
    return True


def parse_game_turn(game: str) -> Tuple[int, List[Dict[str, int]]]:
    turn_id = int(game.split(":")[0].split()[1])
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
    return turn_id, parsed_turns


sum = 0

for game in data.splitlines():
    turn_id, turn = parse_game_turn(game)
    if possible_game(turn):
        sum = sum + turn_id

submit(sum)
