from functools import reduce
from operator import mul
from pathlib import Path
from typing import List

from aoc_2023.utils import PUZZLE_VARIANT, PuzzleSolver

PUZZLE_INPUT = str(Path(__file__).parent.absolute().joinpath("day2_puzzle_input.txt"))


class Day2PuzzleSolver(PuzzleSolver):
    __part_1_bag_content = {"red": 12, "green": 13, "blue": 14}

    @staticmethod
    def __extract_game_set_elt_info(game_set_elt: str) -> tuple[int, str]:
        number, color = game_set_elt.strip().split()

        if color not in Day2PuzzleSolver.__part_1_bag_content:
            raise ValueError(f"Invalid color: {color}")

        if not number.isdigit():
            raise ValueError(f"Invalid number: {number}")

        return int(number), color

    @staticmethod
    def __is_game_set_possible(game_set: str) -> bool:
        for elt in game_set.split(","):
            elt_number, elt_color = Day2PuzzleSolver.__extract_game_set_elt_info(elt)
            if elt_number > Day2PuzzleSolver.__part_1_bag_content[elt_color]:
                return False

        return True

    @staticmethod
    def __is_game_possible(game_sets: List[str]) -> bool:
        return all(
            Day2PuzzleSolver.__is_game_set_possible(game_set) for game_set in game_sets
        )

    @staticmethod
    def __get_fewest_cubes_needed_for_game(game_sets: List[str]) -> dict[str, int]:
        # Assumption: We will always draw at least one cube of each color in
        # each game set
        fewest_cubes_needed = {
            "red": 1,
            "green": 1,
            "blue": 1,
        }

        for game_set in game_sets:
            for elt in game_set.split(","):
                elt_number, elt_color = Day2PuzzleSolver.__extract_game_set_elt_info(
                    elt
                )

                if elt_number > fewest_cubes_needed[elt_color]:
                    fewest_cubes_needed[elt_color] = elt_number

        return fewest_cubes_needed

    @staticmethod
    def __get_power_of_game(game_sets: List[str]) -> int:
        fewest_cubes_needed = Day2PuzzleSolver.__get_fewest_cubes_needed_for_game(
            game_sets
        )
        return reduce(mul, fewest_cubes_needed.values())

    @staticmethod
    def __extract_game_info(game: str):
        game_name, game_sets = game.split(":")
        game_id = game_name.split()[-1]

        if not game_id.isdigit():
            raise ValueError(f"Invalid game id: {game_id}")

        game_sets_list = game_sets.split(";")

        return game_id, game_sets_list

    def __solve_part_1(self):
        sum_of_valid_games_id = 0

        for game in self.puzzle_data:
            game_id, game_sets = Day2PuzzleSolver.__extract_game_info(game)
            if Day2PuzzleSolver.__is_game_possible(game_sets):
                sum_of_valid_games_id += int(game_id)

        # Ignoring: W0201: Attribute 'solution' defined outside __init__
        # Reason: It is defined in the abstract base class __init__
        # trunk-ignore(pylint/W0201)
        self.solution = sum_of_valid_games_id

    def __solve_part_2(self):
        sum_of_games_powers = 0

        for game in self.puzzle_data:
            _, game_sets = Day2PuzzleSolver.__extract_game_info(game)
            sum_of_games_powers += Day2PuzzleSolver.__get_power_of_game(game_sets)

        # Ignoring: W0201: Attribute 'solution' defined outside __init__
        # Reason: It is defined in the abstract base class __init__
        # trunk-ignore(pylint/W0201)
        self.solution = sum_of_games_powers

    def solve(self):
        if self.puzzle_variant == PUZZLE_VARIANT.PART1:
            self.__solve_part_1()
        else:
            self.__solve_part_2()


if __name__ == "__main__":
    solver = Day2PuzzleSolver(PUZZLE_INPUT, PUZZLE_VARIANT.PART2)
    solver.solve()
    print(solver.solution)
