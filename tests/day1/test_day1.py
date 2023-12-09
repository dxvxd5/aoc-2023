from pathlib import Path

from aoc_2023.day1.day1 import Day1PuzzleSolver
from aoc_2023.utils import PUZZLE_VARIANT

TEST_PUZZLE_PART_1_INPUT = (
    Path(__file__).parent.absolute().joinpath("test_day1_puzzle_part_1_input.txt")
)

TEST_PUZZLE_PART_2_INPUT = (
    Path(__file__).parent.absolute().joinpath("test_day1_puzzle_part_2_input.txt")
)

TEST_PUZZLE_PART_1_SOLUTION = 142
TEST_PUZZLE_PART_2_SOLUTION = 281


def test_solve_part_1():
    solver = Day1PuzzleSolver(TEST_PUZZLE_PART_1_INPUT)
    solver.solve()
    assert solver.solution == TEST_PUZZLE_PART_1_SOLUTION


def test_solve_part_2():
    solver = Day1PuzzleSolver(
        TEST_PUZZLE_PART_2_INPUT, puzzle_variant=PUZZLE_VARIANT.PART2
    )
    solver.solve()
    assert solver.solution == TEST_PUZZLE_PART_2_SOLUTION
