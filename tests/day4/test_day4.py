from pathlib import Path

from aoc_2023.day4.day4 import Day4PuzzleSolver
from aoc_2023.utils import PUZZLE_VARIANT

TEST_PUZZLE_INPUT = (
    Path(__file__).parent.absolute().joinpath("test_day4_puzzle_input.txt")
)

TEST_PUZZLE_PART_1_SOLUTION = 13
TEST_PUZZLE_PART_2_SOLUTION = 30


def test_solve_part1():
    solver = Day4PuzzleSolver(TEST_PUZZLE_INPUT, puzzle_variant=PUZZLE_VARIANT.PART1)
    solver.solve()
    assert solver.solution == TEST_PUZZLE_PART_1_SOLUTION


def test_solve_part2():
    solver = Day4PuzzleSolver(TEST_PUZZLE_INPUT, puzzle_variant=PUZZLE_VARIANT.PART2)
    solver.solve()
    assert solver.solution == TEST_PUZZLE_PART_2_SOLUTION
