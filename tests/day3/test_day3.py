from pathlib import Path

from aoc_2023.day3.day3 import Day3PuzzleSolver
from aoc_2023.utils import PUZZLE_VARIANT

TEST_PUZZLE_INPUT = (
    Path(__file__).parent.absolute().joinpath("test_day3_puzzle_input.txt")
)

TEST_PUZZLE_PART_1_SOLUTION = 4361


def test_solve_part_1():
    solver = Day3PuzzleSolver(TEST_PUZZLE_INPUT, PUZZLE_VARIANT.PART1)
    solver.solve()
    assert solver.solution == TEST_PUZZLE_PART_1_SOLUTION
