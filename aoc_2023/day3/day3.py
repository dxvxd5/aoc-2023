from functools import reduce
from operator import mul
from pathlib import Path
from typing import List

from aoc_2023.utils import PUZZLE_VARIANT, PuzzleSolver

PUZZLE_INPUT = str(Path(__file__).parent.absolute().joinpath("day3_puzzle_input.txt"))


class Day3PuzzleSolver(PuzzleSolver):
    @staticmethod
    def __find_next_number_starting_at_idx(
        line: str, start_index=0
    ) -> tuple[str | None, int | None]:
        potential_number = ""
        number_start_at: int | None = None

        for idx, char in enumerate(line[start_index:]):
            if char.isdigit():
                if number_start_at is None:
                    number_start_at = idx + start_index

                potential_number += char
            else:
                if potential_number:
                    return (potential_number, number_start_at)

        return (potential_number or None, number_start_at)

    @staticmethod
    def __find_number_surroundings_in_text(
        number: str,
        number_pos_in_line: int,
        current_line: str,
        previous_line: str | None,
        next_line: str | None,
    ) -> str:
        number_surroundings: str = ""
        horizontal_range = (
            number_pos_in_line - 1 if number_pos_in_line else 0,
            -2
            if (number_pos_in_line + len(number) == len(current_line))
            else number_pos_in_line + len(number),
        )

        if previous_line is not None:
            number_surroundings += previous_line[
                horizontal_range[0] : horizontal_range[1] + 1
            ]

        if next_line is not None:
            number_surroundings += next_line[
                horizontal_range[0] : horizontal_range[1] + 1
            ]

        if horizontal_range[0] > 0:
            number_surroundings += current_line[horizontal_range[0]]

        if horizontal_range[1] != -1:
            number_surroundings += current_line[horizontal_range[1]]

        return number_surroundings

    # !Refactor this function pae vraiment
    @staticmethod
    # trunk-ignore(pylint/R0913)
    # trunk-ignore(pylint/R0912)
    def find_potential_gears_surrounding_number(
        number: str,
        number_pos_in_line: int,
        current_line: str,
        current_line_index: int,
        previous_line: str | None,
        next_line: str | None,
    ):
        gear_tracker: dict[tuple[int, int], List[int]] = {}

        horizontal_range = (
            number_pos_in_line - 1 if number_pos_in_line else 0,
            len(current_line) - 1
            if (number_pos_in_line + len(number) == len(current_line))
            else number_pos_in_line + len(number),
        )

        if previous_line is not None:
            for idx in range(horizontal_range[0], horizontal_range[1] + 1):
                char = previous_line[idx]
                if char == "*":
                    key = (current_line_index - 1, idx)
                    if key in gear_tracker:
                        gear_tracker[key].append(int(number))
                    else:
                        gear_tracker[key] = [int(number)]

        if next_line is not None:
            for idx in range(horizontal_range[0], horizontal_range[1] + 1):
                char = next_line[idx]
                if char == "*":
                    key = (current_line_index + 1, idx)
                    if key in gear_tracker:
                        gear_tracker[key].append(int(number))
                    else:
                        gear_tracker[key] = [int(number)]

        if horizontal_range[0] > 0:
            if current_line[horizontal_range[0]] == "*":
                key = (current_line_index, horizontal_range[0])
                if key in gear_tracker:
                    gear_tracker[key].append(int(number))
                else:
                    gear_tracker[key] = [int(number)]

        if horizontal_range[1] != -1:
            if current_line[horizontal_range[1]] == "*":
                key = (current_line_index, horizontal_range[1])
                if key in gear_tracker:
                    gear_tracker[key].append(int(number))
                else:
                    gear_tracker[key] = [int(number)]

        return gear_tracker

    def solve(self) -> None:
        part_numbers_sum = 0
        potential_gears_tracker: dict[tuple[int, int], List[int]] = {}

        for line_index, line in enumerate(self.puzzle_data):
            previous_line = self.puzzle_data[line_index - 1] if line_index else None

            next_line = (
                self.puzzle_data[line_index + 1]
                if line_index + 1 < len(self.puzzle_data)
                else None
            )

            index_in_line = 0
            while index_in_line < len(line):
                (
                    next_number_in_line,
                    number_pos_in_line,
                ) = Day3PuzzleSolver.__find_next_number_starting_at_idx(
                    line, index_in_line
                )

                if next_number_in_line is None or number_pos_in_line is None:
                    break

                number_surroundings = (
                    Day3PuzzleSolver.__find_number_surroundings_in_text(
                        next_number_in_line,
                        number_pos_in_line,
                        line,
                        previous_line,
                        next_line,
                    )
                )

                potential_gears_surrounding_number = (
                    Day3PuzzleSolver.find_potential_gears_surrounding_number(
                        next_number_in_line,
                        number_pos_in_line,
                        line,
                        line_index,
                        previous_line,
                        next_line,
                    )
                )

                for key, value in potential_gears_surrounding_number.items():
                    if key in potential_gears_tracker:
                        potential_gears_tracker[key].extend(value)
                    else:
                        potential_gears_tracker[key] = value

                index_in_line = number_pos_in_line + len(next_number_in_line)

                is_part_number = any(
                    not char.isdigit() and char != "." for char in number_surroundings
                )

                if is_part_number:
                    part_numbers_sum += int(next_number_in_line)

        sum_of_gear_ratios = sum(
            [
                reduce(mul, gear_numbers)
                for gear_numbers in potential_gears_tracker.values()
                if len(gear_numbers) == 2
            ]
        )

        print(f"Sum of gear ratios: {sum_of_gear_ratios}")

        # Ignoring: W0201: Attribute 'solution' defined outside __init__
        # Reason: It is defined in the abstract base class __init__
        # trunk-ignore(pylint/W0201)
        self.solution = part_numbers_sum


if __name__ == "__main__":
    solver = Day3PuzzleSolver(PUZZLE_INPUT, PUZZLE_VARIANT.PART1)
    solver.solve()
    print(solver.solution)
