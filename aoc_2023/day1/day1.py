from pathlib import Path

from aoc_2023.utils import PUZZLE_VARIANT, PuzzleSolver

PUZZLE_INPUT = str(Path(__file__).parent.absolute().joinpath("day1_puzzle_input.txt"))
# PUZZLE_INPUT = str(Path(__file__).parent.absolute().joinpath("input.txt"))


class Day1PuzzleSolver(PuzzleSolver):
    __spelled_digit_to_digit = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    # maps the first letter of a spelled digit  to the length of the
    # longest (in spelling) digit it could be
    __first_letter_to_digit_length = {
        "o": 3,
        "t": 5,
        "f": 4,
        "s": 5,
        "e": 5,
        "n": 4,
    }

    @staticmethod
    def __is_beginning_of_spelled_digit(letter: str) -> bool:
        return letter in Day1PuzzleSolver.__first_letter_to_digit_length

    @staticmethod
    def __find_spelled_digit_starting_at_idx(idx, line) -> str | None:
        max_length_of_potential_spelled_digit = (
            Day1PuzzleSolver.__first_letter_to_digit_length.get(line[idx])
        )

        if max_length_of_potential_spelled_digit is None:
            return None

        find_in = line[idx : idx + max_length_of_potential_spelled_digit]

        for spelled_digit in Day1PuzzleSolver.__spelled_digit_to_digit:
            if find_in.startswith(spelled_digit):
                return spelled_digit

        return None

    def __get_line_calibration_number(self, line: str) -> int:
        first_digit_in_line = ""
        last_digit_in_line = ""

        idx = 0

        while idx < len(line):
            next_digit_in_line: str | None = None

            # char can be either a digit (e.g. "1") or the beginning of a spelled digit
            # (e.g. "o" in "one") or none of those
            char = line[idx]

            if char.isdigit():
                next_digit_in_line = char

            # if it is the beginning of a spelled digit, we will find that spelled digit
            # and set next_digit_in_line to the digit it represents
            # !NOTE: We only need to check spelled digits if the puzzle
            # !variant is PART2
            elif (
                self.puzzle_variant == PUZZLE_VARIANT.PART2
                and Day1PuzzleSolver.__is_beginning_of_spelled_digit(char)
            ):
                potential_spelled_digit = (
                    Day1PuzzleSolver.__find_spelled_digit_starting_at_idx(idx, line)
                )

                if potential_spelled_digit is not None:
                    next_digit_in_line = Day1PuzzleSolver.__spelled_digit_to_digit[
                        potential_spelled_digit
                    ]
                    idx += len(potential_spelled_digit) - 2

            if next_digit_in_line is not None:
                if first_digit_in_line == "":
                    first_digit_in_line = last_digit_in_line = next_digit_in_line
                else:
                    last_digit_in_line = next_digit_in_line

            idx += 1

        if first_digit_in_line == "" and last_digit_in_line == "":
            return 0

        return int(f"{first_digit_in_line}{last_digit_in_line}")

    def solve(self):
        sum_of_calibration_numbers = 0

        for line in self.puzzle_data:
            line_calibration_number = self.__get_line_calibration_number(line)
            sum_of_calibration_numbers += line_calibration_number

        # Ignoring: W0201: Attribute 'solution' defined outside __init__
        # Reason: It is defined in the abstract base class __init__
        # trunk-ignore(pylint/W0201)
        self.solution = sum_of_calibration_numbers


if __name__ == "__main__":
    solver = Day1PuzzleSolver(PUZZLE_INPUT, PUZZLE_VARIANT.PART2)
    solver.solve()
    print(solver.solution)
